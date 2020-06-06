# -*- coding: utf-8 -*-
import codecs
import io
import os
import sys
import unittest

import pytest

import pdfgen
from pdfgen.errors import InvalidSourceError

TEST_PATH = os.path.dirname(os.path.realpath(__file__))
EXAMPLE_HTML_FILE = f'{TEST_PATH}/fixtures/example.html'


class TestPdfGenerationSyncApi(unittest.TestCase):
    """Test to_pdf() method in Synchronous world"""

    def setUp(self):
        pass

    def tearDown(self):
        if os.path.exists('out.pdf'):
            os.remove('out.pdf')

    def test_pdf_generation_from_html(self):
        pdf = pdfgen.sync.from_string('html', 'out.pdf', options={'format': 'Letter'})
        self.assertEqual(pdf, 'out.pdf')

    def test_pdf_generation_from_url(self):
        pdf = pdfgen.sync.from_url('http://networkcheck.kde.org', 'out.pdf', options={'format': 'Letter'})
        self.assertEqual(pdf, 'out.pdf')

    def test_raise_error_with_invalid_url(self):
        with self.assertRaises(InvalidSourceError):
            pdf = pdfgen.sync.from_url('wrongurl.com', 'out.pdf')

    def test_pdf_generation_from_file_same_directory(self):
        with open('testfile.html', 'w') as f:
            f.write("html")

        path = 'testfile.html'

        pdf = pdfgen.sync.from_file(path, 'out.pdf')
        self.assertEqual(pdf, 'out.pdf')

        os.remove(path)

    def test_raise_error_with_invalid_file_path(self):
        paths = ['frongpath.html', 'wrongpath2.html']
        with self.assertRaises(InvalidSourceError):
            pdfgen.sync.from_file(paths, 'file')

    def test_pdf_generation_from_file(self):
        pdf = pdfgen.sync.from_file(EXAMPLE_HTML_FILE, 'out.pdf')
        self.assertEqual(pdf, 'out.pdf')

    def test_pdf_generation_from_file_like(self):
        with open(EXAMPLE_HTML_FILE, 'r') as f:
            pdf = pdfgen.sync.from_file(f)
        self.assertEqual(pdf[:4].decode('utf-8'), '%PDF')


if __name__ == "__main__":
    unittest.main()
