# Replacement-site validation

November 17, 2026. Tyler requested replacement of the existing portfolio with the supplied Claude static site, following its README.

## Source fidelity

- The ZIP passed its integrity check, and safe extraction rejected absolute paths, parent traversal and symlink entries.
- All 15 page bodies preserve the supplied visible words, captions, alternative text, inline styles and original CSS. Only the keyboard skip link adds visible text, when focused.
- All 91 supplied image/video files remain byte-identical. Checksums are recorded in `import-manifest.json`.
- The original README is preserved unchanged in this folder.

## Integration

- The 15 established clean page addresses remain canonical.
- Fourteen existing `.html` URLs, five newly supplied `.html` names, and five alternate directory names redirect to canonical pages.
- All 48 redirect cases (24 stubs, HTTP(S) and direct-file contexts) preserve query strings and fragments.
- Legacy section names map to the corresponding sections of the new layout. BARE caption/chair/bench targets and NUCITE's final tray target are retained.
- Search/social metadata, intrinsic image dimensions, main landmarks, keyboard skip links and a 404 recovery page were added without changing the supplied design.
- BARE keeps autoplay, loop, mute and inline playback; native controls remain removed per Tyler's earlier request.

## Local checks

- Existing site checker: all 40 HTML files passed route, asset, fragment, heading, description and image-attribute checks.
- Existing routing unit tests: 9 passed.
- Browser at 1440 px and 390 px: all 15 real pages loaded their images with no horizontal overflow.
- Home was visually inspected at desktop and mobile sizes; BARE transformation was inspected on mobile.
- BARE video was observed playing, with looping/mute active and native controls absent.
- Keyboard Tab reveals the skip-to-content link.
- Browser navigation from `bare.html?from=saved#section-2` reaches `/bare/?from=saved#section-2` and scrolls to Transformation.
- The new `/laurel-group/` alias reaches `/laurel/`, retaining the query and `#projects` section.

Deployment uses the existing main/gh-pages workflow. The prior site remains available in Git at `d2132ca` and in a local backup. Public deployment verification follows publication.
