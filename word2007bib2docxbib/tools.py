#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zipfile
import tempfile
import shutil
import os
import sys

template_dir = os.path.dirname(__file__)+'-template'
assert os.path.isdir(template_dir)

def convert(input_file_path, output_file_path):

    temp_dir = tempfile.mkdtemp()    

    shutil.copytree(template_dir, temp_dir+'/template')
    shutil.copy(input_file_path, temp_dir+'/template/customXml/item1.xml')

    output_file = zipfile.ZipFile(output_file_path, mode='w', compression=zipfile.ZIP_DEFLATED)

    pwd = os.path.abspath('.')
    os.chdir(temp_dir+'/template')

    files_to_ignore = ['.DS_Store']

    for dir_path, dir_names, file_names in os.walk('.'):
        for file_name in file_names:

            if file_name in files_to_ignore:
                continue

            template_file_path = os.path.join(dir_path, file_name)
            output_file.write(template_file_path, template_file_path[2:])

    output_file.close()
    os.chdir(pwd)

def main():

    if len(sys.argv) < 3:

        print "word2007bib2docxbib"
        print 20*"="
        print ""
        print "  Usage: word2007bib2docxbib <input> <output>"
        print ""
        print "  <input> may be any Word 2007 bibliography (Sources.xml)"
        print "  <outpu> may be any output filename with suffix .docx"
        print ""
        return

    convert(os.path.abspath(str(sys.argv[1])), os.path.abspath(str(sys.argv[2])))
