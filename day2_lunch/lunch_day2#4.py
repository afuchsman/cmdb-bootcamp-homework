#!/usr/bin/env python

SAM = "/Users/cmdb/data/day1/accepted_hits.sam"

f = open (SAM)

Chrom_location = []        
for i, line in enumerate(f):
    fields = line.rstrip("\r\n").split("\t")
    if i > 17:
        Chrom_location.append( fields[2])
print Chrom_location
#accumulate the column which chromosome read aligns too, but not the header (i>17)