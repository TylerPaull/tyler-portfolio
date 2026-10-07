# Editorial image sources and AI edit notes

September 29, 2026. The layout follows the object-first, numbered-story approach introduced for Nucite. All project subjects come from Tyler's existing work.

## Published opening visuals

| Project | Source and treatment | Published assets |
| --- | --- | --- |
| BARE | Full-size chair photo from Tyler's original BARE portfolio (`portmanteau-1.png`); background removed with the built-in image-generation tool in edit mode. Tyler explicitly rejected the earlier small pencil model. | `dist/assets/editorial-bare-fullsize-chair-{640,1210}.webp` |
| Ostra | Front photograph extracted from `Lipman_Tyler_3F_Final-1 (2).pdf`; background removed with the same built-in tool in edit mode. Tyler approved this lamp image. | `dist/assets/editorial-ostra-{640,1199}.webp` |
| Nucite | Original tray-application study from the supplied Studio III booklet, retained. | Existing `nucite-*` files, documented in `asset-manifest.json`. |
| Butterfly | Original axonometric linework rendered from the vector plot; no AI redraw. | `dist/assets/editorial-pavilion-axon-{640,1280,2400}.webp` |
| Balance | Updated October 4: Tyler’s hand-drawn floor plan from `XEROX.pdf`, page 1. Page margins trimmed during PDF rendering; horizontal on desktop, upright on phones; no AI redraw. | `dist/assets/balance-floorplan-landscape-{640,1280,2400}.webp` and `balance-floorplan-portrait-{640,1000}.webp` |

The BARE transformation switch and closing gallery retain the original full-size chair and bench photographs. The small pencil-model cutouts and rejected bench cutout attempts are not published. Background editing is generative and is not evidence of fabrication details; unedited source photographs remain in the case studies. WebP encoding, responsive sizing and transparent-canvas trimming are display preparation.

## Background-edit prompts

BARE final chair, built-in image tool, referenced-image edit mode:

> Use case: background-extraction. This is a real photograph of Tyler's full-size BARE furniture in its chair with raised backrest. Remove ONLY the room, wall, window, floor, outlet and floor shadows. Return the exact same photographed full-size furniture as a genuine transparent-alpha cutout, including empty transparency between and beneath slats. Preserve the complete exact silhouette, perspective, all plywood slats, their count and arrangement, dowels, notches, comb connectors, wood texture, photographic shading and construction imperfections. Do NOT redesign, reconstruct, mirror, add parts, make a miniature, add pencils, or change materials or proportions. Center the whole original object in a tight frame with small even transparent margin, without cropping any part. No halo, color wash, glow, background, vignette, checkerboard or cast shadow. Faithful background removal only.

Ostra, built-in image tool, referenced-image edit mode:

> Use case: background-extraction. Edit target: the supplied photograph of Tyler's actual Ostra lamp. Remove ONLY the wall, tabletop, shadows and loose trailing cord outside the object. Produce a clean photographic cutout with a genuinely transparent alpha background, including transparency through the four large open frame areas. Keep the exact photographed lamp shape, perspective, all wooden frame members, finger joints, central layered perforated panels, wood texture, imperfections and existing subtle glow. Do not redesign, mirror, change geometry, add parts, smooth the craft, brighten or relight. The full object must fit with small even transparent breathing room. No color wash, backdrop, halo, vignette, fake checkerboard or drop shadow. This is a faithful background removal for a professional portfolio.

## Faithful drawing and photograph extraction

Six pavilion drawings were rendered from original vector PDF regions. Source page, crop rectangles, dimensions, and resolution are in `pavilion-drawing-sources.json`. The final case study replaces the full boards with plans, sections, an environmental diagram, and short source-grounded explanations. The source boards establish Spring 2026; print-scale claims are omitted for responsive digital display.

Ostra photographs and geometry/assembly diagrams were separated from their source sheets. Their source files and extraction regions are in `ostra-image-sources.json`. No generated geometry is substituted for the design drawings. The development model is identified as cardboard, and the final object as wood-framed.

All deployed responsive variants are listed in `asset-manifest.json`.

## The Laurel Group — October 6 addition

The six selected reference/concept images are supplied internship assets, published as `laurel-garden-reference-*`, `laurel-garden-concept-*`, `laurel-terrace-reference-*`, `laurel-pergola-concept-*`, `laurel-entry-brick-*`, and `laurel-entry-stone-*`. The workflow excerpt is a faithful rendering of page 2 of `RENDERING_LIVEDEMO.pdf`, published as `laurel-workflow-*`. No new generation, background removal, or retouching was performed. AI-assisted concepts are explicitly labeled.

The public asset manifest records descriptive source notes, hashes and output dimensions; client-identifying source paths remain local. Guide authorship is not asserted. Tyler confirmed his title as Creative Design Intern.


## Internship process studies — October 7 expansion

Added 24 source assets as responsive WebP variants. The SS-Mayer annotation image is a faithful crop removing only the viewer interface; the underlying annotations remain unchanged. Beach Road, entry, and pergola drawings are faithful PDF-region renderings, with title blocks excluded. The garden CAD excerpt is cropped from its original screenshot and retains its native low resolution. All drawings open at their largest published resolution. Source checksums, crop coordinates, and dimensions are recorded in `asset-manifest.json`; private original-path mappings remain outside the repository.

No new imagery was generated, and no design geometry was redrawn. Supplied AI-assisted visualizations remain labeled as concepts throughout the overview and case studies. The public contractor specification summary reproduces relevant dimensional/material facts rather than the financial proposal document.
