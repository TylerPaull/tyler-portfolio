# Tyler Paul Lipman — design portfolio

A portfolio of furniture, lighting, materials, and spatial design by Tyler Paul Lipman, a Tulane University design student. Built with AI assistance for the September 29, 2026 portfolio assignment, with continued improvements in this same repository through October 8.

**Live site:** [tylerpauldesg.com](https://tylerpauldesg.com/)

**Public repository:** [TylerPaull/tyler-portfolio](https://github.com/TylerPaull/tyler-portfolio)

Initial publication verified September 28, 2026 (America/Chicago). The September 29 editorial redesign is documented below; its final visual checks and publication verification are recorded separately in [the audit](docs/assignment-audit.md).

## The site

- Selected-work homepage with BARE, Ostra, Nucite, Butterfly Streetcar Pavilion, and Balance.
- A professional-experience overview for The Laurel Group links to five process case studies: Poolside Terrace, Layered Arrival, Garden dining, Pergola terrace, and Entry materials. They connect site references, supplied plans, proposal analysis, annotated studies, and visualizations, with Tyler’s confirmed Creative Design Intern title and clear team credits. Home and About link to the overview.
- Five studio case studies use a clean opening image followed by numbered sections that explain the idea, development, and outcome or current direction.
- Butterfly Streetcar Pavilion uses six standalone drawings extracted from an original vector PDF, followed by atmosphere renderings. Full presentation boards are removed. The original studio board establishes the corrected date, Spring 2026.
- Ostra pairs individual object photographs with extracted geometry, cardboard-prototype, and assembly studies, making the design sequence readable without full presentation sheets.
- A bench/chair comparison for BARE that works with pointer, touch, and keyboard. Without JavaScript, both photographs remain visible. A supplied rotation animation autoplays muted and loops continuously, with controls available to pause it. A CNC cut plan and exploded assembly drawing add construction detail; both drawings open at full resolution.
- About page with a real portrait, verified background, internship experience, tools, and email contact.
- Mobile layouts, meaningful headings, skip navigation, visible keyboard focus, reduced-motion support, and responsive WebP images.

Balance is labeled **in progress**. The pavilion is presented as a design proposal. The site does not claim that these concepts have been built or tested.

## Preview locally

No package installation or build step is required. With Python 3 installed, run this from the repository:

```sh
python3 -m http.server 4173 --directory dist
```

Open `http://localhost:4173/`. Refresh after editing.

## Edit and check

The `dist/` folder contains the complete website. Edit its HTML files for copy and page structure, `styles.css` for layout, and `site.js` for the BARE comparison. Add optimized assets to `dist/assets/`; keep `src`, `srcset`, `sizes`, dimensions, and alternative text consistent.

```sh
python3 scripts/check_site.py
```

The check verifies all local links, image variants, fragment targets, descriptive metadata, a single main heading per page, and image alternatives/dimensions. Browser testing is also necessary. See [the audit](docs/assignment-audit.md).

## GitHub Pages publication

`main` preserves the full source and documentation. `gh-pages` contains only the files from `dist/`, with history derived from the same commits. In **Settings → Pages**, choose **Deploy from a branch → gh-pages → /(root)**. The `.nojekyll` file allows the static files to publish directly.

After reviewing and committing changes:

```sh
./scripts/publish.sh
```

This checks the site, pushes `main`, and publishes `dist/` to `gh-pages`. It requires Git, its standard subtree command, and authenticated access to this repository. No force push is used. GitHub runs its Pages deployment after the branch updates; wait for success and check the public site.

The custom domain is `tylerpauldesg.com`, preserved in `dist/CNAME`. Keep that file when publishing. The recovery links in `dist/404.html` and the `BASE` in `scripts/check_site.py` use `/` for the custom domain. Normal pages use relative links. If domain settings are edited on GitHub and create a commit on `gh-pages`, incorporate that change into `dist/` before publishing; do not force-push over it.

## How the files work

HTML supplies content and structure. CSS controls the editorial layout and adapts it to smaller screens. JavaScript switches between the two BARE photographs. Git records meaningful changes; GitHub stores the repository; GitHub Pages serves the files as the public website.

## Content, credits, and AI use

Project descriptions and imagery were gathered from [Tyler's existing portfolio](https://www.tylerpauldesg.com/) and original project files supplied by Tyler, reviewed, and reorganized into concise case studies. The visual design was developed separately from the original Framer template. See [content sources](docs/content-sources.md) and [the image manifest](docs/asset-manifest.json). The [pavilion drawing record](docs/pavilion-drawing-sources.json) and [Ostra image record](docs/ostra-image-sources.json) preserve source filenames, page or crop coordinates, and extraction methods.

Codex assisted with planning, source review, editorial rewriting, HTML/CSS/JavaScript, image optimization, accessibility checks, repository preparation, and publication. A second AI review checked claims and source-level accessibility. Nucite uses the corrected Studio III OSM booklet for its project name, process, sample quantities, and imagery. The pavilion drawings and Ostra studies were extracted from Tyler's original files without redrawing their geometry. The full-size BARE chair and Ostra opening photographs received AI background removal; original photographs remain in their case studies. See [image sources and edit prompts](docs/visual-source-notes.md). The current headshot was supplied directly by Tyler; its transparency is preserved. AI-generated commits are attributed to `Codex <codex@localhost>` rather than falsely attributed to Tyler.

Portfolio artwork and photographs remain the property of their respective owners. This repository does not grant a blanket license to reuse them.

## Remaining content

A current résumé has not yet been supplied. Add the real PDF and a clearly labeled download link when available. Add more specific project-role credits and reflections when verified.
