# Shift + wording review — 15 October 2026

Terms version: `2026-10-15.v2`. Local review only; no release, push or publication.

## Message and presentation

The acknowledgement uses the owner's approved title, three paragraphs and checkbox wording verbatim. It describes reliable work reminders, correct device configuration, monitoring reminders and accurate duty-time recording. It does not recast Work Alarms as wake-up alarms or ask users to maintain backup alarms.

The app and website use matching Terms of Use. Eight short sections cover purpose, schedule responsibility, Work Alarms, updates, purchases, responsible use, a proportionate liability provision, and privacy/contact. Mandatory consumer rights are preserved wherever the user lives; there is no country-specific statutory list or universal Irish-law assumption.

Privacy Information explains local data, optional transfers, local acknowledgement, permissions, Google Play/Home Assistant, support, deletion and applicable rights. The website adds its own hosting information. The app's legal screens now separate section headings and paragraphs. Settings uses “Terms & Privacy” with an information icon. About links and onboarding entry points still reach the same documents and acknowledgement.

## Mechanism retained

- The checkbox starts unticked and Accept & continue remains disabled until selected.
- Reading Terms or selecting Not now does not record acceptance.
- Acceptance stores only the version and UTC timestamp in local preferences. No new collection or transmission is introduced.
- Current acceptance skips the prompt. The v1 record requires review of v2 through the existing version check.
- Existing enabled alarms use the existing hold-and-review flow for changed terms; scheduling and permission handling are unchanged.
- Settings-only reset retains acknowledgement; full app-data reset clears it. Device backups can restore data after reinstall, which the privacy text now acknowledges.

## Scope

This is a wording and presentation update, not a change to alarm delivery, purchases, sync or data handling. Existing development artifacts and unrelated files are preserved. The original 14 October review is retained in Git history.

## Reference check

Official consumer guidance informed the short rights-preserving provision without importing its legislative detail into the user experience:

- https://europa.eu/youreurope/citizens/consumers/unfair-treatment/unfair-contract-terms/
- https://www.ccpc.ie/information-for-businesses/selling-goods-and-services/selling-digital-content-or-services/

## Verification

Focused app tests cover unticked consent, accept/decline, UTC/version persistence, old-version review, current-version reuse and reading Terms on a compact screen with enlarged text. Website checks cover seven pages, internal legal/footer links and responsive behaviour. Actual Flutter widgets were rendered in a local debug browser preview for screenshot inspection; this is not a new Android/Play release or a physical-device delivery test.
