#!/usr/bin/env python

#7. Count number of reads that start their alignment on chromosome 2L between base 10000 and 20000 (inclusive)

SAM = "/Users/cmdb/data/day1/accepted_hits.sam"

f = open (SAM)

count = 0

for i, line in enumerate(f):
    fields = line.rstrip("\r\n").split("\t")
    if i > 17:    
        if fields[2] == "2L" and "10000" <= fields[3] <= "20000":
            count = count + 1
            
print count             


