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

#translation code found through googleing http://stackoverflow.com/questions/19521905/translation-dna-to-protein

def translate_dna(sequence):

    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
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






reader = FASTAReader(sys.stdin)

translate = []
for sid, sequence in reader:
    translate_dna(sequence)
    translate.append(sequence)




