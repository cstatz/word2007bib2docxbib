#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.command.install import INSTALL_SCHEMES
from setuptools import setup, find_packages
from glob import glob

for scheme in INSTALL_SCHEMES.values(): scheme['data'] = scheme['purelib']

setup(name='word2007bib2docxbib',
      version='0.1.0',
      description='The word2007bib2docxbib module embeds a MS Word 2007 bibliography in form of a Sources.xml as bibliography into a docx document.',
      author='Christoph Statz',
      author_email='statz@wh2.tu-dresden.de',
      url='https://word2007bib2docxbib.googlecode.com',
      license='New BSD License',
      packages=find_packages(),
      data_files=[
          ('word2007bib2docxbib-template/', glob('template/*.xml')),
          ('word2007bib2docxbib-template/_rels', glob('template/_rels/.*')),
          ('word2007bib2docxbib-template/docProps', glob('template/docProps/*.*')),
          ('word2007bib2docxbib-template/word', glob('template/word/*.xml')),
          ('word2007bib2docxbib-template/word/theme', glob('template/word/theme/*.*')),
          ('word2007bib2docxbib-template/word/_rels', glob('template/word/_rels/*.*')),
          ('word2007bib2docxbib-template/customXml', glob('template/customXml/*.xml')),
          ('word2007bib2docxbib-template/customXml/_rels', glob('template/customXml/_rels/*.*')),
          ],
      entry_points = {
        'console_scripts': [
            'word2007bib2docxbib = word2007bib2docxbib:entry_point'
        ],
      },
      )
