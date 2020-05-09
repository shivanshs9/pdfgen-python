# -*- coding: utf-8 -*-
"""
Wkhtmltopdf python wrapper to convert html to pdf using the webkit rendering engine and qt
"""

__forked_from__ = 'Golovanov Stanislav'
__author__ = 'Shivansh Saini'
__version__ = '0.7.2'
__license__ = 'MIT'

from .pdfkit import PDFKit
from .api import from_url, from_file, from_string, configuration
