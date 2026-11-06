# Design Squad — weboldal

A designsquad.space custom kódja. Az FEA Create marad a motor (formok, workflow-k, e-mailek, domain, SEO panel), a látvány innen jön.

## Hogyan működik

- `design/tokens.css` — színek, betűk, alapok
- `design/components.css` — építőelemek (portré, bordó kiemelés, számozott lista, lábléc…)
- `pages/` — oldalanként a tartalom
- `partials/footer.html` — közös lábléc
- `fonts/`, `images/` — betűk és képek
- `seo/seo.json` — SEO mezők oldalanként
- `tools/build.py` — ebből készül a `dist/` mappa

`dist/ds.css` a közös design-fájl. Minden FEA oldal erre hivatkozik a jsDelivr linkjén:
`https://cdn.jsdelivr.net/gh/dorkasusztak-star/designsquad-web@main/dist/ds.css`

`dist/fea/<oldal>.html` — ez másolható be az FEA Custom HTML elemébe.

## Térkép

| Fájl | FEA oldal | URL | Állapot | Utolsó módosítás |
|---|---|---|---|---|
| pages/links-page.html | Link In Bio Page – DesignSquad | /links-page | élesben (önálló kóddal), átállításra vár | 2026-11-06 |
| pages/home.html | Home | /home | tervezett | — |
| pages/about.html | About | /about | tervezett | — |
| pages/services.html | Services | /services | tervezett | — |
| pages/contact.html | Contact | /contact | tervezett | — |
| pages/legal/* | jogi oldalak | /privacy-policy-page, /terms-of-service, /cookie-policy, /refund-policy, /community-guidelines | tervezett | — |
| pages/funnels/* | opt-in + thank-you oldalak | /op-canvahacks-page, /waitlist/confident-creator-kit/op-page, /apply/custom-branding/opt-page, /newsletter/optin-page | tervezett | — |

## Szabályok

- Az élő URL-eket nem nevezzük át.
- Fájlnevek: kisbetű, ékezet nélkül, kötőjellel. Oldalfájl = URL vége.
- Képek: `ds-<oldal>-<mi>-<méret>.jpg`
- Minden CSS osztály `ds-` előtagú.
- Paletta: #d9bca3 · #d9c8bf · #f2f0f0 · #737272 · #404040 · #7a2e3b · #6b2737
- Betűk: Playfair Display (címek), Montserrat (szöveg)

## Módosítás menete

1. Változtatás a `design/` vagy `pages/` fájlokban
2. `python3 tools/build.py`
3. Előnézet: `dist/preview/`
4. Push → design-változás magától élesedik (jsDelivr cache ürítése: `https://purge.jsdelivr.net/gh/dorkasusztak-star/designsquad-web@main/dist/ds.css`)
5. Ha az oldal tartalma változott: `dist/fea/<oldal>.html` bemásolása az FEA-ba
6. Élő ellenőrzés + CHANGELOG
