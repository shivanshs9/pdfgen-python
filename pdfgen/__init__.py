# -*- coding: utf-8 -*-
"""
Pyppeteer-based async python wrapper to convert html to pdf
"""

__forked_from__ = 'Golovanov Stanislav'
__author__ = 'Shivansh Saini'
__version__ = '1.0.5'
__license__ = 'MIT'

import pdfgen.api_sync as sync

from .api_async import from_file, from_sources, from_string, from_url
from .configuration import configuration
from .pdfgen import PDFGen
from .source import Source
