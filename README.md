# Shift + website

A dedicated static marketing and help website for the Shift + Android app. No app release files were changed. Source is in `site/`: plain HTML, CSS and JavaScript, with no production dependencies, external fonts, analytics or build framework.

## Preview

From this directory:

```sh
python -m http.server 4173 --bind 127.0.0.1 --directory site
```

Open http://127.0.0.1:4173/. This address works only on the computer running the server. Stop with Ctrl+C. The delivered preview uses `noindex`; it is not a public deployment.

## Check

```sh
python scripts/check.py
python -m pip install -r requirements-test.txt
python -m playwright install chromium
python scripts/browser_test.py
```

The browser suite expects the preview server above. It checks all six pages at 1440, 768, 390 and 320 pixels; local image loads; horizontal overflow; mobile navigation; all walkthrough states; screenshot enlargement and Escape; FAQ matches and empty states; keyboard skip link; and no-JavaScript guide content. Screenshots and JSON results appear in `test-results/` (ignored by Git).

## Structure

- `site/index.html`: showcase, screenshot walkthrough and Standard/Premium comparison.
- `site/guide.html`: onboarding and feature usage.
- `site/home-assistant.html`: requirements, HACS pairing, sync semantics and troubleshooting.
- `site/support.html`: searchable FAQs and verified support contact.
- `site/privacy.html`: documented behaviour, clearly identified as an overview.
- `site/404.html`: recovery/help page.
- `CONTENT-SOURCES.md`: evidence and launch TODOs.
- `ASSET-PROVENANCE.json`: authentic screenshot origins and hashes.
- `DEPLOYMENT.md`: controlled public launch, Google Sites embed and domain choices.

Maintain brand text as **Shift +**. Do not recreate screenshots or introduce unsupported features or prices. Keep relative page/asset links so project-path hosting works. Update content alongside app changes and rerun checks.

## Current release state

Private repository: https://github.com/bgibbo/shift-plus-website

Public publishing, Pages activation, live Google Sites edits and DNS changes have deliberately not been performed. The manual Pages workflow is configured but requires authorization and repository Pages settings before it can deploy. A push only runs checks.
