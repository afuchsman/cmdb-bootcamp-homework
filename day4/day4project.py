#!/usr/bin/env python

import sys 
import pandas
import scipy.stats
import matplotlib.pyplot as plot


f = open("/Users/cmdb/data/results/SRR072893_clout/transcripts.gtf")

trans_start = []
    
for line in f:
    fields = line.rstrip("\r\n").split()
    if fields [2] == "transcript":
        if fields [6] == "+":
            name = line.rstrip("\r\n").split()
            chrom = fields[0]
            start = (int(fields[3])-250)
            if start <= 0:
                start = 1
            end = (int(fields[3])+250)
            name1 = name[9]
            FPKM = fields[13][1:-2]
            trans_start.append((chrom, start, end, name1, FPKM))  
        if fields [6] == "-":
            name = line.rstrip("\r\n").split()
            chrom = fields[0]
            start = (int(fields[4])-250)
            if start <= 0:
                start = 1
            end = (int(fields[4])+250)
            name1 = name[9]
            FPKM = fields[13][1:-2]
            trans_start.append((chrom, start, end, name1, FPKM))  
    if fields [2] == "":
        break  
#print trans_start                

for chrom, start, end, name1, FPKM in trans_start:
    print chrom+"\t"+str(start)+"\t"+str(end)+"\t"+name1+"\t"+FPKM

#bedtools getfasta -fi test.fa -bed test.bed -fo test.fa.out


#bedtools getfasta [OPTIONS] -fi <input FASTA(dmel)> -bed <BED/GFF/VCF> -fo <output FASTA>