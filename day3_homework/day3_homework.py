#!/usr/bin/env python


"""" - Extract the 100 longest assembled transcripts from your cufflinks output (transcripts.gtf) in FASTA format
 - Finding ORFS in these transcripts and print all ORFs found, translated to peptide sequence using the standard genetic code"""

"""/Users/cmdb/data/day1/cufflinks_out $ gtf_to_fasta ./transcripts.gtf /Users/cmdb/data/genomes/dmel-all-chromosome-r5.57.fasta transcripts_homework.fa"""


import sys
import csv
from fasta import FASTAReader
        
        
reader = FASTAReader(sys.stdin)

ref = []
for sid, sequence in reader:
    ref.append((len(sequence), sequence))
    
#print sorted(ref, reverse=True)[0:100]
ref2 = []
ref2 = sorted(ref, reverse=True)[0:100]
#print ref2

with open('transcripts_100.csv', 'wb') as result:
    writer = csv.writer(result, dialect='excel')
    writer.writerows(ref2)


transcripts = "/Users/cmdb/data/day3/transcripts_100.csv" 
    
f = open(transcripts)
print "open"
file = []
while True:
    line = f.readline()
    seq = line.rstrip("\r\n").split(",")
    seqs = seq[1]
    file.append(seq[1])

    #for line in seqs:
    #    line = line.readline()
    #    if line.startswith("ATG"):
    #        print "ATG"
    if line == "":
        break
#with open('seqs.csv', 'wb') as result:
#    writer = csv.writer(result, dialect='excel')
#    writer.writerows(file)        



#prints reverse complement             
def revcompl2( x ):
    return ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])
print revcompl2(x)    

revcompl2(file)        

        
