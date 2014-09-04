#!/usr/bin/env python


import matplotlib.pyplot as plt

file_dir = "/Users/cmdb//data/results/"
file_ext = "_clout/genes.fpkm_tracking"
samples = ["SRR072905", "SRR072906", "SRR072907", "SRR072908", "SRR072909", "SRR072911", "SRR072913", "SRR072915"]

FPKM_level = []
for i in samples:
    full_path = file_dir + str(i) + file_ext
    f = open (full_path)
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
        
        