#!/usr/bin/env python3


import os, sys

file = open("pwd_list.txt", "r+", encoding = "utf-8")

file.seek(0, os.SEEK_END)

pos = file.tell() - 1

while pos > 0 and file.read(1) != "\n":
    pos -= 1
    file.seek(pos, os.SEEK_SET)

if pos > 0:
    file.seek(pos, os.SEEK_SET)
    file.truncate()

file.close()