# -*- coding: utf-8 -*-
from syncasync import async_to_sync

from pdfgen import api_async


def from_url(url, output_path=None, options=None):
    """
    Convert file of files from URLs to PDF document

    :param url: URL or list of URLs to be saved
    :param output_path: (optional) path to output PDF file. If not provided, PDF will be returned as string
    :param options: (optional) dict to configure pyppeteer page.pdf action

    Returns: output_path if provided else PDF Binary
    """
    return async_to_sync(api_async.from_url)(url, output_path, options)


def from_file(input, output_path=None, options=None):
    """
    Convert HTML file or files to PDF document

    :param input: path to HTML file or list with paths or file-like object
    :param output_path: (optional) path to output PDF file. If not provided, PDF will be returned as string
    :param options: (optional) dict to configure pyppeteer page.pdf action

    Returns: output_path if provided else PDF Binary
    """
    return async_to_sync(api_async.from_file)(input, output_path, options)


def from_string(input, output_path=None, options=None):
    """
    Convert given string or strings to PDF document

    :param input: string with a desired text. Could be a raw text or a html file
    :param output_path: (optional) path to output PDF file. If not provided, PDF will be returned as string
    :param options: (optional) dict to configure pyppeteer page.pdf action

    Returns: output_path if provided else PDF Binary
    """

    return async_to_sync(api_async.from_string)(input, output_path, options)


def from_sources(sources, output_path=None, options=None):
    """
    Convert given sources to PDF document

    :param sources: list of source objects
    :param output_path: (optional) path to output PDF file. If not provided, PDF will be returned as string
    :param options: (optional) dict to configure pyppeteer page.pdf action

    Returns: output_path if provided else PDF Binary
    """
    return async_to_sync(api_async.from_url)(sources, output_path, options)
