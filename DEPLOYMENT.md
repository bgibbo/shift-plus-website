# Shift + launch status — 14 October 2026

## Confirmed

- Website repository is public: https://github.com/bgibbo/shift-plus-website
- GitHub Pages uses GitHub Actions and custom domain `www.shiftplus.plus`.
- Deployment of commit `775996e` succeeded: https://github.com/bgibbo/shift-plus-website/actions/runs/38529766990
- The deployed homepage returned HTTP 200 when routed directly to a GitHub Pages server. This is an origin check, not a successful public DNS/HTTPS check.
- Google Play lists Shift + by GIBBO at https://play.google.com/store/apps/details?id=ie.shiftplus.app. Install availability was shown in the Ireland browser context and varies by device/region.
- The website now links to the published app privacy policy from that listing: https://sites.google.com/view/dunmore-east-holiday-rental/privacy-policy (effective 27 July 2026). Its identity and accessibility were verified; legal completeness was not certified. It does not explicitly discuss newer Home Assistant/calendar-sync features.
- No Spaceship, email, or Google Sites changes were made. The owner will edit DNS personally.

## DNS records to add in Spaceship

Open https://www.spaceship.com/application/advanced-dns-application/ and select `shiftplus.plus`, then **DNS records → Custom records**. Add the following records individually. Use TTL **3600 seconds** (or the normal default).

| Type | Name / Host | Value |
|---|---|---|
| CNAME | www | bgibbo.github.io |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

Do not include `https://` or a repository path in the CNAME value. Do not create a CNAME at `@`. No URL-forwarding service or nameserver change is needed. GitHub Pages will redirect the apex `shiftplus.plus` to `www.shiftplus.plus` after DNS is working.

Preserve all existing MX, TXT, DKIM, DMARC and other mail records, plus the current `launch1.spaceship.net` and `launch2.spaceship.net` nameservers. Observed mail records include `mx1.spacemail.com`, `mx2.spacemail.com`, and SPF `v=spf1 include:spf.spacemail.com ~all`. This is not a complete zone backup: DKIM selector records cannot be exhaustively discovered through public DNS.

No apex A/AAAA or www CNAME was returned during the initial DNS check. If the dashboard shows existing web records or forwarding, review them before adding conflicting records; do not delete mail or service connections.

Official guidance: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site and https://www.spaceship.com/knowledgebase/dns-records-types/

## Remaining verification

After the owner saves DNS, check public resolution for both hostnames, wait for GitHub's certificate, enable **Enforce HTTPS**, and verify HTTPS page loading, assets, navigation, privacy/Play links and apex redirection. DNS and certificate provisioning can take up to 24 hours. The custom-domain website is not yet verified live.

