#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 ~ 2014 Deepin, Inc.
#               2013 ~ 2014 Kaisheng Ye
#
# Author:     Kaisheng Ye <kaisheng.ye@gmail.com>
# Maintainer: Kaisheng Ye <kaisheng.ye@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os

def convert(svg_dir, size, png_dir):
    for (root, folders, files) in os.walk(svg_dir):
        for f in files:
            svg_path = os.path.join(root, f)
            ext = os.path.splitext(svg_path)[1]
            if ext == ".svg":
                png_path = os.path.join(png_dir, os.path.splitext(os.path.split(svg_path)[1])[0] + ".png")
                os.system("inkscape -f %s -w %s -e %s" % (svg_path, size, png_path))

if __name__ == "__main__":
    if not len(sys.argv) == 4:
        print "Usage: %s Svg_dir Size Png_dir" % __file__
        exit()
    svg_dir = sys.argv[1]
    size = sys.argv[2]
    png_dir = sys.argv[3]
    convert(svg_dir, size, png_dir)

