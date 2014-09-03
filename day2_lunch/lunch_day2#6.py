#!/usr/bin/env python

SAM = "/Users/cmdb/data/day1/accepted_hits.sam"

f = open (SAM)

total_reads = 0
x = 0

       
for i, line in enumerate(f):
    fields = line.rstrip("\r\n").split("\t")
    if i > 17:
        x = x + int(fields[4])
        total_reads = total_reads + 1
    
print "Average MAPQ score: ", x/total_reads 
