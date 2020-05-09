Async Python-PDFKit: HTML to PDF wrapper
==================================

[![Build Status](https://travis-ci.org/shivanshs9/python-pdfkit-async.svg?branch=master)](https://travis-ci.org/shivanshs9/python-pdfkit-async) [![PyPI version](https://badge.fury.io/py/pdfkit-async.svg)](https://badge.fury.io/py/pdfkit-async) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/pdfkit-async.svg)](https://pypi.python.org/pypi/pdfkit-async/)


Python 3.5+ async wrapper for wkhtmltopdf utility to convert HTML to PDF
using Webkit.

**NOTE:** All the public API functions are adapted to async coroutines, so use them with await!

* * * * *

This is adapted version of [ruby
PDFKit](https://github.com/pdfkit/pdfkit) library, so big thanks to
them!

Installation
============

1.  Install python-pdfkit:
```bash
$ pip install pdfkit-async
```

2.  Install wkhtmltopdf:
    -   Windows and other options: check wkhtmltopdf
    [homepage](http://wkhtmltopdf.org/) for binary installers

    -   Debian/Ubuntu:
    ```bash
    $ sudo apt-get install wkhtmltopdf
    ```

    -   macOS:
    ```bash
    $ brew install caskroom/cask/wkhtmltopdf
    ```

**Warning!** Version in debian/ubuntu repos have reduced functionality
(because it compiled without the wkhtmltopdf QT patches), such as adding
outlines, headers, footers, TOC etc. To use this options you should
install static binary from [wkhtmltopdf](http://wkhtmltopdf.org/) site
or you can use [this
script](https://github.com/JazzCore/python-pdfkit/blob/master/travis/before-script.sh).

Usage
=====

For simple tasks:

```python
import pdfkit

async def f():
    await pdfkit.from_url('http://google.com', 'out.pdf')
    await pdfkit.from_file('test.html', 'out.pdf')
    await pdfkit.from_string('Hello!', 'out.pdf')
```

You can pass a list with multiple URLs or files:

```python
await pdfkit.from_url(['google.com', 'yandex.ru', 'engadget.com'], 'out.pdf')
await pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf')
```

Also you can pass an opened file:

```python
with open('file.html') as f:
    await pdfkit.from_file(f, 'out.pdf')
```

If you wish to further process generated PDF, you can read it to a
variable:

```python
# Use False instead of output path to save pdf to a variable
pdf = await pdfkit.from_url('http://google.com', False)
```

You can specify all wkhtmltopdf
[options](http://wkhtmltopdf.org/usage/wkhtmltopdf.txt). You can drop
'--' in option name. If option without value, use *None, False* or *''*
for dict value:. For repeatable options (incl. allow, cookie,
custom-header, post, postfile, run-script, replace) you may use a list
or a tuple. With option that need multiple values (e.g. --custom-header
Authorization secret) we may use a 2-tuple (see example below).

```python
options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ]
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}

await pdfkit.from_url('http://google.com', 'out.pdf', options=options)
```

By default, PDFKit will show all `wkhtmltopdf` output. If you don't want
it, you need to pass `quiet` option:

```python
options = {
    'quiet': ''
    }

await pdfkit.from_url('google.com', 'out.pdf', options=options)
```

Due to wkhtmltopdf command syntax, **TOC** and **Cover** options must be
specified separately. If you need cover before TOC, use `cover_first`
option:

```python
toc = {
    'xsl-style-sheet': 'toc.xsl'
}

cover = 'cover.html'

await pdfkit.from_file('file.html', options=options, toc=toc, cover=cover)
await pdfkit.from_file('file.html', options=options, toc=toc, cover=cover, cover_first=True)
```

You can specify external CSS files when converting files or strings
using *css* option.

**Warning** This is a workaround for [this
bug](http://code.google.com/p/wkhtmltopdf/issues/detail?id=144) in
wkhtmltopdf. You should try *--user-style-sheet* option first.

```python
# Single CSS file
css = 'example.css'
await pdfkit.from_file('file.html', options=options, css=css)

# Multiple CSS files
css = ['example.css', 'example2.css']
await pdfkit.from_file('file.html', options=options, css=css)
```

You can also pass any options through meta tags in your HTML:

```python
body = """
    <html>
      <head>
        <meta name="pdfkit-page-size" content="Legal"/>
        <meta name="pdfkit-orientation" content="Landscape"/>
      </head>
      Hello World!
      </html>
    """

await pdfkit.from_string(body, 'out.pdf') #with --page-size=Legal and --orientation=Landscape
```

Configuration
=============

Each API call takes an optional configuration paramater. This should be
an instance of `pdfkit.configuration()` API call. It takes the
configuration options as initial paramaters. The available options are:

-   `wkhtmltopdf` - the location of the `wkhtmltopdf` binary. By default
    `pdfkit` will attempt to locate this using `which` (on UNIX type
    systems) or `where` (on Windows).
-   `meta_tag_prefix` - the prefix for `pdfkit` specific meta tags - by
    default this is `pdfkit-`

Example - for when `wkhtmltopdf` is not on `$PATH`:

```python
config = pdfkit.configuration(wkhtmltopdf='/opt/bin/wkhtmltopdf')

await pdfkit.from_string(html_string, output_file, configuration=config)
```

Troubleshooting
===============

-   `IOError: 'No wkhtmltopdf executable found'`:

    Make sure that you have wkhtmltopdf in your \$PATH or set via custom
    configuration (see preceding section). *where wkhtmltopdf* in
    Windows or *which wkhtmltopdf* on Linux should return actual path to
    binary.

-   `IOError: 'Command Failed'`

    This error means that PDFKit was unable to process an input. You can
    try to directly run a command from error message and see what error
    caused failure (on some wkhtmltopdf versions this can be cause by
    segmentation faults)
