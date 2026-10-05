# Telivu

**Open-Source Decision Intelligence for Excel**

**Free. Open Source. No Subscriptions.**

Telivu’s direction is one decision intelligence toolkit for individuals and organizations, supported through voluntary donations and sponsorship, with no paid feature tiers or separate editions.

Explore Monte Carlo simulation, scenario analysis, sensitivity, optimization and XmR statistical process control directly in desktop Excel on Windows.

[Official website](https://unrealvijay1.github.io/telivu/) · [Download through the official website](https://unrealvijay1.github.io/telivu/#download) · [Existing release notes](https://github.com/unrealvijay1/telivu/releases/tag/v0.2.1)

## Current distribution status

The existing unsigned 0.2.1 installer still has a 30-day trial and offline activation. Removing those restrictions is a separate application change. No open-source application license has been selected. The public repository currently contains website source and installer releases, rather than application source. The stated product direction does not grant application redistribution or commercial-use rights.

Donation provider setup required. No donations are collected by this website.

## Website development

Static HTML/CSS/JavaScript; no backend, analytics, external fonts or framework dependencies.

```powershell
python site/scripts/build.py --site-url https://unrealvijay1.github.io/telivu/
python site/scripts/check.py site/_build
```

The existing Pages workflow builds `site/_build` and deploys on main. All download buttons use the existing `[data-download]` handler in `site/js/site.js`, with the verified HTTPS asset from `site/site-config.js`. Preserve this release URL, asset name and shared resolution logic. No new releases or installer changes are needed for website updates.

Product images are real development captures with synthetic data. Guides describe implemented capabilities and analytical limitations. Report issues with synthetic examples and avoid confidential workbooks.
