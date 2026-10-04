"""Regenerate secondary placeholder pages using the shared home header/footer."""
from pathlib import Path
import re
site = Path(__file__).resolve().parents[1]
home = (site / 'index.html').read_text(encoding='utf-8')
head = home.split('<body>')[0]
header = home.split('<body>')[1].split('<main')[0]
footer = '<footer' + home.split('<footer', 1)[1]
resources = [('getting-started','Getting Started'),('documentation','Documentation'),('example-models','Example Models'),('tutorials','Tutorials'),('release-notes','Release Notes')]
pages = {
 'resources': ('Resources', '<p class="lead">Practical guidance for decision analysis in Excel.</p><div class="resource-links">'+''.join(f'<a href="resources/{slug}/">{name}<span>↗</span></a>' for slug,name in resources)+'</div><p>Learning materials are being prepared for launch.</p>'),
 'resources/demo': ('Product Demo','<p class="lead">Demo video coming soon.</p><p>A guided demonstration is being prepared. Explore the actual development captures and product features on the home page.</p><a class="button secondary" href="index.html#showcase">Explore the product</a>'),
 'privacy': ('Privacy Policy','<p class="notice">Pre-launch placeholder · policy requires legal review before commercial launch.</p><h2>Local product processing</h2><p>The current Excel add-in performs simulation, scenario analysis, optimization and process-control calculations locally. Workbook/model data is not sent to an external analytics platform. Trial state and paid-license verification also operate locally.</p><h2>This website</h2><p>This website contains no application analytics, advertising trackers, forms or accounts. Hosting-provider infrastructure may process request information. A complete privacy policy covering final hosting and commercial arrangements is being prepared.</p><p>This factual pre-launch summary is not the final privacy policy.</p>'),
 'license': ('License Terms','<p class="notice">Pre-launch placeholder · terms require legal review before commercial launch.</p><p>Commercial license terms are being prepared. This page does not grant a license or establish purchase terms.</p><p>The current product implements a 30-day evaluation and locally validated signed paid licenses. Final commercial pricing and purchase arrangements will be published when approved.</p>'),
 'support': ('Support & Contact','<p class="lead contact-status">Contact information coming soon.</p><p>Public support details will be provided before launch.</p><a class="button secondary" data-contact href="resources/">Explore resources</a>')
}
for slug,title in resources:
 body = '<p class="lead">Coming soon.</p><p>We’re preparing this resource for public launch. No downloads or documentation are available here yet.</p>'
 if slug == 'release-notes': body = '<p class="lead">Version <span data-version>0.2.1</span></p><p>Public release notes are being prepared. This version is not yet approved for public download.</p>'
 pages['resources/'+slug] = (title,body)
for slug,(title,body) in pages.items():
 text = head.replace('<title>Telivu — Decision Analysis for Excel</title>', f'<title>{title} — Telivu</title>')+'<body>'+header+f'<main id="main" class="wrap document"><p class="eyebrow">TELIVU</p><h1>{title}</h1>{body}<p class="back"><a href="index.html">← Back to Telivu</a></p></main>'+footer
 prefix = '../'*len(Path(slug).parts)
 text = re.sub(r'(href|src)="(?!https?:|mailto:|#)([^"]+)"', lambda m: f'{m[1]}="{prefix}{m[2]}"', text)
 path = site/slug/'index.html'; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(text,encoding='utf-8')
