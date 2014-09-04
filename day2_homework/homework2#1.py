#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

cufflinks_output = "/Users/cmdb//data/results/SRR072893_clout/genes.fpkm_tracking"
cufflinks_output2 = "/Users/cmdb//data/results/SRR072915_clout/genes.fpkm_tracking"

df = pd.read_table(cufflinks_output)
df2 = pd.read_table(cufflinks_output2)

#for SRR072893 male 
top = df.sort("FPKM", ascending=False) ["FPKM"] [0:5200]
middle = df.sort("FPKM", ascending=False) ["FPKM"] [5200:10400]
bottom = df.sort("FPKM", ascending=False)["FPKM"] [10400: ]

data_to_plot = [top, middle, bottom]   
   
# Create a figure instance
fig = plt.figure()
# Create the boxplot
plt.boxplot(data_to_plot)
# Save the figure
fig.savefig('box_male.png')

# for SRR072915 female
top2 = df2.sort("FPKM", ascending=False) ["FPKM"] [0:5200]
middle2 = df2.sort("FPKM", ascending=False) ["FPKM"] [5200:10400]
bottom2 = df2.sort("FPKM", ascending=False)["FPKM"] [10400: ]

data_to_plot2 = [top2, middle2, bottom2]   
   
# Create a figure instance
fig = plt.figure()
# Create the boxplot
plt.boxplot(data_to_plot2)
# Save the figure
fig.savefig('box_female.png')