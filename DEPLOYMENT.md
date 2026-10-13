# Deployment and shiftplus.plus options

Nothing in this document has been applied to live hosting or DNS. Public launch needs explicit owner authorization. The new repository is private; Pages is not enabled. Pushing commits only runs validation.

## 1. Publish on GitHub Pages after approval

1. Resolve the privacy-policy and Play-listing checks in `CONTENT-SOURCES.md`.
2. In the repository's Settings → Pages, choose **GitHub Actions** as the build source. An eligible paid plan is needed for Pages from a private repository. A private repository does not by itself make a Pages website private. Do not change repository visibility without separate authorization.
3. Optionally protect the `github-pages` environment with required reviewers where supported.
4. In Actions, choose **Publish approved website → Run workflow**. Enter `PUBLISH` and the approved base URL, initially `https://bgibbo.github.io/shift-plus-website/`.
5. The workflow validates source, builds `dist/` with public canonical/Open Graph URLs, a sitemap and indexable robots metadata, then uploads and deploys the static files. It has no push trigger.
6. Verify the returned URL, every page, screenshot enlargement, mobile navigation, Google Play links and privacy link. Verify HTTPS and public metadata before sharing.

The default URL above is a planned address, not a currently deployed preview. The workflow does not configure DNS or create a custom domain. For a local production-build check:

```sh
python scripts/prepare_release.py https://bgibbo.github.io/shift-plus-website/
python -m http.server 4174 --bind 127.0.0.1 --directory dist
```

GitHub Pages serves static HTML/CSS/JS. See [GitHub Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

## 2. Embed the published site in Google Sites

Google Sites provides an iframe-style full-page URL embed; it does not import this repository as an editable Google Sites theme. GitHub Pages continues to host the actual website.

After public launch is approved and the hosted URL works:

1. Open the intended Google Site as an editor.
2. Choose **Pages → Add (+) → Full page embed**.
3. Enter the published Pages URL and insert it.
4. Preview desktop and mobile. Confirm navigation stays usable, external Play links open, screenshot dialogs work and the page scrolls properly.
5. Publish the Google Site only when authorized. A local `127.0.0.1` URL cannot be used for public embedding.

The site has relative internal links and does not set a frame-blocking header. Production headers and Google's embedding restrictions must still be checked. Avoid nesting an embedded URL that redirects back to the containing Google Site.

Official steps: [Google Sites full-page embeds](https://support.google.com/sites/answer/90569).

## 3. Choose ONE primary domain route

### A. shiftplus.plus redirects to a Google Site (matches the original plan)

Keep the website on Pages, embed it in Google Sites, then configure your domain provider's **HTTP URL forwarding** for `shiftplus.plus` (and `www` if desired) to the final published Google Sites URL. Use an ordinary unmasked 301 redirect for a permanent choice, with HTTPS support on the source domain. A DNS A/CNAME record alone cannot redirect to a URL path. The visitor's address bar will show the Google Sites destination. Registrar-specific forwarding fields depend on the current provider, which was not inspected.

### B. www.shiftplus.plus is the Google Site's custom address

As the Google Site owner, use **Settings → Custom domains → Start setup**, enter `www.shiftplus.plus`, verify ownership using the generated Search Console TXT record if requested, then follow the exact CNAME target shown by Google. Google Sites requires a subdomain such as `www`; redirect apex `shiftplus.plus` to `https://www.shiftplus.plus/` using HTTPS URL forwarding. Workspace-managed accounts may need their administrator. Share the published site publicly for the custom domain to work. Keep the embedded Pages URL separate and avoid redirect loops.

See [Google Sites custom domain instructions](https://support.google.com/sites/answer/9068867). DNS and certificate changes can take time; retain a rollback record of the previous configuration.

### C. shiftplus.plus directly serves GitHub Pages

This gives the bespoke website its own top-level URL. After authorization, verify domain ownership in GitHub first, then set the repository's Pages custom domain to `shiftplus.plus` **before** changing DNS. At the registrar, use an apex ALIAS/ANAME to `bgibbo.github.io` if supported, or GitHub's documented A records:

```text
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

For `www`, use CNAME `bgibbo.github.io` (no repository path). Keep existing mail/MX and unrelated TXT records intact. Check conflicting apex/AAAA records rather than blindly adding records. Wait for verification and certificate provisioning, then enable Enforce HTTPS. Build with base URL `https://shiftplus.plus/` and rerun the manual deployment. With Actions publishing, the Pages custom-domain setting controls the domain; a source CNAME file is not needed. Do not leave abandoned domain mappings in place.

Verify current values against [GitHub's custom-domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) before executing. Google Sites can still embed this URL, provided it does not redirect to that same Google Site.

## Rollback

Redeploy a previously approved commit using the manual workflow for a content rollback. Restore recorded DNS/forwarding settings for a domain rollback. To take a site offline, disable Pages in repository settings; do not assume making source private removes an already-public website.
