#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011~2014 Deepin, Inc.
#               2011~2014 Kaisheng Ye
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

import os

def inkscape_convert(svg_path, png_path, size):
    os.system("inkscape -e %s -w %s -h %s %s" % (png_path, size, size, svg_path))

def get_size_dir(hicolor_folder, size):
    folder = os.path.join(hicolor_folder, size, "apps")
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def main(svg_path):
    current_folder = os.path.dirname(svg_path)
    svg_name = os.path.split(svg_path)[1]
    image_name = os.path.splitext(svg_name)[0]
    hicolor_folder = os.path.join(current_folder, "hicolor")

    # move scalable image
    scalable_dir = get_size_dir(hicolor_folder, "scalable")
    scalable_svg_path = os.path.join(scalable_dir, svg_name)
    os.system("mv %s %s" % (svg_path, scalable_svg_path))
    os.system("ln -sf %s %s" % ("hicolor/scalable/apps/%s" % svg_name, svg_path))

    for size in ["16", "24", "48", "64", "96"]:
        hicolor_size = "%sx%s" % (size, size)
        folder = get_size_dir(hicolor_folder, hicolor_size)
        png_path = os.path.join(folder, "%s.png" % image_name)
        inkscape_convert(scalable_svg_path, png_path, size)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])

