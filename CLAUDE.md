# Huan Mao International website — maintenance guide

Staging site for Huan Mao International Company Limited (環貿國際有限公司), an OEM/ODM wood-panel
furniture factory in Hai Phong, Vietnam. Served by GitHub Pages from `main` (root).
Final domain (not live yet): huanmao.co. Owner: Channing (prefers Traditional Chinese).

## How the site is built
- Edit **only** `_src/template.html` (English master) and `_src/i18n.py` (en / zh-Hant / ja / vi table).
- Then run `python3 _src/build.py`. It writes `index.html`, `zh/`, `ja/`, `vi/`, `robots.txt`,
  `sitemap.xml`, `llms.txt`, and exits non-zero if any i18n string no longer matches the template
  or an image is missing. Never hand-edit the generated HTML files.
- Every English string you add or change in the template needs a matching row in `_src/i18n.py`
  with all three translations; remove rows whose English no longer exists.
- Photos live in `img/` (1600 px wide JPEG, quality ~75). Never add photos showing customer brands,
  logos, cartons or product labels (Lakeshore, Branch, etc.).
- `STAGING = True` in build.py adds noindex and blocks crawlers. Do not change it; the owner decides.

## Facts that must not be changed or invented
Established 2024 · ~100 employees · Taiwanese management · annual sales ~US$10M · ISO 9001 and
ISO 14001 · FSC board only via FSC-certified suppliers (no own FSC CoC) · formaldehyde certificates come from board suppliers, not our own · MOQ and lead time depend on the product · customer names are confidential
(customer names must NEVER appear on the site) · phone +84 369 686 820 ·
email sales@huanmao.co · tax code 0801449372. Never publish bank accounts.
Products (owner, 2026-11-26, from the exhibition catalogue): besides classroom/office storage, we sell electric standing desks,
standing desk with drawer, tilting whiteboard desks, mobile collaborative/training desks, modular whiteboard desks, sliding-door
cabinets, side tables and custom credenzas/benches. Their images are product renderings (labelled so). Never show the
catalogue company name, logo or TP-TZ model codes.
Do not invent capacities, MOQ, lead times, certifications, machine counts or customer names.
Red dashed `.note` boxes mark items waiting for the owner; leave them until he answers.

## Daily check-and-improve routine
1. `python3 _src/build.py` must pass.
2. Check: broken links/anchors, missing images or alt text, JSON-LD validity (parse it), hreflang/canonical,
   horizontal overflow at 390 px and 1280 px (Playwright + Chromium are preinstalled), light and dark theme,
   leftover English in zh/ja/vi pages, translation mistakes.
3. Fix any bug found. Then make **one** small, safe improvement (SEO/GEO wording, an extra FAQ that only
   uses the facts above, accessibility, performance such as image size, layout polish). Small diffs only;
   no redesigns, no new sections without facts from the owner.
   **Owner priority (2026-11-21): SEO/GEO first** — help buyers find us and help AI assistants recommend us.
   Choose the daily improvement from SEO/GEO whenever a safe one is left; read recent `CHANGELOG.md` entries
   first so work is not repeated. Ideas (only facts above or text already on the site): titles, meta
   descriptions, headings and alt text that use the words buyers search for (OEM/ODM furniture manufacturer
   Vietnam, RTA furniture, classroom storage, melamine particleboard, Hai Phong) and natural zh/ja/vi
   equivalents; clear, quotable answer sentences AI can cite; an extra FAQ whose visible text matches its
   FAQPage JSON-LD exactly; more precise JSON-LD for existing facts. No keyword stuffing, hidden text, fake
   reviews, customer names or unstated claims. In the report, list SEO/GEO steps only the owner can do
   (going live: domain + STAGING; Google Search Console / Bing Webmaster; Google Business Profile;
   LinkedIn or B2B directory pages to link via `sameAs`; updating the `llms.txt` text in build.py).
4. Rebuild, re-check, append a dated entry to `CHANGELOG.md` (Traditional Chinese, 1–3 lines), commit, push to `main`.
