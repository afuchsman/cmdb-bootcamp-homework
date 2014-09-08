#!/usr/bin/env python
#19
"""
#calculates the CpG "%" for each transcript
"""

import sys
from fasta import FASTAReader
import numpy as np
from numpy import log10
import pandas
import matplotlib.pyplot as plot
import statsmodels.api as sm
import pylab

f = open("/Users/cmdb/cmdb-bootcamp-homework/day4/bedtools_nuc copy.txt")
df = pandas.read_table("bedtools_nuc copy.txt") 
#copy bedtools_nuc2.text to make edits 
y = open("/Users/cmdb/cmdb-bootcamp-homework/day4/CpG_per.txt")

#replace CG with CpC for graphing
for line in f:
    fields = line.rstrip("\r\n").split()
    #print "ok"
    #if line == "GC":
    GC = fields[6]
    #print GC
    for GC_line in GC:
        new_line = y.readline()
        #GC_line = new_line
        str.replace(GC, GC_line, new_line)
#cannot rewrite the CG in the bedtools file to CpG so that I can easily graph the CpG with the CG setting from before.         
        if GC_line == "":
            break

#says GC but replacing with CpG
model = sm.formula.ols(formula="FPKM ~ GC", data=df)
#remember to change column heading no underscore
res = model.fit()
print res.summary()

x= df["FPKM"]
y = df["GC"]
m, b =np.polyfit(x,y,1)
plot.plot(x,y, ".")
plot.plot(x, m*x + b, "-")

plot.savefig("fpkm_vs_CpG_lin.png")

#plot.scatter(log10(df["FPKM"]), df["GC"])
#plot.savefig("fpkm_vs_gc.png")
#for plot without regression line 



