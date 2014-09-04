#!/usr/bin/env python

"""
For each alignment in the blast output, print the sequence name, ratio of identifies, and ratio of gaps
"""

import sys

while True:
    line = sys.stdin.readline()
    if line.startswith("Query="):
        fly_name1 = line.rstrip("\r\n").split(" ")
        fly_name = fly_name1[2]
    if line.startswith(">"):
        hum_name1 = line[1:].rstrip("\r\n").split(" ")
        hum_name = hum_name1[1]
    if line.startswith(" Identities"):
        info = line[1:].rstrip("\r\n").split(" ")
        ident = info[2]
        gaps = info[6]
        print fly_name, hum_name, ident, gaps
    if line == "":
        break        
            