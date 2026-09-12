import { execSync } from 'node:child_process';
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const manuscriptsDir = join(root, 'manuscripts');
const frontMatterDir = join(root, 'front-matter');
const backMatterDir = join(root, 'back-matter');
const releasesDir = join(root, 'releases');

function hasTool(name) {
	try {
		execSync(`${name} --version`, { stdio: 'ignore' });
		return true;
	} catch {
		return false;
	}
}

const args = process.argv.slice(2);
const versionArg = args.find((a) => a.startsWith('--version='));
if (!versionArg) {
	console.error('Usage: node build/generate.mjs --version=v2.0.0');
	process.exit(1);
}
const version = versionArg.split('=')[1];
const releaseDir = join(releasesDir, version);
mkdirSync(releaseDir, { recursive: true });

const hasPandoc = hasTool('pandoc');
const hasLatex = hasTool('pdflatex') || hasTool('xelatex') || hasTool('lualatex');

console.log(`Generating release ${version}`);
console.log(`  pandoc: ${hasPandoc ? 'OK' : 'TIDAK ADA'} | LaTeX: ${hasLatex ? 'OK' : 'TIDAK ADA'}`);

// --- Utilitas Markdown -------------------------------------------------------

/** Strip blok front matter YAML (--- ... ---) di awal berkas. */
function stripFrontmatter(text) {
	return text.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/, '');
}

/** Tulis ulang path gambar `figures/...` menjadi absolut (buku utuh di-release-dir). */
function rewriteFigurePaths(content, chDir) {
	return content.replace(/!\[([^\]]*)\]\(figures\/([^)]+)\)/g, (_m, alt, src) => {
		const full = join(manuscriptsDir, chDir, 'figures', src);
		return `![${alt}](${full.replace(/\\/g, '/')})`;
	});
}

/** Terapkan konvensi buku utuh: TOC di sisi Pdf di-generate pandoc --toc. */
function loadSectionFiles(dir, { excludeNames = [] } = {}) {
	if (!existsSync(dir)) return [];
	return readdirSync(dir)
		.filter((f) => f.endsWith('.md'))
		.filter((f) => !excludeNames.includes(f))
		.sort()
		.map((f) => {
			const full = join(dir, f);
			return {
				name: f,
				content: stripFrontmatter(readFileSync(full, 'utf8')),
			};
		});
}

// --- Buku utuh (front matter + bab + back matter) ----------------------------

const chapterDirs = readdirSync(manuscriptsDir, { withFileTypes: true })
	.filter((d) => d.isDirectory() && !d.name.startsWith('.'))
	.map((d) => d.name)
	.sort();

if (chapterDirs.length === 0) {
	console.warn('Tidak ada bab di manuscripts/ — tambahkan folder ch-0N-<slug>/master.md');
	process.exit(0);
}

// Daftar Isi disimpan sebagai berkas `02-daftar-isi.md` dan disertakan pada
// posisi yang benar (setelah hak cipta & lisensi). Untuk edisi cetak yang
// membutuhkan nomor halaman, tambahkan flag `--toc` pada perintah pandoc
// (TOC otomatis) dan pindahkan letaknya sesuai urutan standar buku.
const frontMatter = loadSectionFiles(frontMatterDir);
const backMatter = loadSectionFiles(backMatterDir);

const chapters = chapterDirs
	.map((ch) => {
		const master = join(manuscriptsDir, ch, 'master.md');
		if (!existsSync(master)) return null;
		return {
			name: ch,
			path: master,
			content: rewriteFigurePaths(stripFrontmatter(readFileSync(master, 'utf8')), ch),
		};
	})
	.filter(Boolean);

const bookTitle = 'Pengantar Deep Learning untuk Meteorologi';

