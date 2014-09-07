#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata_output = "/Users/cmdb/cmdb-bootcamp-homework/day2-hw/samples.csv"

samples = pd.read_csv(metadata_output)

samples = []

for x in samples[ samples["sex"] == "female" ]["sample"]:
    # get TypeError: list indices must be integers, not str hmmm
    current_df = pd.read_table ( cufflinks_dir + x + "_clout/genes.fpkm_tracking")
    Sxl.append( current_df[ current_df["gene_short_name"] =="Sxl" ]["FPKM"] )
    
plt.figure ()
plt.plot(metadata_output)
plt.savefig("plot_fexpression.png")

#samples_file = "/Users/cmdb/data/day2/samples.csv"
