"""Check publication-critical links, assets, headings and image metadata."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1] / 'dist'
BASE = '/'

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.source = source
        self.links, self.images, self.ids = [], [], set()
        self.headings = 0
        self.has_description = False
        self.feed(source.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.headings += 1
        if tag == 'meta' and attrs.get('name') == 'description':
            self.has_description = bool(attrs.get('content'))
        for field in ('href', 'src', 'poster'):
            if attrs.get(field):
                self.links.append(attrs[field])
        for value in attrs.get('srcset', '').split(','):
            if value.strip():
                self.links.append(value.strip().split()[0])
        if tag == 'img':
            self.images.append(attrs)

pages = {p: Page(p) for p in ROOT.glob('*.html')}
errors = []
for path, page in pages.items():
    if page.headings != 1:
        errors.append(f'{path.name}: expected one h1')
    if not page.has_description:
        errors.append(f'{path.name}: missing description')
    for image in page.images:
        for attr in ('alt', 'width', 'height'):
            if not image.get(attr):
                errors.append(f'{path.name}: image missing {attr}')
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        route = unquote(url.path)
        if route.startswith(BASE):
            target = ROOT / route[len(BASE):]
        elif route.startswith('/'):
            errors.append(f'{path.name}: unexpected absolute path {link}')
            continue
        else:
            target = (path.parent / route) if route else path
        if not target.exists():
            errors.append(f'{path.name}: missing {link}')
        elif url.fragment and target in pages and url.fragment not in pages[target].ids:
            errors.append(f'{path.name}: missing anchor {link}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(pages)} pages; local links, assets, fragments, headings and image metadata.')
