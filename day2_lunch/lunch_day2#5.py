#!/usr/bin/env python

SAM = "/Users/cmdb/data/day1/accepted_hits.sam"

f = open (SAM)


C_2L = 0
C_2R = 0
C_3L = 0
C_3R = 0
C_4 = 0
C_X = 0

     
for i, line in enumerate(f):
    fields = line.rstrip("\r\n").split("\t")
    if i > 17:    
        if fields[2] == "2L":
            C_2L = C_2L + 1
        if fields[2] == "2R":
            C_2R = C_2R + 1
        if fields[2] == "3L":
            C_3L = C_3L + 1  
        if fields[2] == "3R":
            C_3R = C_3R + 1
        if fields[2] == "4":
            C_4 = C_4 + 1 
        if fields[2] == "X":
            C_X = C_X + 1  
print "Chromosome 2L: " + str(C_2L)
print "Chromosome 2R: " + str(C_2R)
print "Chromosome 3L: " + str(C_3L)
print "Chromosome 3R: " + str(C_3R)
print "Chromosome 4: " + str(C_4)
print "Chromosome X: " + str(C_X)
#Calculate how many alignments are on chromosome 2L 2R 3L 3R 4 X 