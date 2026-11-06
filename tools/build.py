#!/usr/bin/env python3
"""
Design Squad — build

Mit csinál:
  1. design/tokens.css + design/components.css  →  dist/ds.css  (a közös design-fájl)
  2. pages/**/*.html  →  dist/fea/<oldal>.html  (bemásolható blokk az FEA Custom HTML elembe)
                     →  dist/preview/<oldal>.html  (helyi előnézet)

Futtatás:  python3 tools/build.py
"""
import json, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
cfg = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))

CDN = f"https://cdn.jsdelivr.net/gh/{cfg['github_owner']}/{cfg['github_repo']}@{cfg['ref']}"
DIST = ROOT / "dist"
(DIST / "fea").mkdir(parents=True, exist_ok=True)
(DIST / "preview").mkdir(parents=True, exist_ok=True)

# 1. közös CSS
css = "\n\n".join((ROOT / "design" / f).read_text(encoding="utf-8") for f in ("tokens.css", "components.css"))
(DIST / "ds.css").write_text(css, encoding="utf-8")

# 2. oldalak
footer = (ROOT / "partials" / "footer.html").read_text(encoding="utf-8")
year = str(datetime.date.today().year)

def render(src: str, img_base: str) -> str:
    return (src.replace("{{footer}}", footer)
               .replace("{{year}}", year)
               .replace("{{img}}", img_base))

built = []
for page in sorted((ROOT / "pages").rglob("*.html")):
    name = page.relative_to(ROOT / "pages").as_posix().replace("/", "__")
    src = page.read_text(encoding="utf-8")

    fea = (f'<!-- Design Squad · {page.relative_to(ROOT).as_posix()} · build {datetime.date.today()} -->\n'
           f'<link rel="preload" href="{CDN}/fonts/playfair-display-400.woff2" as="font" type="font/woff2" crossorigin>\n'
           f'<link rel="preload" href="{CDN}/fonts/montserrat-400.woff2" as="font" type="font/woff2" crossorigin>\n'
           f'<link rel="stylesheet" href="{CDN}/dist/ds.css">\n'
           + render(src, f"{CDN}/images"))
    (DIST / "fea" / name).write_text(fea, encoding="utf-8")

    preview = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
               '<meta name="viewport" content="width=device-width, initial-scale=1">'
               f'<title>{name} — preview</title><link rel="stylesheet" href="../ds.css"></head><body style="margin:0">\n'
               + render(src, "../../images") + "\n</body></html>")
    (DIST / "preview" / name).write_text(preview, encoding="utf-8")
    built.append(name)

print("ds.css +", ", ".join(built))
