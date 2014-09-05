#!/usr/bin/env python

import pandas
import matplotlib.pyplot as plot
import statsmodels.api as sm

df = pandas.read_table("bedtools_nuc.txt") 

model = sm.formula.ols(formula="FPKM ~ GC", data=df)
#remember to change column heading no underscore
res = model.fit()
print res.summary()

plot.scatter(df["FPKM"], df["GC"])

plot.savefig("fpkm_vs_gc.png")

