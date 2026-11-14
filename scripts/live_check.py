"""Read-only smoke check for an already published Shift + website."""
import sys
from playwright.sync_api import sync_playwright

base = sys.argv[1] if len(sys.argv) > 1 else "https://www.shiftplus.plus/"
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(base, wait_until="networkidle")
    assert page.locator("video").count() == 1
    page.wait_for_function("document.querySelector('video').readyState >= 1")
    assert page.evaluate("document.querySelector('video').duration") >= 60
    assert page.locator("track[kind='captions']").count() == 1
    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
    page.set_viewport_size({"width": 390, "height": 844})
    page.reload(wait_until="networkidle")
    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
    browser.close()
print("PASS: live video, captions, metadata and desktop/mobile layout")
