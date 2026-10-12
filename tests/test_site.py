"""Static-site smoke test (freesongfromreel standard).

Run: python -m pytest tests/test_site.py
"""
from pathlib import Path
import re

SITE = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "help.html", "about.html", "privacy.html", "terms.html", "contact.html"]


def _read(name: str) -> str:
    return (SITE / name).read_text(encoding="utf-8")


def test_all_pages_present():
    for p in PAGES:
        assert (SITE / p).exists(), f"missing {p}"


def test_every_page_has_title_and_meta_description():
    for p in PAGES:
        html = _read(p)
        assert "<title>" in html, f"{p} missing <title>"
        assert 'name="description"' in html, f"{p} missing meta description"


def test_index_has_schema_canonical_and_adsense():
    html = _read("index.html")
    assert 'rel="canonical"' in html, "index missing canonical"
    assert "application/ld+json" in html, "index missing schema markup"
    assert "adsbygoogle" in html, "index missing AdSense loader"


def test_index_inline_js_has_balanced_braces():
    scripts = re.findall(r"<script>(.*?)</script>", _read("index.html"), re.S)
    assert scripts, "index must have an inline script block"
    for s in scripts:
        assert s.count("{") == s.count("}"), "unbalanced braces in inline JS"


def test_footer_links_resolve():
    html = _read("index.html")
    for target in PAGES:
        if target != "index.html":
            assert f'href="{target}"' in html, f"footer should link {target}"


def test_help_page_has_content_sections():
    html = _read("help.html")
    assert html.count("<h2") >= 4, "help page should have section headings"
    assert "track.js" in html, "help page should load tracking"