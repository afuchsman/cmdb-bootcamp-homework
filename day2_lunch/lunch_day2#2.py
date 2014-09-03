#!/usr/bin/env python

SAM = "/Users/cmdb/data/day1/accepted_hits.sam"

f = open (SAM)

ln = 0
for i in f:
    if "MD:Z:40" in i:
        ln = ln + 1
print ln