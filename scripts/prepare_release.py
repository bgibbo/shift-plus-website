"""Build a public-ready copy only after a real production URL has been selected.
Does not publish anything. Example: python scripts/prepare_release.py https://bgibbo.github.io/shift-plus-website/
"""
from pathlib import Path
import shutil,sys,re
from urllib.parse import urlsplit
from html import escape
base=sys.argv[1].rstrip('/')+'/' if len(sys.argv)>1 else ''
u=urlsplit(base)
if u.scheme!='https' or not u.netloc or u.query or u.fragment: raise SystemExit('Supply the approved HTTPS production base URL.')
root=Path(__file__).resolve().parents[1]; out=root/'dist'
out.mkdir(exist_ok=True); shutil.copytree(root/'site',out,dirs_exist_ok=True)
urls=[]
for p in out.glob('*.html'):
 text=p.read_text(encoding='utf-8'); url=base+(p.name if p.name!='index.html' else '')
 text=text.replace('<meta name="robots" content="noindex,nofollow">','<meta name="robots" content="index,follow">' if p.name!='404.html' else '<meta name="robots" content="noindex">')
 text=text.replace('content="assets/app-icon.png"','content="'+escape(base+'assets/app-icon.png',quote=True)+'"')
 text=text.replace('</head>',f'<link rel="canonical" href="{escape(url,quote=True)}"><meta property="og:url" content="{escape(url,quote=True)}"></head>')
 p.write_text(text,encoding='utf-8')
 if p.name!='404.html': urls.append(url)
(out/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'sitemap.xml\n')
(out/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+escape(x)+'</loc></url>' for x in urls)+'</urlset>')
print('Prepared dist/ for '+base+'; nothing was deployed.')
