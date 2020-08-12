# -*- coding: utf-8 -*-
import asyncio
import codecs
import io
import re
import subprocess
import sys
from tempfile import NamedTemporaryFile

from PyPDF2 import PdfFileMerger
from pyppeteer import errors, launch

from .configuration import DEFAULT_CONFIG
from .errors import InvalidSourceError
from .source import Source
from .utils import is_iterable


class PDFGen(object):
    """
    Main class that does all generation routine.

    :param url_or_file: str - either a URL, a path to a file or a string containing HTML
                       to convert
    :param type_: str - either 'url', 'file' or 'string'
    :param options: dict (optional) with pyppeteer options
    """

    def __init__(self, sources, options=None):
        self.sources = sources if is_iterable(sources) else [sources]
        self.configuration = DEFAULT_CONFIG
        self.options = self.configuration.options
        self.environ = self.configuration.environ
        if options is not None:
            self.options.update(options)

    async def print_pyppeteer(self, source, output_path):
        is_stdout = (not output_path) or (output_path == '-')
        try:
            page = await self.browser.newPage()
            if source.isString():
                await page.setContent(source.to_s())
            elif source.isFileObj():
                await page.setContent(source.source.read())
            else:
                path = source.urlPath()
                await page.goto(path)
            options = self.options
            options.update(self._find_options_in_meta(await page.content()))
            if not is_stdout:
                options['path'] = output_path
            stdout = await page.pdf(options)

            return stdout if is_stdout else output_path
        finally:
            await page.close()

    async def merge_pdfs(self, input_pdfs, output_path=None):
        is_stdout = (not output_path) or (output_path == '-')
        merger = PdfFileMerger()
        for pdf in input_pdfs:
            merger.append(pdf)
        if is_stdout:
            output = io.BytesIO()
        else:
            output = output_path
        merger.write(output)

        return output.getvalue() if is_stdout else output_path

    async def to_pdf(self, path=None):
        result = None
        self.browser = await launch(args=["--no-sandbox"], env=self.environ)
        try:
            count = len(self.sources)
            result = await asyncio.gather(*(
                self.print_pyppeteer(source, self._get_output_path(path, i, count))
                for i, source in enumerate(self.sources)
            ))
        except errors.NetworkError as e:
            raise InvalidSourceError(e)
        finally:
            await self.browser.close()

        if count > 1:
            result = await self.merge_pdfs(result, path)
        else:
            if is_iterable(result):
                result = result[0]
        return result

    def _get_output_path(self, path, i, count):
        if count > 1:
            return NamedTemporaryFile(prefix=f'{path}-{i}-', suffix='.pdf', delete=False).name
        else:
            return path

    def _find_options_in_meta(self, content):
        """Reads 'content' and extracts options encoded in HTML meta tags

        :param content: str or file-like object - contains HTML to parse

        returns:
          dict: {config option: value}
        """
        if (isinstance(content, io.IOBase)
                or content.__class__.__name__ == 'StreamReaderWriter'):
            content = content.read()

        found = {}

        for x in re.findall('<meta [^>]*>', content):
            if re.search('name=["\']%s' % self.configuration.meta_tag_prefix, x):
                name = re.findall('name=["\']%s([^"\']*)' %
                                  self.configuration.meta_tag_prefix, x)[0]
                found[name] = re.findall('content=["\']([^"\']*)', x)[0]

        return found
