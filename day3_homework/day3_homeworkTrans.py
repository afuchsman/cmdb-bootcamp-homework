#!/usr/bin/env python


"""" - Extract the 100 longest assembled transcripts from your cufflinks output (transcripts.gtf) in FASTA format
 - Finding ORFS in these transcripts and print all ORFs found, translated to peptide sequence using the standard genetic code"""

"""/Users/cmdb/data/day1/cufflinks_out $ gtf_to_fasta ./transcripts.gtf /Users/cmdb/data/genomes/dmel-all-chromosome-r5.57.fasta transcripts_homework.fa"""


import sys
import csv
from fasta2 import FASTAReader
from sys import argv
#script, filename = argv
        

reader = FASTAReader(sys.stdin)

ref = []
for sid, sequence in reader:
    ref.append((len(sequence), sequence))

reader = FASTAReader(sys.stdin)
f = open("/Users/cmdb/data/day3/seqs.csv")


translate = []
for sid, sequence in reader:
    translate_dna(sequence)
    translate.append(sequence)


#translation code found through googleing http://stackoverflow.com/questions/19521905/translation-dna-to-protein

def translate_dna(sequence):

    codontable = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
    "TCT":"S", "TCC":"s", "TCA":"S", "TCG":"S",
    "TAT":"Y", "TAC":"Y", "TAA":"STOP", "TAG":"STOP",
    "TGT":"C", "TGC":"C", "TGA":"STOP", "TGG":"W",
    "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    
    
    proteinsequence = ''
    start = sequence.find('ATG')
    sequencestart = sequence[int(start):]
    stop = sequencestart.find('TAA')
    cds = str(sequencestart[:int(stop)+3])

    for n in range(0,len(cds),3):
        if cds[n:n+3] in codontable == True:
            proteinsequence += codontable[cds[n:n+3]]
            print proteinsequence
        sequence = ''


header = ''
sequence = ''
f = open("/Users/cmdb/data/day3/seqs.csv")
for line in f:
    #if line[0] == ">":
    if header != '':
        print header
        translate_dna(line)
        header = line.strip()
        sequence = ''
    else:
        sequence += line.strip()

print header 
translate_dna(line)











