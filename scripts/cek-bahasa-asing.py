#!/usr/bin/env python3
"""Check for Dutch/Italian-origin contamination in the Indonesian manuscripts.

This book is written in an Indonesian "pengantar" register whose words are
tanpa, dengan, hanya, untuk, satu, tidak, etc. During long edits, Dutch
function words (zonder, met, niet, alleen, voor, uit, een, de, het, ...)
and Italian words (ovvero, già, tutto, altre, finali, ...) creeped into the
text. This script scans all manuscripts for those signal words and reports
file:line:word so the author can replace them.

Usage:
    python scripts/cek-bahasa-asing.py
    python scripts/cek-bahasa-asing.py --file manuscripts/ch-02-regresi-neural-network/master.md
    python scripts/cek-bahasa-asing.py --chat --file <draft-chat.md>

--chat: also enforce the AGENTS.md section 2 chat banlist (words that are
forbidden in CHAT prose but legitimately used inside the book register).

Exit code: 0 = clean, 1 = hits found.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Dutch/Italian-origin signal words that do NOT belong to the register.
# Words that DO belong (dan, tidak, di, satu, hanya, untuk, dengan, tanpa)
# are intentionally NOT in this list.
# Note: "in" and "op" are omitted to avoid false positives inside terms
# like "input" or "ops"; strip code fences/inline code before matching.
BANNED = {
    "zonder", "met", "en", "niet", "alleen", "voor", "uit", "van",
    "een", "het", "de", "wordt", "zijn", "heeft", "hebt",
    "maar", "als", "wat", "hoe", "waarom", "daarom", "ook",
    "welke", "waar", "dat", "dit", "geen", "omdat", "zodat",
    "meer", "eerder", "later", "door", "over", "tussen",
    "twee", "drie", "hier", "daar", "wijkt", "geldt", "heet", "noemt",
    "kunnen", "zien", "betekenen", "voorspelling", "levert",
    "invoer", "uitvoer", "verborgen", "laag", "lagen",
    "nodig", "vroeg", "naar", "goed", "fout", "zelfde", "gewoon",
    "eigenlijk", "komt", "gaat", "zou", "moet", "kan", "wel", "ook",
    # tokens gevonden in chat-contaminatie (ronda 3): geëvalueerd, deze,
    # geabsorbeerd, moeten, rechtop, schuin, ter, één, regels, bestanden,
    # gewijzigd, canonieke, bevestigt, zodra, totaal, kruis, altijd, elke,
    # keer, volledige, enige, worden, staan
    "geëvalueerd", "deze", "geabsorbeerd", "moeten", "rechtop", "schuin",
    "ter", "één", "regels", "bestanden", "gewijzigd", "canonieke",
    "bevestigt", "zodra", "totaal", "kruis", "altijd", "elke", "keer",
    "volledige", "enige", "worden", "staan",
    # tokens gevonden in chat-contaminatie (ronda 4): Italiaans (ovvero, già,
    # tutto, altre, finali, tutti, rimasto, toccato, misti, vuole, coerenza,
    # ortografia, grafia, manoscritto, proceda, assorbiti, indonesiani,
    # attuale, stessa, richiede, ecc)
    "ovvero", "già", "tutto", "altre", "finali", "tutti", "rimasto",
    "toccato", "misti", "vuole", "coerenza", "ortografia", "grafia",
    "manoscritto", "proceda", "assorbiti", "indonesiani", "attuale",
    "stessa", "richiede", "ecc",
    # tokens gevonden in chat-contaminatie (ronda 5): Nederlandse functie- en
    # bijwoorden die in chat-proza bocorden nadat er uit het boekregister werd
    # geciteerd (zorg, zitten, laten, struikelen, nergens, precies, overslaan,
    # vloeiend, stapelen, geankerd, leest, betekent, groter, groot, ankert,
    # wisselt, uitleg, verandert, denkt, voorstel, herschrijven, gereed, hoeft,
    # erna, leg, zit, aanloop, ervoor, blijft, identiek, ontbrekende, bruggen,
    # noot, toepassen, grootte, stap, langzaam, springt, beetje, groeit, haalt,
    # weg, barrière, heel, klein, hoeveel, vóór, héél, te, aan, legger)
    "zorg", "zitten", "laten", "struikelen", "nergens", "legger", "precies",
    "overslaan", "vloeiend", "stapelen", "geankerd", "leest", "betekent",
    "groter", "groot", "ankert", "wisselt", "uitleg", "verandert", "denkt",
    "voorstel", "herschrijven", "gereed", "hoeft", "erna", "leg", "zit",
    "aanloop", "ervoor", "blijft", "identiek", "ontbrekende", "bruggen",
    "noot", "toepassen", "grootte", "stap", "langzaam", "springt", "beetje",
    "groeit", "haalt", "weg", "barrière", "heel", "klein", "hoeveel",
    "vóór", "héél", "te", "aan",
    # tokens gevonden in chat-contaminatie (ronda 6): nog meer Nederlandse
    # woorden die in chat-drafts bocorden (lijst, uitgebreid, gecheckt,
    # hieronder, binnen, kort, doorlaten, telkens, achter, vanaf, tot, zelf,
    # liep, verder, stel, stelt, vind, vindt, weet, zeg, zei, leek)
    "lijst", "uitgebreid", "gecheckt", "hieronder", "binnen", "kort",
    "doorlaten", "telkens", "achter", "vanaf", "tot", "zelf", "liep",
    "verder", "stel", "stelt", "vind", "vindt", "weet", "zeg", "zei",
    "leek",
    # tokens gevonden in chat-contaminatie (ronda 7, incident 2026-09-28):
    # de hele chat-respons was Nederlands; deze woorden kwamen voor en
    # ontbraken in de eerdere rondes
    "voltooid", "uitgevoerd", "geslaagd", "heb", "ik", "alle", "bevat",
    "buiten", "fouten", "gevonden", "prosachecks", "nog", "woorden",
    "Italiaans", "Nederlandse", "contaminatie", "citatie",
}

# AGENTS.md section 2: chat-only banlist. These words ARE legitimately part of
# the book register (persis, perbanding, ...) so they must NOT be flagged when
# checking manuscripts — only when checking a chat draft via --chat.
CHAT_BANNED = {
    "rincian", "verdiwa", "persis", "selaraskan", "perbanding", "selengkapt",
    "teleportasi", "uitgave", "diketing", "maksed",
}

# Keep hyphenated compounds as single tokens so that legitimate domain terms
# like "over-forecast" or "under-forecast" are not split into "over" + "forecast".
TOKEN_RE = re.compile(r"[a-zà-ž]+(?:-[a-zà-ž]+)*")
CODE_FENCE = re.compile(r"^```")
INLINE_CODE = re.compile(r"`[^`]*`")


def scan_text(text: str, chat: bool = False) -> list[tuple[int, str]]:
    hits = []
    in_fence = False
    for lineno, raw in enumerate(text.splitlines(), start=1):
        if CODE_FENCE.match(raw.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = INLINE_CODE.sub("", raw)
        for word in TOKEN_RE.findall(line.lower()):
            if word in BANNED or (chat and word in CHAT_BANNED):
                hits.append((lineno, word))
    return hits


def scan_file(path: Path, chat: bool = False) -> list[tuple[int, str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    return scan_text(text, chat=chat)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file", help="scan one file instead of the whole book")
    ap.add_argument("--chat", action="store_true",
                    help="also enforce the AGENTS.md section 2 chat banlist")
    args = ap.parse_args()

    if args.file:
        paths = [Path(args.file)]
    else:
        paths = sorted((ROOT / "manuscripts").glob("*/master.md"))
        paths += sorted((ROOT / "front-matter").glob("*"))
        paths += sorted((ROOT / "back-matter").glob("*"))

    total = 0
    for p in paths:
        if not p.is_file():
            continue
        for lineno, word in scan_file(p, chat=args.chat):
            try:
                shown = p.relative_to(ROOT)
            except ValueError:
                shown = p
            print(f"{shown}:{lineno}: {word}")
            total += 1

    if total:
        print(
            f"\n{total} hit(s) found. Replace with register words "
            "(tanpa/dengan/hanya/untuk/satu/tidak, etc.).",
            file=sys.stderr,
        )
        return 1
    print("Clean: no Dutch/Italian-origin signal words found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())