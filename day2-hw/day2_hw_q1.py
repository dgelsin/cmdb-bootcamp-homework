#!/usr/bin/env python

import pandas as pd

cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"

df = pd.read_table(cufflinks_output)

import matplotlib.pyplot as plt

cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
df2 = pd.read_table(cufflinks_output2)

top_middle_bottom = pd.DataFrame({"bottom": df["FPKM"][0:5200], "middle": df["FPKM"][5201:10400], "top": df["FPKM"][10401:15602], "bottom2": df2["FPKM"][0:5200], "middle2": df2["FPKM"][5201:10400], "top2": df2["FPKM"][10401:15602]})
#restricted definitions for each variable

plt.figure()
top_middle_bottom.boxplot()
plt.ylabel("FPKM")
plt.xlabel("1/3 Percentiles")
#axis labels
plt.axis([0, 7, -10, 100])
# x1, x2, y1, y2
plt.savefig("boxplot.png")
