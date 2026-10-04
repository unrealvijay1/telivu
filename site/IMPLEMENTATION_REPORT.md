# Telivu website implementation

Verified 2026-10-04. No commit, push, public deployment, application rebuild or installer
rebuild was performed. Existing unrelated working-tree changes were preserved.

1. **Technology:** semantic HTML, responsive CSS, lightweight vanilla JavaScript. Python
   3.10+ is used only for publication metadata/version generation and link validation.
   There is no runtime server requirement, framework or package installation.
2. **Structure:** `site/index.html`, `css/`, `js/`, `site-config.js`, `assets/brand/`,
   `assets/product/`, resource/legal directories and `scripts/`. Generated output is ignored
   `site/_build/`. README and this report are not published.
3. **Pages:** home plus Resources, Getting Started, Documentation, Example Models,
   Tutorials, Release Notes, Product Demo, Privacy Policy, License Terms, Support (11 total).
   Product/features/use cases/pricing/download are home anchors rather than duplicate pages.
4. **Responsive behavior:** desktop split hero, four pillar columns, three-column showcase,
   tablet two-column cards and stacked hero; mobile stacked sections and accessible toggled
   navigation. Without JavaScript, navigation remains visible and downloads stay safely disabled.
5. **Hero:** Telivu wordmark, exact tagline and product positioning, restrained green/off-white
   design, illustrative SVG probability curve with clearly labeled example values. It does
   not fabricate an Excel interface. Download state is truthful; Watch Demo reaches a placeholder.
6. **Product sections:** value strip, input/simulation/decision workflow, four pillars,
   actual UI showcase, five use cases, signature probability example, five audiences,
   local processing, pricing, version/download, resources, seven native-details FAQs and final CTA.
7. **Actual captures:** `results.webp` from `artifacts/results-tabs-preview/forecast.png`
   and `optimizer.webp` from `artifacts/optimizer-layout/results-1.png`. Both were visually
   inspected; synthetic values, no personal data, keys, local paths or machine IDs. Captions
   disclose development rendering and existing Monte Carlo application branding.
8. **Screenshots still required:** polished Excel workbook/ribbon/Results composition,
   Scenario Analysis, SPC and Correlations; preferably replace the harness Results/Optimizer
   captures with complete interactive captures. Three panels visibly say screenshots are coming soon.
9. **Local-processing verification:** `ExcelSimulationWorkbook.cs` accesses local Excel
   cells/recalculation through COM; `ScenarioExcelSandbox.cs` uses a local temporary workbook
   and owned Excel instance, rejects external connections/links for scenarios;
   `SpcAnalysisService.cs` reads local ranges and invokes `XmRCalculator`. Optimizer uses
   local evaluation and supports deterministic/Monte Carlo modes (`OptimizerForm.cs`, Core
   optimizer implementation). `LocalLicenseValidator.cs` verifies signed payloads against
   the embedded RSA public key; `TrialService.cs` maintains local DPAPI/Registry trial state.
   Source search found no HTTP/network client or external service URL in application/Core C#
   (the ribbon XML namespace is not a network request). Claim concerns this add-in's processing,
   not Excel's own external connections, cloud sync or host telemetry. No security certification
   or universal confidentiality guarantee is asserted.
10. **Version:** 0.2.1, authoritative `ProductVersion` in `Directory.Build.props`.
    Build substitutes public configuration and visible version text; no binaries are read.
11. **Download configuration:** centrally controlled by `downloadEnabled`, `downloadUrl`,
    `installerSize`, `releaseNotesUrl`; approved HTTPS links only. Domain, demo and contact
    also have configuration points. No invented contact or payment arrangement.
12. **Public download:** disabled. Located existing 0.2.0/0.2.1 Setup and manifests in `dist/`.
    Current 0.2.1 manifest reports NotSigned and pending clean-machine acceptance. Those
    files and their internal paths are not copied or linked. Installer size is hidden until approved.
13. **Pages workflow:** `.github/workflows/pages.yml`, relevant main pushes/manual
    dispatch, official Pages configuration/upload/deploy actions, website-only build job and
    scoped deploy permissions. No pre-existing workflows or website directory were found.
    Actual GitHub deployment remains untested because publishing was not requested.
14. **Local preview:** `python site/scripts/build.py`,
    `python -m http.server 8765 --bind 127.0.0.1 --directory site/_build`.
15. **SEO:** requested title/description, Open Graph and Twitter metadata, local share image,
    SVG favicon, robots.txt, conditional canonical/og:url, per-page WebPage JSON-LD and sitemap.
    CI supplies the configured Pages base URL. No public domain is assumed. Local builds
    without a site URL deliberately omit canonical/sitemap, rather than inventing a domain.
16. **Accessibility:** semantic landmarks/headings, skip link, alt text, chart title/description,
    visible focus, native disclosure controls, menu expansion state/Enter/Escape/focus return,
    reduced-motion CSS and readable palette. Browser keyboard checks passed. A formal
    Lighthouse/axe audit and screen-reader testing were not performed; no score is claimed.
17. **Performance:** system font stack, no third-party requests, deferred small JS, CSS-only
    responsive layout, dimensioned lazy-loaded WebP below fold. Two product WebPs total
    approximately 61 KB; all image/brand assets total approximately 85 KB. No speed benchmark claimed.
18. **Browser results:** headless Microsoft Edge through existing Playwright passed at
    1920×1080, 1440×900, 1366×768, 768×1024, 390×844 and 375×812 under both `/` and
    `/telivu/`. No horizontal scrolling or JS errors. Menu/FAQ keyboard activation, nested
    route navigation, enabled/disabled downloads, invalid file URL rejection, reduced motion,
    missing screenshot assets and no-JS navigation passed. Synthetic approved download
    URL was intercepted for testing; no installer was fetched. Screenshots/results remain
    under `artifacts/site-validation/` and are excluded from publication. Real-device Safari,
    Firefox and GitHub-hosted smoke checks remain unperformed.
19. **Links:** all 288 link/asset references across 11 configured production pages passed
    (277 in a local build without canonical links); anchors, image alt
    presence, absence of internal Windows paths and executable/XLL/key artifacts checked.
20. **Files:** all new website files under `site/`, new Pages workflow, and added website
    section in `PROJECT_CONTEXT.md`. Existing application/installer changes were not touched.
21. **Omitted commercial claims:** pricing, invented 14-day trial, no-credit-card promise,
    testimonials/logos/user counts, endorsements/certifications, benchmarks/ROI, macOS
    support, global optimization guarantees and unconditional validated x86 support.
22. **Launch inputs:** approved signed/release-validated installer and public HTTPS URL,
    domain/repository choice, public support destination, final screenshot set/demo,
    reviewed legal policies, finalized pricing/purchase arrangements and final brand mark if desired.
23. **Whitespace validation:** `git diff --check` passed. JavaScript syntax checks and
    build/link checks passed. Git emitted existing CRLF conversion notices only.

Manual GitHub publication and custom-domain steps are in `README.md`. Review the deployment
branch, repository name and account before pushing; the exact requested project URL requires
a repository named `telivu` under the chosen account. The task did not publish internal artifacts.
