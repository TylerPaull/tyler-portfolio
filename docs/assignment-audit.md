# Assignment audit

Round 1: September 29, 2026. Final review: October 8, 2026, using the same repository. This records evidence, not a predicted grade.

**Editorial redesign baseline — September 29:** The five-case-study redesign is published and verified. BARE uses the full-size chair. GitHub Pages built the exact `gh-pages` commit `78f0675ae0e58f698d98972b8fedcf0d3862637c`, corresponding to `main` commit `db3fa00`; local and public checks are recorded below. The October 4 request to replace Balance's opening image with Tyler's floor plan from `XEROX.pdf` is a subsequent change and is not covered by this baseline verification.

| Category | Points | Current evidence | Remaining |
| --- | ---: | --- | --- |
| Live and published | 25 | Public repository and HTTPS GitHub Pages site verified through the September 29 editorial redesign; deployment evidence is recorded below. | Verify the subsequent October 4 Balance image change after publication; Tyler’s final review and Canvas submission. |
| Portfolio quality | 50 | Five source-grounded case studies, verified background, process images, real contact email. | Current résumé; stronger explicit contribution/credits and Tyler's reflections when available. |
| Design and presentation | 30 | Five case studies with clean opening images, numbered narratives, real portrait, and original project photographs/drawings. | Tyler's final review. |
| Web best practices | 25 | Semantic HTML; skip link; headings; image alternatives and dimensions; responsive images; focus styles; reduced motion. | No formal screen-reader audit performed; browser zoom testing beyond responsive-width checks remains unverified. |
| GitHub workflow | 20 | Public repository, meaningful pushed commits, README, source/asset provenance, validation and publication scripts. | Submit the repository URL to Canvas. |

## Completed checks — initial version

- All six main pages checked in the browser at 320, 390, 768, and 1440 CSS-pixel widths: no horizontal page overflow; exactly one h1 per page.
- Visually inspected the desktop homepage and mobile homepage/BARE interaction.
- Chair button selects the chair image, hides the bench image, and updates both pressed states.
- Local validation passes for seven HTML files, including the 404 page: local links, fragments, image sources/variants, headings, descriptions, alt text, and intrinsic dimensions.
- JavaScript syntax check passed.
- Independent source/content review found no substantive unsupported claims or placeholder content. It identified footer focus contrast and nested 404 paths; both were corrected.
- Focus outline is light on the dark footer; ordinary text uses high-contrast dark/light combinations.

## Content accuracy

BARE is the verified project title; the source does not establish the suffix “001.” Ostra is a studio lighting object with cardboard development studies. Butterfly is labeled a proposal and dated Spring 2026 following the supplied original studio boards. Balance is explicitly in progress. No invented solo roles, testing metrics, materials, measurements, awards, or clinical outcomes are included.

## Submission still required

Tyler must submit the verified public repository URL, live GitHub Pages URL, and a short screen-share walkthrough through Canvas. The walkthrough and Canvas submission have not been completed by this build.

After Round 1, record feedback and keep improving the same repository before October 8. Mapping a custom domain is optional and has not been performed.

## Initial public deployment verification

- Repository: https://github.com/TylerPaull/tyler-portfolio — public, default branch `main`.
- Live site: https://tylerpaull.github.io/tyler-portfolio/ — HTTPS enforced.
- GitHub Pages reports `built`, from `gh-pages` at `/`, with no build error.
- Published website commit: `fed1ac4562492c924d8823c8b6e83f683be4d7c6`.
- All 81 published HTML, CSS, JavaScript, and WebP files returned HTTP 200. The public homepage matched the local file byte for byte.
- All six main public pages checked at 390 and 1440 CSS pixels: no horizontal overflow and correct page titles.
- Public nested missing URL returned the custom 404; its CSS and recovery link resolved to the correct repository base and the recovery link worked.
- Public BARE switch tested with Enter and Space: image visibility and pressed states updated correctly. No warning or error logs were reported during that check.
- Contact uses Tyler’s supplied `tlipman@tulane.edu` mailto address. No email was sent.

The résumé, video recording, Canvas submission, and optional custom-domain mapping remain outside the completed publication.

## Supplied media update — September 28

- Replaced the homepage and About portrait with Tyler’s supplied transparent headshot. Verified the full head remains visible at phone and desktop sizes; the headshot update was confirmed on the public site.
- Added Tyler’s CNC cut plan and exploded assembly drawing to BARE, with responsive display images and full-resolution local downloads.
- Added the supplied 11-second, 1280×720 rotation animation without transcoding. It has no audio track, no autoplay, native playback controls, a video-derived poster, and a written visual description. Local playback and the mobile player layout were verified.
- Removed the unverified exact dowel count from BARE’s introductory copy while retaining the supported mechanism description.
- Static validation covers the new source, poster, image variants, and full-resolution drawing links.

- Replaced the earlier headshot with Tyler’s final `NEWAI.png` selection; checked the transparent portrait at 390px and 1440px. Content-specific asset names refresh cached portraits.
- Added zero minimum widths to case-study grid children and constrained the video width; versioned the shared stylesheet to refresh cached mobile styles. Verified the 350px-wide player fits a 390px viewport without horizontal overflow.

