# Payslip Generator

One-page UK & Nigeria PAYE payslip generator. Fully client-side — nothing is uploaded or stored on a server.

**Video origin:** replica of a proven one-page-site idea from Greg Isenberg's
one-page-website video (RnzQ4QunFT4). Added value + validation: see the
portfolio repo [`/workspace/onepage-sites`](../onepage-sites) (validation reports).

## Files
- `index.html` — the whole app (single page)
- `privacy.html`, `ads.txt`, `robots.txt`, `sitemap.xml`, `track.js`

## Self-check
Open `index.html?demo=true` in a browser — runs the built-in assertions.

## Deploy (GitHub Pages)
Push this folder's contents to the repo root, enable Pages. Ads run via
AdSense **Auto ads** (loader tag in `<head>`, no manual `data-ad-slot` units).
Fix the canonical/sitemap slug if the repo name differs.
