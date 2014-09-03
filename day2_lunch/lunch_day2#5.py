#!/usr/bin/env python

SAM = "/Users/cmdb/data/day1/accepted_hits.sam"

f = open (SAM)


C_2L = 0
C_2R = 0
C_3L = 0
C_3R = 0
C_4 = 0
X = 0

chrom = (C_2L, C_2R, C_3L, C_3R, C_4, X)
     
for i, line in enumerate(f):
    fields = line.rstrip("\r\n").split("\t")
    if i > 17:    
        if fields[2] = "2L":
            C_2L = C_2L + 1
        if fields[2] = "2R":
            C_2R = C_2R + 1
        if fields[2] = "3L":
            C_3L = C_3L + 1  
        if fields[2] = "3R":
            C_3R = C_3R + 1
        if fields[2] = "4":
            C_4 = C_4 + 1 
        if fields[2] = "X":
            C_X = C_X + 1                       
print Chrom_location
#accumulate the column which chromosome read aligns too, but not the header (i>17)