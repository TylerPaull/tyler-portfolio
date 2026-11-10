"""Regression checks for links after migrating flat pages to directory URLs."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from check_site import check_site


class DirectoryURLTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.page('index.html', '<section id="work"></section>')
        self.page('about/index.html', '<section id="contact"></section>')

    def page(self, name, body='', head=''):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            '<!doctype html><html lang="en"><head>'
            '<meta name="description" content="Fixture page">'
            f'{head}</head><body><h1>Fixture</h1>{body}</body></html>',
            encoding='utf-8',
        )

    def test_root_parent_and_directory_links_resolve_to_index_pages(self):
        self.page('chair/index.html', '''
            <a href="/#work">Home work</a>
            <a href="../#work">Parent work</a>
            <a href="../about/">About</a>
            <a href="../about/?from=chair#contact">Contact</a>
            <a href="./#detail">Detail</a>
            <section id="detail"></section>
        ''')
        self.assertEqual(check_site(self.root), [])

    def test_fragment_checks_use_normalized_directory_target(self):
        self.page('chair/index.html', '<a href="../about/#missing">Missing section</a>')
        self.assertEqual(check_site(self.root), [
            'chair/index.html: missing anchor ../about/#missing',
        ])

    def test_nested_asset_paths_are_relative_to_the_nested_page(self):
        (self.root / 'assets').mkdir()
        (self.root / 'assets/chair.webp').write_bytes(b'image fixture')
        self.page('chair/index.html', '''
            <img src="../assets/chair.webp" alt="Chair" width="640" height="480">
            <img src="assets/chair.webp" alt="Broken path" width="640" height="480">
        ''')
        self.assertEqual(check_site(self.root), [
            'chair/index.html: missing assets/chair.webp',
        ])

    def test_directory_without_index_is_not_a_valid_page(self):
        (self.root / 'unfinished').mkdir()
        self.page('chair/index.html', '<a href="../unfinished/">Unfinished</a>')
        self.assertEqual(check_site(self.root), [
            'chair/index.html: missing ../unfinished/',
        ])

    def test_missing_directory_is_reported(self):
        self.page('chair/index.html', '<a href="../absent/">Missing page</a>')
        self.assertEqual(check_site(self.root), [
            'chair/index.html: missing ../absent/',
        ])

    def test_recursive_discovery_checks_unlinked_nested_pages(self):
        self.page('studies/chair/index.html', '<a href="../../#absent">Missing section</a>')
        self.assertEqual(check_site(self.root), [
            'studies/chair/index.html: missing anchor ../../#absent',
        ])

    def test_regular_pages_must_use_clean_internal_navigation(self):
        self.page('chair/index.html', '''
            <a href="../about/index.html#contact">Old local URL</a>
            <a href="https://example.com/reference.html">External reference</a>
        ''')
        self.assertEqual(check_site(self.root), [
            'chair/index.html: navigation should use a directory URL: ../about/index.html#contact',
        ])

    def test_legacy_redirect_and_fallback_target_a_directory(self):
        self.page('about.html', '<a href="about/">Continue</a>',
                  '<meta http-equiv="refresh" content="0; url=about/">')
        self.assertEqual(check_site(self.root), [])

    def test_broken_redirect_target_is_checked(self):
        self.page('legacy.html', '<a href="/">Home</a>',
                  '<meta http-equiv="refresh" content="0; url=absent/">')
        self.assertEqual(check_site(self.root), ['legacy.html: missing absent/'])


if __name__ == '__main__':
    unittest.main()