## Nucite case study update

- Added the supplied Studio III material study under its latest documented name, Nucite, as the third homepage project. Updated next-project links and numbering; Balance closes the five-project grid with a wider image.
- Selected 13 original image assets from the corrected OSM booklet and generated 29 responsive WebP variants with descriptive alternatives and full-image links.
- Verified sample quantities and narrative against the source. Copy describes a material exploration and tray application study, without unsupported performance or food-contact claims.
- Local validation passes for eight HTML pages. Nucite and the homepage were checked at 390px and 1440px without horizontal overflow. The Nucite homepage link and a full-image link worked; no browser warning or error logs were reported.

## Editorial redesign — September 29

- Reorganized all five project pages around clean opening images and numbered narratives, carrying the Nucite story format across the portfolio.
- Rebuilt Butterfly Streetcar Pavilion around six standalone drawings rendered from page 1 of the original vector plot: axonometric, ground plan, roof plan, two sections, and environmental diagram. Full plot boards are removed; atmosphere renderings support the final experience section.
- Corrected the pavilion date to Spring 2026 and course to Design II Studio / DESG 3005 using the supplied original plot and final-review board. Roof drainage and planting are presented as design intentions rather than tested outcomes.
- Replaced Ostra's full-sheet presentation with extracted photographs and diagrams covering geometry, cardboard prototypes, assembly, and illumination. Captions distinguish cardboard development studies from the final wood-framed light.
- Recorded source pages, extraction rectangles and dimensions in `pavilion-drawing-sources.json` and `ostra-image-sources.json`, with responsive variants in `asset-manifest.json`.
- Tyler rejected the small pencil-model image as BARE's main photograph. It was replaced with a background-removed photograph of the full-size chair; no small model cutouts are published. The original full-size photographs remain in the switch and closing gallery.
- **Redesign baseline local checks:** all seven content pages at 320, 390, 768 and 1440 CSS pixels have no horizontal overflow and one h1. Desktop opening visuals and mobile pavilion drawings/BARE comparison were visually reviewed. The BARE switch works by click and Enter with correct visibility and pressed states; video metadata loads with an 11-second duration and no playback error. The pavilion ground-plan link opens the complete 2400px image. Static validation passes for eight HTML pages. Browser warning/error logs were empty.
- **Redesign baseline public verification:** GitHub Pages reports `built` for exact `gh-pages` commit `78f0675ae0e58f698d98972b8fedcf0d3862637c`, corresponding to `main` commit `db3fa00`. All 47 checked HTML, CSS, JavaScript, and new editorial asset files returned HTTP 200 and matched the local files byte for byte. The workspace verification record is `work/editorial-refresh/public-verification.json`.
- The live desktop homepage at 1440 CSS pixels and mobile pavilion page at 390 CSS pixels were verified. This public evidence applies to the published editorial redesign, not to the subsequent October 4 Balance floor-plan change, whose checks are still separate and pending.

The résumé, verified contribution/credits and reflections, walkthrough recording, Canvas submission, formal screen-reader audit, and browser zoom checks beyond responsive-width testing remain unresolved as described above. No custom-domain mapping has been performed.

## Balance floor-plan cover — October 4

- Replaced the homepage card and project opening with Tyler’s hand-drawn floor plan from `XEROX.pdf`. The original drawing is preserved; only page margins and viewing orientation change.
- Verified desktop landscape framing at 1440 CSS pixels and the upright phone image at 390 CSS pixels. No horizontal overflow on Balance; the full-plan link loads the complete 1000 × 2860 image.
- Static validation passes for all eight HTML pages. Published from main `9967933` to GitHub Pages commit `66d84c4afa1e194ac4bf97e0d3b129ea4908020c`, confirmed built without error. All 15 checked pages, shared files, and floor-plan images returned HTTP 200 and matched local files byte for byte. The live Balance page selects the upright image at 390px and landscape image at 1440px with no overflow; browser warning/error logs were empty.

## BARE continuous playback — October 4

- Enabled native muted inline autoplay and looping at Tyler’s request, retaining controls so visitors can pause. This supersedes the initial click-to-play behavior recorded above.
- Verified automatic playback when the video enters view, followed by a complete 11-second cycle and a return to 3 seconds while still playing. Native `loop`, `muted`, `playsInline`, and controls are enabled; no media error was reported.
- Static publication checks passed for all eight pages.

## The Laurel Group experience — October 6

- Added `laurel.html` with the user-confirmed Creative Design Intern title, year 2026, selected visualization studies, explicit AI-assisted concept captions, team design credits, and a clean workflow-document excerpt. Home includes an Experience feature and direct introduction link; About includes the role and case-study link.
- Source and visual review checked attribution and selected images. Only neutral selected content is included in the public files; private client identifiers, raw records, and the full internship archive remain outside the repository.
- Home, About, and the internship page fit 320, 390, and 768 CSS-pixel widths without horizontal overflow, with one h1 each. Desktop internship and homepage feature reviewed at 1440px; mobile internship visually reviewed at 390px. About and breadcrumb navigation work, as does the workflow full-image link. Browser warning/error logs were empty. Static validation passes for nine HTML pages.
