"""Dependency-free internal link, image, metadata and publication-safety checks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys
root=Path(__file__).resolve().parents[1]/'site'
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__(); self.path=path; self.ids=set(); self.links=[]; self.meta={}; self.h1=0
  self.feed(path.read_text(encoding='utf-8'))
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:
   assert a['id'] not in self.ids, f'duplicate id {self.path}:{a["id"]}'
   self.ids.add(a['id'])
  if tag=='h1': self.h1+=1
  if tag=='meta': self.meta[a.get('name',a.get('property',''))]=a.get('content','')
  if tag=='img': assert 'alt' in a, f'{self.path}: image missing alt attribute'
  for key in ('href','src'):
   if a.get(key): self.links.append(a[key])
pages={p.name:Page(p) for p in root.glob('*.html')}
for name,page in pages.items():
 assert page.h1==1, f'{name}: expected one h1'
 for key in ('description','viewport','og:title','og:description','og:image'): assert page.meta.get(key),f'{name}: missing {key}'
 for link in page.links:
  u=urlsplit(link)
  if u.scheme or u.netloc: continue
  target=(page.path.parent/unquote(u.path)).resolve() if u.path else page.path
  assert target.exists(),f'{name}: broken {link}'
  if u.fragment and target.suffix=='.html': assert u.fragment in pages[target.name].ids,f'{name}: missing anchor {link}'
print(f'PASS: {len(pages)} pages; all internal assets, links, anchors, unique IDs and metadata checked')
