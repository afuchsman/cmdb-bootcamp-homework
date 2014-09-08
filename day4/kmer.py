#!/usr/bin/env python
#19
"""
#calculates the CpG "%" for each transcript
"""

import sys
from fasta import FASTAReader

reader = FASTAReader(sys.stdin)

cpg_pct = []
for _, sequence in reader:    
    count = 0
    for i in range(len(sequence)):
        if sequence [i:i+2] == "GC" or sequence [i:i+2] == "CG":
            #print sequence [i:i+2]
            count += 1 
    #print count
    cpg = count / float(len(sequence))
    print cpg
    cpg_pct.append(cpg)

#print cpg_pct        
            

        