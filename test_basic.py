#!/usr/bin/env python3
"""Basic smoke tests for the article-to-pdf-extractor app."""
import os

HTML_PATH = os.path.join(os.path.dirname(__file__), "index.html")


def get_html():
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        return f.read()


def test_index_html_exists_and_nonempty():
    assert os.path.isfile(HTML_PATH), "index.html does not exist"
    assert os.path.getsize(HTML_PATH) > 0, "index.html is empty"


def test_index_html_has_doctype():
    assert "<!doctype html>" in get_html().lower(), "index.html missing <!doctype html>"


def test_index_html_has_jspdf():
    assert "jspdf" in get_html().lower(), "index.html missing jsPDF reference"


def test_index_html_has_localstorage():
    assert "localstorage" in get_html().lower(), "index.html missing localStorage"


def test_index_html_has_bookmarklet():
    assert "bookmarklet" in get_html().lower(), "index.html missing bookmarklet"


if __name__ == "__main__":
    tests = [
        test_index_html_exists_and_nonempty,
        test_index_html_has_doctype,
        test_index_html_has_jspdf,
        test_index_html_has_localstorage,
        test_index_html_has_bookmarklet,
    ]
    for t in tests:
        t()
        print(f"  ✓ {t.__name__}")
    print(f"\nAll {len(tests)} tests passed.")
