# Assignment audit

Round 1: September 29, 2026. Final review: October 8, 2026, using the same repository. This records evidence, not a predicted grade.

| Category | Points | Current evidence | Remaining |
| --- | ---: | --- | --- |
| Live and published | 25 | Public repository and HTTPS GitHub Pages site live; all 81 published files return HTTP 200; direct pages work on desktop/mobile. | Tyler’s final review and Canvas submission. |
| Portfolio quality | 50 | Four source-grounded case studies, verified background, process images, real contact email. | Current résumé; stronger explicit contribution/credits and Tyler's reflections when available. |
| Design and presentation | 30 | Editorial design, real portrait, original project images, no placeholders. | Tyler's final content and visual review. |
| Web best practices | 25 | Semantic HTML; skip link; headings; image alternatives and dimensions; responsive images; focus styles; reduced motion. | No formal screen-reader audit performed; browser zoom testing beyond responsive-width checks remains unverified. |
| GitHub workflow | 20 | Public repository, meaningful pushed commits, README, source/asset provenance, validation and publication scripts. | Submit the repository URL to Canvas. |

## Completed checks

- All six main pages checked in the browser at 320, 390, 768, and 1440 CSS-pixel widths: no horizontal page overflow; exactly one h1 per page.
- Visually inspected the desktop homepage and mobile homepage/BARE interaction.
- Chair button selects the chair image, hides the bench image, and updates both pressed states.
- Local validation passes for seven HTML files, including the 404 page: local links, fragments, image sources/variants, headings, descriptions, alt text, and intrinsic dimensions.
- JavaScript syntax check passed.
- Independent source/content review found no substantive unsupported claims or placeholder content. It identified footer focus contrast and nested 404 paths; both were corrected.
- Focus outline is light on the dark footer; ordinary text uses high-contrast dark/light combinations.

## Content accuracy

BARE is the verified project title; the source does not establish the suffix “001.” Ostra is a studio lighting object. Butterfly is labeled a proposal. Balance is explicitly in progress. No invented solo roles, testing metrics, materials, measurements, awards, or clinical outcomes are included.

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
