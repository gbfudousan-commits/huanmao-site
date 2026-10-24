"""Build the Huan Mao website from _src/ into the repo root.

Run from anywhere:  python3 _src/build.py
- _src/template.html : English master page (edit content here)
- _src/i18n.py       : (en, zh-Hant, ja, vi) string table; every English string that
                       changes in template.html must be updated here too
- img/               : photos (shared by all languages)
Output: index.html, zh/index.html, ja/index.html, vi/index.html, robots.txt, sitemap.xml, llms.txt
"""
import os, sys, re

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
sys.path.insert(0, SRC)
from i18n import T, LANGS

# Staging: keep True until the site moves to huanmaofurniture.com and the owner approves going public.
STAGING = True
DOMAIN = 'https://huanmaofurniture.com/'
ORDER = [('en', 'EN'), ('zh', '中文'), ('ja', '日本語'), ('vi', 'Tiếng Việt')]

src = open(f'{SRC}/template.html', encoding='utf-8').read()
src = src.replace('{{MARK}}', open(f'{SRC}/mark-copper.b64').read()).replace('{{CUT}}', open(f'{SRC}/cut.svg.txt').read())

problems = []

def page(lang):
    t = src
    sub = lang != 'en'
    if sub:
        L = LANGS[lang]
        for row in sorted(T, key=lambda r: -len(r[0])):
            en, tr = row[0], row[L['idx']]
            if not tr:
                continue
            if en in t:
                t = t.replace(en, tr)
            elif lang == 'zh' and '&#x27;' not in en:
                problems.append('i18n string not found in template: ' + en[:80])
        t = t.replace('<title>Huan Mao International</title>', f'<title>{L["title"]}</title>')
        t = re.sub(r'family=Zilla\+Slab[^"&]*(&family=Work\+Sans[^"&]*)?', L['fonts'], t, count=1)
        t = t.replace('</style>', f':root{{--display:{L["display"]};--body:{L["body"]}}}\n</style>', 1)
        t = t.replace('src="img/', 'src="../img/')
    alt = [f'<link rel="alternate" hreflang="{"zh-Hant" if c == "zh" else c}" href="{DOMAIN}{"" if c == "en" else c + "/"}">' for c, _ in ORDER]
    alt.append(f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}">')
    alt.append(f'<link rel="canonical" href="{DOMAIN}{"" if lang == "en" else lang + "/"}">')
    t = t.replace('<link rel="preconnect"', '\n'.join(alt) + '\n<link rel="preconnect"', 1)
    links = []
    for c, name in ORDER:
        href = ('../' if sub else '') + ('index.html' if c == 'en' else f'{c}/index.html')
        cur = ' aria-current="true"' if c == lang else ''
        hl = 'zh-Hant' if c == 'zh' else c
        links.append(f'<a href="{href}" hreflang="{hl}" lang="{hl}"{cur}>{name}</a>')
    bar = '<div class="langbar"><div class="wrap"><nav aria-label="Language">' + ''.join(links) + '</nav></div></div>\n'
    t = t.replace('<header>', '<header>\n' + bar, 1)
    css = ('.langbar{border-bottom:1px solid var(--line);font:500 .78rem/1 var(--body)}'
           '.langbar nav{display:flex;justify-content:flex-end;gap:16px;padding-block:7px;flex-wrap:wrap}'
           '.langbar a{text-decoration:none;color:var(--muted)}.langbar a:hover{color:var(--ink)}'
           '.langbar a[aria-current]{color:var(--accent);font-weight:600}\n')
    t = t.replace('/* fact strip */', css + '/* fact strip */', 1)
    for m in re.findall(r'src="(?:\.\./)?(img/[^"]+)"', t):
        if not os.path.exists(f'{ROOT}/{m}'):
            problems.append(f'{lang}: missing image {m}')
    return t

def full(t, lang):
    hl = 'zh-Hant' if lang == 'zh' else lang
    head = '<meta name="robots" content="noindex, nofollow">\n' if STAGING else ''
    return (f'<!doctype html>\n<html lang="{hl}">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n' + head
            + t.replace('<header>', '</head>\n<body>\n<header>', 1) + '\n</body>\n</html>\n')

for c, _ in ORDER:
    path = f'{ROOT}/index.html' if c == 'en' else f'{ROOT}/{c}/index.html'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(full(page(c), c))

open(f'{ROOT}/robots.txt', 'w').write(
    ("User-agent: *\nDisallow: /\n" if STAGING else
     "User-agent: *\nAllow: /\nDisallow: /_src/\n\nUser-agent: GPTBot\nAllow: /\nUser-agent: OAI-SearchBot\nAllow: /\n"
     "User-agent: ClaudeBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\n"
     f"Sitemap: {DOMAIN}sitemap.xml\n"))
urls = ''.join(f'  <url><loc>{DOMAIN}{"" if c == "en" else c + "/"}</loc></url>\n' for c, _ in ORDER)
open(f'{ROOT}/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
open(f'{ROOT}/llms.txt', 'w', encoding='utf-8').write(
    "# Huan Mao International Company Limited (環貿國際有限公司)\n\n"
    "> ISO 9001 and ISO 14001 certified OEM/ODM manufacturer of melamine particleboard and MDF furniture in Hai Phong, Vietnam. "
    "Supplies U.S. furniture brands with classroom storage, office credenzas, consoles and ready-to-assemble (RTA) furniture.\n\n"
    "- Established: 2024, Taiwanese management, about 100 employees\n- Annual sales: about US$10 million\n"
    "- Factory: Quan Goi Quarter, Thuong Khuong Hamlet, Ke Sat Commune, Hai Phong City, Vietnam\n"
    "- Equipment: Nanxing computer panel saws with automatic loaders, Nanxing CNC nesting centres with automatic loading/unloading, "
    "Nanxing CNC point-to-point machining centre, Nanxing CNC boring, automatic and double-end edge banders, profile edge wrapping, "
    "glue spreader and 60-ton hydraulic cold press\n"
    "- Contact: sales@huanmaofurniture.com, +84 369 686 820\n\n"
    f"## Pages\n- [English]({DOMAIN})\n- [中文]({DOMAIN}zh/)\n- [日本語]({DOMAIN}ja/)\n- [Tiếng Việt]({DOMAIN}vi/)\n")

if problems:
    print('PROBLEMS:'); print('\n'.join('  ' + p for p in problems)); sys.exit(1)
print('built OK (staging=%s)' % STAGING)
