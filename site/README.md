# Telivu website

This repository contains the public Telivu marketing website: static HTML, CSS,
JavaScript and a small Python build. Installers are distributed as GitHub Release assets,
not committed to this repository. No backend, analytics or external font is required.

## Preview and validate

From the repository root, with Python 3.10+:

```powershell
python site/scripts/build.py --site-url https://unrealvijay1.github.io/telivu/
python site/scripts/check.py site/_build
python -m http.server 8765 --bind 127.0.0.1 --directory site/_build
```

Open http://127.0.0.1:8765/ and stop the server with Ctrl+C.
Generated files in `site/_build/` are ignored. The Pages workflow uploads this directory's
contents: `site/index.html` becomes the artifact root `index.html`. No `site/` URL suffix
is needed. Relative navigation and assets support root domains and GitHub project paths.

## Configuration

Edit `site/site-config.js`. `Directory.Build.props` supplies the product version at build time.

- `downloadEnabled`: keep false until an approved Release asset is published and verified.
- `downloadUrl`: the actual public HTTPS installer asset URL returned by GitHub.
- `installerSize`: measured size of that asset.
- `releaseNotesUrl`: public release page or local release-notes placeholder.
- `contactUrl`: approved HTTPS support page or public mailto address; empty shows coming soon.
- `demoUrl`: approved HTTPS demo video; empty opens the demo placeholder.
- `siteUrl`: optional full HTTPS site root. Empty uses GitHub's configured Pages URL in CI.
- `customDomain`: optional approved hostname. Configure the domain in repository Pages
  settings and DNS as well; CNAME alone does not configure Actions deployments.
- `analytics`: reserved, disabled. No tracker is loaded.

All five home-page download CTAs use this shared configuration, including the responsive
header. Download links fail closed on invalid URLs. Without JavaScript, the safe static
coming-soon state remains available.

## Content and assets

Edit `site/index.html`, `site/css/site.css`, `site/js/site.js`, and the resource/legal pages.
Optional `create-pages.py` regenerates secondary pages from the home header/footer and
its placeholder text; it overwrites those pages. Review legal pages before commercial launch.

Product captures under `site/assets/product/` show actual development interfaces with
synthetic demonstration data, with limitations identified in their captions. The hero
probability chart is illustrative and is not a product screenshot. Scenario Analysis,
SPC and Correlations capture placeholders and the demo video still need final assets.
Review replacement images for sensitive information, use WebP and preserve meaningful alt
text and dimensions. Below-fold product images are lazy-loaded.

## GitHub Pages

The workflow deploys on relevant pushes to **main** or manual dispatch. Set repository
Settings → Pages → Source to **GitHub Actions**. Only `site/_build` is uploaded. Internal
reports, release build files and executable assets must not be committed to this repository.

Optional browser checks use an existing Playwright installation and Chromium/Edge. Set
`PLAYWRIGHT_PATH` and optionally `BROWSER_PATH`, then run `node site/scripts/browser-check.mjs`.
Checks cover desktop/tablet/mobile widths, root/project paths, navigation and FAQ keyboard
interaction, reduced motion, download states and screenshot fallbacks. Results stay under
ignored `artifacts/`. Run `git diff --check` before commits.
