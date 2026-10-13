"""Run: python scripts/browser_test.py [base_url]. Requires playwright + Chromium."""
from pathlib import Path
import json,sys,time,urllib.request,urllib.error
from playwright.sync_api import sync_playwright
base=sys.argv[1] if len(sys.argv)>1 else 'http://127.0.0.1:4173/'
out=Path(__file__).resolve().parents[1]/'test-results';out.mkdir(exist_ok=True)
errors=[];checks=[]
for attempt in range(30):
 try:
  with urllib.request.urlopen(base, timeout=2) as response: assert response.status==200
  break
 except (urllib.error.URLError, OSError):
  if attempt==29: raise
  time.sleep(.2)
with sync_playwright() as p:
 browser=p.chromium.launch()
 page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.on('response',lambda r:errors.append(f'HTTP {r.status}: {r.url}') if r.status>=400 else None)
 for width in [1440,768,390,320]:
  page.set_viewport_size({'width':width,'height':900})
  for route in ['index.html','guide.html','home-assistant.html','support.html','privacy.html','404.html']:
   page.goto(base+route);page.wait_for_load_state('networkidle')
   assert page.locator('h1').count()==1
   assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),f'Overflow {width} {route}'
   assert page.locator('img').evaluate_all('(imgs)=>imgs.filter(i=>!i.closest("dialog")).every(i=>i.complete && i.naturalWidth>0)'),f'Image failure {route}'
   checks.append(f'{route} @ {width}px: render, images, no overflow')
  page.goto(base)
  if width in [1440,390]: page.screenshot(path=str(out/f'home-{width}.png'),full_page=True)
  if width<760:
   page.get_by_role('button',name='Menu').click();assert page.locator('#navigation').is_visible()
   page.keyboard.press('Escape');assert not page.locator('#navigation').is_visible()
   checks.append(f'Mobile navigation and Escape @ {width}px')
 page.set_viewport_size({'width':1440,'height':1000});page.goto(base)
 for name in ['alarms','alarm-centre','calendar']:
  page.locator(f'[data-tour="{name}"]').click()
  assert page.locator(f'[data-tour="{name}"]').get_attribute('aria-pressed')=='true'
  assert name+'.webp' in page.locator('.tour-visual img').get_attribute('src')
 page.locator('.tour-visual .screenshot').click();assert page.locator('dialog').is_visible()
 page.keyboard.press('Escape');assert not page.locator('dialog').is_visible()
 checks.append('All walkthrough states, image dialog and Escape')
 page.goto(base+'support.html');page.locator('#faq-search').fill('secure QR pairing');assert page.locator('.faq-list details:visible').count()==1
 page.locator('#faq-search').fill('zzzz-no-match');assert page.locator('#no-results').is_visible()
 page.locator('#faq-search').fill('');assert page.locator('.faq-list details:visible').count()==9
 page.locator('summary').first.click();assert page.locator('details').first.get_attribute('open') is not None
 checks.append('FAQ filtering, empty state, reset and native disclosure')
 page.goto(base+'guide.html#alarms');assert page.locator('#alarms').is_visible()
 page.set_viewport_size({'width':1440,'height':1000});page.screenshot(path=str(out/'guide-desktop.png'),full_page=True)
 page.goto(base);page.keyboard.press('Tab');assert page.locator('.skip').evaluate('(e)=>e===document.activeElement')
 page.keyboard.press('Enter');page.wait_for_function('document.activeElement.id === "main"')
 checks.append('Keyboard skip link')
 # No-JS baseline keeps content and links accessible.
 nojs=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':844})
 np=nojs.new_page();np.goto(base+'guide.html');assert np.locator('#alarms').count()==1
 checks.append('No-JavaScript guide content')
 browser.close()
assert not errors,errors
(out/'browser-results.json').write_text(json.dumps({'passed':len(checks),'checks':checks,'errors':errors},indent=2))
print(f'PASS: {len(checks)} browser checks; no JS errors or failed local requests')
