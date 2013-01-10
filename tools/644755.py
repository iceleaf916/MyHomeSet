#!/usr/bin/python
# coding: utf-8

import os, sys

USAGE = '''
This script gives all dirs 0755 and all files 0644 access authority in the dir_path.
Usage:
    python %s dir_path
''' % __file__

def chmod755(path):
    if os.path.isdir(path):
        try:
            os.chmod(path, 0755)
            print "chmod 0755 %s: OK!" % path
        except Exception, e:
            print e

def chmod644(path):
    if os.path.isfile(path):
        try:
            os.chmod(path, 0644)
            print "chmod 0644 %s: OK!" % path
        except Exception, e:
            print e

def walk(dir_path):
    for root, dirs, files in os.walk(dir_path):
        chmod755(root)
        for f in files:
            chmod644(os.path.join(root, f))

def run(path):
    if not os.path.isdir(path):
        print 'Error:"%s" is not a folder path.' % path
        sys.exit(1)
    else:
        walk(path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print USAGE
        sys.exit(0)
    else:
        path = sys.argv[1].strip()
        run(path)

