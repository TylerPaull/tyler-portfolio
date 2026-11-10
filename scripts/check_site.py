"""Check publication-critical links, assets, headings and image metadata."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / 'dist'

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.source = source
        self.links, self.navigation, self.images, self.ids = [], [], [], set()
        self.headings = 0
        self.has_description = False
        self.is_redirect = False
        self.feed(source.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.headings += 1
        if tag == 'meta' and attrs.get('name') == 'description':
            self.has_description = bool(attrs.get('content'))
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            self.is_redirect = True
            refresh = re.match(
                r'^\s*\d+(?:\.\d+)?\s*;\s*url\s*=\s*(.*?)\s*$',
                attrs.get('content', ''), re.IGNORECASE,
            )
            if refresh:
                self.links.append(refresh.group(1).strip('\"\''))
        if tag == 'a' and attrs.get('href'):
            self.navigation.append(attrs['href'])
        for field in ('href', 'src', 'poster'):
            if attrs.get(field):
                self.links.append(attrs[field])
        for value in attrs.get('srcset', '').split(','):
            if value.strip():
                self.links.append(value.strip().split()[0])
        if tag == 'img':
            self.images.append(attrs)

def resolve_local_target(root, source, route):
    """Resolve a decoded URL path using the site's directory-index behavior."""
    if not route:
        return source
    target = root / route.lstrip('/') if route.startswith('/') else source.parent / route
    target = target.resolve()
    target.relative_to(root)  # Reject paths that escape the published directory.
    if target.is_dir() or route.endswith('/'):
        target = target / 'index.html'
    return target


def check_site(root=ROOT):
    root = Path(root).resolve()
    pages = {p.resolve(): Page(p) for p in sorted(root.rglob('*.html'))}
    errors = []
    if not pages:
        return ['No HTML pages found.']
    for path, page in pages.items():
        name = path.relative_to(root).as_posix()
        if page.headings != 1:
            errors.append(f'{name}: expected one h1')
        if not page.has_description:
            errors.append(f'{name}: missing description')
        for image in page.images:
            for attr in ('alt', 'width', 'height'):
                if not image.get(attr):
                    errors.append(f'{name}: image missing {attr}')
        if not page.is_redirect:
            for link in page.navigation:
                url = urlsplit(link)
                if not url.scheme and not url.netloc and unquote(url.path).lower().endswith('.html'):
                    errors.append(f'{name}: navigation should use a directory URL: {link}')
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            try:
                target = resolve_local_target(root, path, unquote(url.path))
            except ValueError:
                errors.append(f'{name}: link escapes site root: {link}')
                continue
            if not target.is_file():
                errors.append(f'{name}: missing {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{name}: missing anchor {link}')
    return errors


def main():
    errors = check_site()
    if errors:
        print('\n'.join(errors))
        return 1
    count = len(list(ROOT.rglob('*.html')))
    print(f'PASS: {count} pages; local links, assets, fragments, headings and image metadata.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
