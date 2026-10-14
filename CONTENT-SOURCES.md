# Content and asset evidence

Reviewed 13 October 2026. Local repositories were read only; their HEADs matched the remote HEADs at review time.

## App: bgibbo/shiftplus

Commit `56afefa7bdcd0d6cd537e3e48f109505985518ee` (release 6.0.0 build 77).

| Website material | Source within app repository |
| --- | --- |
| Roster, unit, active-versus-viewed distinction, alarms, annual leave, calendar sync and usage instructions | `lib/screens/help_centre_screen.dart` |
| Premium feature list and gating | `lib/screens/home_screen.dart` (`_showPremiumUpgrade`, feature entry guards), `lib/screens/help_centre_screen.dart` |
| Purchase flow through Google Play; no price asserted | `lib/services/premium_access_service.dart` |
| Home Assistant pairing and Premium requirement | `lib/screens/home_assistant_sync_screen.dart` |
| Support address `hello@shiftplus.plus` | `lib/services/feedback_launcher.dart` |
| Privacy overview | `lib/screens/help_centre_screen.dart`, About Shift + topic |
| Brand blue `#005EB8`, ink `#07111F`, pale surface `#F4F7FB` | `lib/theme/app_theme.dart` |
| Authentic master plus symbol and app icon | `assets/branding/shift_plus_logo_master.svg`, `shift_plus_icon.png` |

Original raster icon is copied unchanged; favicon and touch icon are resized derivatives. The web directory's existing favicon was not assumed to be approved branding: the new favicons derive from the actual branded app icon. Master SVG is copied unchanged. Existing source files were not modified.

## Integration: bgibbo/shift-plus-home-assistant

Commit `08690849ebb19a59c24b539be4c8fe0f74c2b833`, default branch `main`.

`README.md` verifies HA 2024.7+, HACS, Premium, custom repository setup, five-minute single-use QR, Android-initiated sync, local minute-by-minute recalculation, troubleshooting and issue tracker. `docs/security.md`, `docs/entities.md` and `docs/dashboard.md` are linked for further detail. The website does not claim household controls or prebuilt automation routines.

## Genuine captures

`E:\Projects\ShiftPlus\Marketing\Instagram-Reel-Work-Alarms-v1\README.txt` records capture from the real Android release package at version 6.0.0 build 77. Three full-frame captures are reused with WebP compression only; no screen contents are altered. The calendar is a frame from the genuine recording, not a fabricated mockup. Screenshot provenance and SHA-256 hashes are in `ASSET-PROVENANCE.json`. No live pairing QR, personal notes, access tokens or credentials are included. Captured roster examples are retained exactly as in existing marketing materials.

## Launch verification — 14 October 2026

- The official Google Play listing opened successfully in the Ireland browser context as Shift + by GIBBO, with an install control and device availability. Availability remains device/region dependent.
- Its App support section links to https://sites.google.com/view/dunmore-east-holiday-rental/privacy-policy. The page explicitly identifies Shift Plus and an effective date of 27 July 2026. A direct link is now present on the website privacy page. This verifies the published policy source, not legal completeness or coverage of newer features. The policy does not explicitly describe Home Assistant or calendar sync; the website retains its sourced feature overview.
- The owner authorized public website launch, repository visibility if needed, GitHub Pages, and www.shiftplus.plus on 14 October 2026. The owner will make DNS changes personally.

## Historical pre-launch notes (13 October 2026)

1. **Complete app privacy policy:** no complete developer-approved policy was found in the inspected app/marketing materials. The site clearly provides a documented-behaviour overview. Obtain/verify the authoritative Play policy link and add it before public launch; do not invent legal retention or deletion promises.
2. **Play availability:** the supplied Google Play URL is used exactly. The listing could not be retrieved through web tooling; public install eligibility, store wording and price were not independently verified. No price or universal availability claim is made.
3. **Publication authorization:** required before running the manual Pages deployment, changing repository visibility or editing DNS/Google Sites. Private repo storage and local preview are complete.
4. **Host plan:** Pages from a private repository requires an eligible GitHub plan. Keep the repository private unless public source release is separately approved.
5. **Production URL:** select the final hosting/domain route before building public metadata. `prepare_release.py` creates absolute canonical/OG URLs, sitemap and indexable robots metadata; source preview remains noindex.
6. **Actual Google Sites integration:** final embedding must be checked on the chosen published Google Site after authorization. Local browser tests do not establish production iframe behaviour.
7. **Device coverage:** browser QA uses Chromium at desktop/tablet/mobile widths, not a physical Android/iOS device lab.

No testimonials, invented user counts, prices, fabricated UI captures or unimplemented future features are included. The connection diagram is explicitly labelled as an overview.
