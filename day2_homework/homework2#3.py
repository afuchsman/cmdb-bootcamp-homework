#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

cufflinks_output10 = "/Users/cmdb//data/results/SRR072905_clout/genes.fpkm_tracking"
cufflinks_output11 = "/Users/cmdb//data/results/SRR072906_clout/genes.fpkm_tracking"
cufflinks_output12 = "/Users/cmdb//data/results/SRR072907_clout/genes.fpkm_tracking"
cufflinks_output13 = "/Users/cmdb//data/results/SRR072908_clout/genes.fpkm_tracking"
cufflinks_output14A = "/Users/cmdb//data/results/SRR072909_clout/genes.fpkm_tracking"
cufflinks_output14B = "/Users/cmdb//data/results/SRR072911_clout/genes.fpkm_tracking"
cufflinks_output14C = "/Users/cmdb//data/results/SRR072913_clout/genes.fpkm_tracking"
cufflinks_output14D = "/Users/cmdb//data/results/SRR072915_clout/genes.fpkm_tracking"

#file_dir = "/Users/data"
#file_ext = "_clout/gene.fpkm_tracking"
#values = [905, 906, 908]
#for i in values:
#    full_path = file_dir + str(i) + file_ext


all_files = [cufflinks_output10, cufflinks_output11, cufflinks_output12, cufflinks_output13, cufflinks_output14A, cufflinks_output14B, cufflinks_output14C, cufflinks_output14D]

FPKM_level = []
for i in all_files:
    f = open (i)
    while True:
        line = f.readline()
        if "Sxl" in line:
            #print line
            fields = line.rstrip("\r\n").split("\t")
            FPKM_level.append(fields[9])
            break
#print FPKM_level


plt.figure()
plt.plot(FPKM_level)
plt.savefig("FPKM_levels.png")
        