if (hasPandoc) {
	const orderedFiles = [
		...frontMatter.map((f) => f.content),
		...chapters.map((c) => c.content),
		...backMatter.map((f) => f.content),
	].map((content, i) =>
		// Halaman baru antar bagian (PDF); raw LaTeX diabaikan di DOCX.
		`${i === 0 ? '' : '\\newpage\n\n'}${content}`,
	);

	const bookMd = join(releaseDir, '_buku-utuh.md');
	writeFileSync(bookMd, orderedFiles.join('\n\n'), 'utf8');

	// Bangun DOCX
	try {
		execSync(
			`pandoc "${bookMd}" --metadata title="${bookTitle}" ` +
				`--metadata author="Kanada Kurniawan" --metadata lang=id ` +
				`-o "${join(releaseDir, 'buku-pengantar-dl-meteorologi.docx')}"`,
			{ stdio: 'ignore' },
		);
		console.log(`  OK  buku-pengantar-dl-meteorologi.docx (buku utuh)`);
	} catch (e) {
		console.error(`  GAGAL docx buku utuh: ${e.message}`);
	}

	// Bangun PDF
	if (hasLatex) {
		try {
			execSync(
				`pandoc "${bookMd}" --metadata title="${bookTitle}" ` +
					`--metadata author="Kanada Kurniawan" --metadata lang=id ` +
					`--pdf-engine=xelatex -o "${join(releaseDir, 'buku-pengantar-dl-meteorologi.pdf')}"`,
				{ stdio: 'ignore' },
			);
			console.log(`  OK  buku-pengantar-dl-meteorologi.pdf (buku utuh)`);
		} catch (e) {
			console.error(`  GAGAL pdf buku utuh: ${e.message}`);
		}
	} else {
		console.warn(`  SKIP buku utuh .pdf (LaTeX tidak terpasang)`);
	}

	rmSync(bookMd, { force: true });

	// Output per bab (dengan citeproc bila ada refs.bib) — tetap dipertahankan.
	for (const ch of chapters) {
		const bib = join(manuscriptsDir, ch.name, 'refs.bib');
		const chDir = join(manuscriptsDir, ch.name);
		const outBase = join(releaseDir, ch.name);
		const bibOpts = existsSync(bib) ? `--citeproc --bibliography="${bib}"` : '';
		const resOpts = `--resource-path="${chDir}"`;
		try {
			execSync(`pandoc "${ch.path}" ${bibOpts} ${resOpts} -o "${outBase}.docx"`, { stdio: 'ignore' });
			console.log(`  OK  ${ch.name}.docx`);
		} catch (e) {
			console.error(`  GAGAL docx ${ch.name}: ${e.message}`);
		}
		if (hasLatex) {
			try {
				execSync(`pandoc "${ch.path}" ${bibOpts} ${resOpts} -o "${outBase}.pdf" --pdf-engine=xelatex`, {
					stdio: 'ignore',
				});
				console.log(`  OK  ${ch.name}.pdf`);
			} catch (e) {
				console.error(`  GAGAL pdf ${ch.name}: ${e.message}`);
			}
		} else {
			console.warn(`  SKIP ${ch.name}.pdf (LaTeX tidak terpasang)`);
		}
	}
} else {
	console.warn('  SKIP build: pandoc tidak terpasang. Install dari https://pandoc.org');
}

// Manifes rilis
const manifest = [
	`# Release ${version}`,
	``,
	`Dirilis: ${new Date().toISOString()}`,
	``,
	`## Isi bundel`,
	``,
	`- Buku utuh (PDF + DOCX): \`buku-pengantar-dl-meteorologi.pdf\`, \`buku-pengantar-dl-meteorologi.docx\``,
	`- Output per bab: \`ch-<NN>-*/master.md\` → \`ch-<NN>-*.pdf\` / \`ch-<NN>-*.docx\``,
	`- Sumber: \`front-matter/\`, \`manuscripts/\`, \`back-matter/\` (lihat README)`,
].join('\n');
writeFileSync(join(releaseDir, 'MANIFEST.md'), manifest, 'utf8');

console.log(`Selesai. Rilis: ${releaseDir}`);