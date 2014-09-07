#!/usr/bin/env python

import pandas as pd
metadata_output = "/Users/cmdb/cmdb-bootcamp-homework/day2-hw/samples.csv"
samples = pd.read_csv(metadata_output)

cufflinks_dir = "/Users/cmdb/data/results/"

for x in samples[ samples["sex"] == "female" ]["sample"]:
    current_df = pd.read_table ( cufflinks_dir + x + "_clout/genes.fpkm_tracking")
    print "Sxl abundance (FPKM) for " + x
    print current_df[ current_df["gene_short_name"] == "Sxl" ]["FPKM"]