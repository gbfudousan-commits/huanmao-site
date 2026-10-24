# Huan Mao International website — maintenance guide

Staging site for Huan Mao International Company Limited (環貿國際有限公司), an OEM/ODM wood-panel
furniture factory in Hai Phong, Vietnam. Served by GitHub Pages from `main` (root).
Final domain (not live yet): huanmaofurniture.com. Owner: Channing (prefers Traditional Chinese).

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
email sales@huanmaofurniture.com · tax code 0801449372. Never publish bank accounts.
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
4. Rebuild, re-check, append a dated entry to `CHANGELOG.md` (Traditional Chinese, 1–3 lines), commit, push to `main`.
