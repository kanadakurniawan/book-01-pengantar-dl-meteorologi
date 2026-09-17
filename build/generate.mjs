import { execSync } from 'node:child_process';
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const manuscriptsDir = join(root, 'manuscripts');
const frontMatterDir = join(root, 'front-matter');
const backMatterDir = join(root, 'back-matter');
const releasesDir = join(root, 'releases');
const previewDir = join(root, 'preview');

const bookTitle = 'Pengantar Deep Learning untuk Meteorologi';

function hasTool(name) {
	try {
		execSync(`${name} --version`, { stdio: 'ignore' });
		return true;
	} catch {
		return false;
	}
}

// --- Mode -----------------------------------------------------------------
// Zonder `--version`     -> PREVIEW: cuma 1 file PDF buku utuh naar `preview/`,
//                           folder wordt elke keer overschreven. Geen versie,
//                           geen MANIFEST, geen 'rilis'.
// Met `--version=vX.Y.Z` -> RELEASE: volledige bundel naar `releases/<versie>/`
//                           (PDF+DOCX buku utuh, per bab, MANIFEST.md).
const args = process.argv.slice(2);
const versionArg = args.find((a) => a.startsWith('--version='));
const bareVersionFlag = args.includes('--version');
const isPreview = !versionArg && !bareVersionFlag;
let version = null;
if (versionArg) {
	version = versionArg.split('=')[1].trim();
	if (!/^v\d+\.\d+\.\d+$/.test(version)) {
		console.error('Usage: node build/generate.mjs --version=vX.Y.Z (of zonder --version voor preview)');
		process.exit(1);
	}
} else if (bareVersionFlag) {
	console.error('--version vereist een waarde: --version=vX.Y.Z (of laat --version weg voor preview)');
	process.exit(1);
}
const outDir = isPreview ? previewDir : join(releasesDir, version);

if (isPreview) {
	rmSync(previewDir, { recursive: true, force: true });
}
mkdirSync(outDir, { recursive: true });

const hasPandoc = hasTool('pandoc');
const hasLatex = hasTool('pdflatex') || hasTool('xelatex') || hasTool('lualatex');

console.log(
	`Generating ${isPreview ? `PREVIEW (cuma liat format, naar ${outDir})` : `RELEASE ${version} (naar ${outDir})`}`,
);
console.log(`  pandoc: ${hasPandoc ? 'OK' : 'TIDAK ADA'} | LaTeX: ${hasLatex ? 'OK' : 'TIDAK ADA'}`);

// --- Utilitas Markdown ----------------------------------------------------

/** Strip blok front matter YAML (--- ... ---) di awal berkas. */
function stripFrontmatter(text) {
	return text.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/, '');
}

/** Tulis ulang path gambar `figures/...` menjadi absolut (buku utuh di-out-dir). */
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

// --- Sumber (front matter + bab + back matter) ------------------------------

const chapterDirs = readdirSync(manuscriptsDir, { withFileTypes: true })
	.filter((d) => d.isDirectory() && !d.name.startsWith('.'))
	.map((d) => d.name)
	.sort();

if (chapterDirs.length === 0) {
	console.warn('Tidak ada bab di manuscripts/ — tambahkan folder ch-0N-<slug>/master.md');
	process.exit(0);
}

// Daftar Isi disimpan sebagai berkas `02-daftar-isi.md` en disertakan pada
// posisi die correct is (na hak cipta & lisensi). Voor edisi cetak die
// paginanummers nodig heeft, voeg `--toc` toe aan het pandoc-commando.
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

if (!hasPandoc) {
	console.warn('  SKIP build: pandoc tidak terpasang. Install dari https://pandoc.org');
	process.exit(0);
}

const orderedFiles = [
	...frontMatter.map((f) => f.content),
	...chapters.map((c) => c.content),
	...backMatter.map((f) => f.content),
].map((content, i) =>
	// Halaman baru antar bagian (PDF); raw LaTeX diabaikan di DOCX.
	`${i === 0 ? '' : '\\newpage\n\n'}${content}`,
);

const bookMd = join(outDir, '_buku-utuh.md');
writeFileSync(bookMd, orderedFiles.join('\n\n'), 'utf8');

// --- Buku utuh PDF (altijd; bij preview de enige output) --------------------

if (hasLatex) {
	try {
		execSync(
			`pandoc "${bookMd}" --metadata title="${bookTitle}" ` +
				`--metadata author="Kanada Kurniawan" --metadata lang=id ` +
				`--pdf-engine=xelatex -o "${join(outDir, 'buku-pengantar-dl-meteorologi.pdf')}"`,
			{ stdio: 'ignore' },
		);
		console.log('  OK  buku-pengantar-dl-meteorologi.pdf (buku utuh)');
	} catch (e) {
		console.error(`  GAGAL pdf buku utuh: ${e.message}`);
	}
} else {
	console.warn('  SKIP buku utuh .pdf (LaTeX tidak terpasang)');
}

if (isPreview) {
	rmSync(bookMd, { force: true });
	console.log(`Selesai. Preview (1 file): ${join(outDir, 'buku-pengantar-dl-meteorologi.pdf')}`);
	process.exit(0);
}

// --- RELEASE only: DOCX buku utuh -------------------------------------------

try {
	execSync(
		`pandoc "${bookMd}" --metadata title="${bookTitle}" ` +
			`--metadata author="Kanada Kurniawan" --metadata lang=id ` +
			`-o "${join(outDir, 'buku-pengantar-dl-meteorologi.docx')}"`,
		{ stdio: 'ignore' },
	);
	console.log('  OK  buku-pengantar-dl-meteorologi.docx (buku utuh)');
} catch (e) {
	console.error(`  GAGAL docx buku utuh: ${e.message}`);
}

// --- RELEASE only: output per bab (met citeproc bila er refs.bib is) ---------

for (const ch of chapters) {
	const bib = join(manuscriptsDir, ch.name, 'refs.bib');
	const chDir = join(manuscriptsDir, ch.name);
	const outBase = join(outDir, ch.name);
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

rmSync(bookMd, { force: true });

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
writeFileSync(join(outDir, 'MANIFEST.md'), manifest, 'utf8');

console.log(`Selesai. Rilis: ${outDir}`);