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

import os
import sys

exts = [".cpp", ".h", ".qml", ".py"]

def deal_line(line):
    middle = line.strip()
    if middle == "":
        return "\n"
    else:
        header = line.split(middle)[0]
        return header + middle + "\n"

def delete_blank(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    for i in xrange(len(lines)):
        line = lines[i]
        lines[i] = deal_line(line)

    with open(file_path, "w") as f:
        f.writelines(lines)

def scan(root_folder):
    for (root, folders, files) in os.walk(root_folder):
        for f in files:
            path = os.path.join(root, f)
            ext = os.path.splitext(path)[1]
            if ext in exts:
                delete_blank(path)

if __name__ == "__main__":
    scan(sys.argv[1])
