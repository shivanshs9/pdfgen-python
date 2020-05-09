import codecs
from distutils.core import setup
from setuptools.command.test import test as TestCommand
import re
import os
import sys
import pdfkit

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['pdfkit-tests.py']
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        os.chdir('tests/')
        errno = pytest.main(self.test_args)
        sys.exit(errno)

def long_description():
    """Pre-process the README so that PyPi can render it properly."""
    readme = open('README.md').read()
    try:
        history = '\n\n' + open('HISTORY.md').read()
    except:
        history = ''
    return readme + history

setup(
    name='pdfkit-async',
    version=pdfkit.__version__,
    description=pdfkit.__doc__.strip(),
    long_description=long_description(),
    long_description_content_type='text/markdown',
    download_url='https://github.com/shivanshs9/python-pdfkit-async',
    license=pdfkit.__license__,
    tests_require=['pytest', 'pytest-asyncio', 'asynctest'],
    cmdclass = {'test': PyTest},
    packages=['pdfkit'],
    author=pdfkit.__author__,
    author_email='shivanshs9@gmail.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: XML',
        'Topic :: Utilities'
        ]
)
