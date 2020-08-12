# Changelog

- 1.0.5

  - Merged #4: Fix missing await on merging PDFs

- 1.0.4

  - Fixes #2: Use file's absolute path for urlPath (#1)

- 1.0.3

  - Added 'pdfgen-setup' script to setup Chromium
  - Fixed Travis build

- 1.0.0

  - Renamed to PdfGen
  - Migrated to Pyppeteer (headless chromium) and removed wkhtmltopdf support.
  - Migrated to Poetry
  - Added both sync and async APIs
  - Added support to merge pdfs
  - Updated README

- 0.7.2

  - Fixed Project description for latest rules
  - Fixed Travis build
  - Updated README

- 0.7.0

  - Dropped support of Python2.7 till Python3.4
  - Supports Python3.5+
  - AsyncIO support
  - Project took over by [shivanshs9](https://github.com/shivanshs9)

- 0.6.1

  - Fix regression on python 3+ when trying to decode pdf output

- 0.6.0

  - Support repeatable options
  - Support multiple values for some options
  - Fix some corner cases when specific argument order is
    required
  - Some Python 3+ compatibility fixes
  - Update README

- 0.5.0

  - Allow passing multiple css files
  - Fix problems with external file encodings
  - Rise an error when X server is missing on \*nix systems
  - Fix tests that was broken with latest wkhtmltopdf release
  - Update README

- 0.4.1

  - More easier custom configuration setting
  - Update README

- 0.4.0

  - Allow passing file-like objects
  - Ability to return PDF as a string
  - Allow user specification of configuration
  - API calls now returns True on success
  - bugfixes

- 0.3.0

  - Python 3 support

- 0.2.4

  - Add History
  - Update setup.py

- 0.2.3
  - Fix installing with setup.py
  - Update README
