# Telivu website

Plain semantic HTML, CSS, small JavaScript and a dependency-free Python publishing build.
The website is isolated from the Excel add-in. No application or installer build is needed.
No backend, framework, external font request, account, analytics or tracker is used.

## Preview

From the repository root, with Python 3.10+:

```powershell
python site/scripts/build.py
python site/scripts/check.py site/_build
python -m http.server 8765 --bind 127.0.0.1 --directory site/_build
```

Open http://127.0.0.1:8765/. Stop with Ctrl+C. To check project-path SEO generation:
`python site/scripts/build.py --site-url https://YOUR-USERNAME.github.io/telivu/`.
The source can also be served directly using `--directory site`, but generated SEO and
the authoritative product version are applied only in the build. Never publish the repository root.

## Edit content and configuration

- Edit home content in `index.html`, styles in `css/site.css`, behavior in `js/site.js`.
- Edit secondary pages directly, or update `scripts/create-pages.py` and run it to
  regenerate them from the shared home header/footer. Regeneration overwrites those pages.
- `site-config.js` owns download, contact, demo, release notes and domain settings.
- `Directory.Build.props` is the authoritative product version. The build reads only
  `ProductVersion` and refreshes the public config and visible version text. Do not change
  application version just to update website copy. Source config version is a preview fallback.
- `downloadEnabled` is **false**. Disabled buttons point to the download status section.
  They never link to local artifacts. After release approval, insert a public HTTPS URL,
  set `installerSize` to the approved release size, and set `downloadEnabled: true`.
  JavaScript rejects non-HTTPS/credentialed URLs. Without JS, the safe pre-launch state stays visible.
- `releaseNotesUrl` may be a public HTTPS URL; otherwise the local placeholder is used.
- `demoUrl` is an optional public HTTPS video. Until provided, Watch Demo opens a truthful placeholder.
- `contactUrl` accepts a public HTTPS support URL or an explicitly approved public `mailto:` address.
  Empty contact settings show “Contact information coming soon.” No address was inferred.
- `siteUrl` remains empty until a domain is selected. CI uses the URL returned by GitHub's
  configure-pages action. An explicit `siteUrl` overrides CI; include any project path.
- `analytics: null` is a reserved configuration point only. Implement and review any
  future integration separately. The site works entirely without analytics.

## Pages and assets

Home contains Product, Features, Use Cases, Pricing, Download, Resources and FAQ anchors.
Secondary routes: Resources, Getting Started, Documentation, Example Models, Tutorials,
Release Notes, Product Demo, Privacy Policy, License Terms, Support.

The temporary wordmark/icon lives in `assets/brand/mark.svg`. Replace it and update header,
footer and favicon references when final branding is supplied. `social.png` is the share image.
No CNAME or domain is hardcoded in source. Legal pages are explicitly pre-launch placeholders.

Two inspected synthetic development captures were converted to lightweight WebP:

| Published asset | Source capture | Limit |
| --- | --- | --- |
| `assets/product/results.webp` | `artifacts/results-tabs-preview/forecast.png` | Actual Results; native selector/input text is blank in harness rendering |
| `assets/product/optimizer.webp` | `artifacts/optimizer-layout/results-1.png` | Actual Optimizer; synthetic fixture, no optimality guarantee |

They contain no personal/company data, local paths, keys, machine IDs or debug logs.
Neither pretends to be a finished Telivu-branded production capture. The hero graphic and
cost values are labeled illustrative, not application UI. Supply a polished Excel workbook
with ribbon and Results visible, plus captures for Scenario Analysis, SPC and Correlations.
The latter panels explicitly show screenshot placeholders. Inspect every replacement for
sensitive content; keep dimensions and useful alt text. Use WebP, a width around 1100px for
the large shot and smaller images for cards. Keep below-fold images lazy-loaded. Existing
application assets were neither moved nor modified.

## Publishing manually in GitHub

No commit, push or deployment has been performed by this task.

1. Choose a repository named `telivu` under the intended account for the exact
   `https://<username>.github.io/telivu/` address. Keep application source private if desired;
   do not change repository visibility merely for hosting. Pages availability depends on plan.
   For a separate website repository, preserve `site/`, the Pages workflow, and a sanitized
   version-only `Directory.Build.props` so the build has its version source.
2. Review and commit the website, workflow and context changes locally, then push them yourself.
   The workflow currently targets **main**, the website publishing branch. Change its
   `push.branches` if the publishing repository uses another branch such as main.
3. In that GitHub repository, open **Settings → Pages**. Under **Build and deployment**,
   set **Source → GitHub Actions**.
4. In **Settings → Actions → General**, allow the official actions used in `pages.yml`.
   If environment rules restrict branches, allow the publishing branch in **Settings →
   Environments → github-pages**. The deploy job declares Pages-write and OIDC permissions.
5. Open **Actions → Deploy Telivu website → Run workflow**, select the publishing branch,
   and run it. Later pushes affecting site files, version props or workflow redeploy automatically.
6. Wait for both build and deploy to succeed. Open the deployment URL from the workflow or
   Settings → Pages, and check navigation, resources, privacy and the disabled download state.

Only `site/_build` is uploaded. The builder explicitly includes HTML, assets, CSS, JS,
public config, robots, sitemap and optional CNAME. It does not read or copy dist installers,
release manifests, XLLs, license generators, keys, scripts, test reports or this README.

GitHub workflow guidance: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Future custom domain

Set `customDomain` to the approved hostname and `siteUrl` to its HTTPS root, rebuild and push.
The build emits CNAME for portability. For Actions deployments, GitHub's repository Pages
**Custom domain** setting controls the domain; CNAME is not sufficient. Add the domain in
Settings → Pages, configure DNS according to GitHub's documentation, then enable HTTPS
when available. All asset/navigation paths work at both root and project locations.

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## Checks

`scripts/check.py` checks every internal link/anchor, image alt presence and artifact boundaries.
`node --check site/js/site.js` checks JavaScript syntax. Optional browser checks require an
existing Playwright installation and Chromium/Edge; no browser installation is part of the build.
Set `PLAYWRIGHT_PATH` to its package directory and optionally `BROWSER_PATH` to the browser
executable, then run `node site/scripts/browser-check.mjs`. It tests root/project paths at
1920×1080, 1440×900, 1366×768, 768×1024, 390×844 and 375×812, menu Enter/Escape,
FAQ keyboard interaction, reduced motion, downloads enabled/disabled, unsafe URLs,
missing images and no-JS navigation. Output stays in `artifacts/site-validation/`, never published.

See `IMPLEMENTATION_REPORT.md` for source verification, results and launch requirements.

## Website-only repository export

Run `python site/scripts/prepare-publication.py` in the application repository to prepare
`artifacts/telivu-publish/`. The export includes all website source files except generated
output/cache, `.github/workflows/pages.yml`, a version-only `Directory.Build.props` and a
website repository `.gitignore`. It excludes the application, installers, release binaries,
root project handoff and existing Git history. The script refuses to overwrite an initialized
export repository. Initialize Git inside this folder on `main`, then commit and push only
that new repository. Do not change the application repository's remote.

`site/_build/index.html` is the uploaded artifact's root `index.html`; there is no extra
`site/` wrapper inside the Pages artifact. GitHub's `/telivu/` URL prefix is the repository
path, not a `site/` directory in the deployment.
