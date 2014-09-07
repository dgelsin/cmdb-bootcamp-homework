#!/usr/bin/env python


import pandas

base = "Users/cmdb/cmdb-bootcamp-homework/day2-hw/"

df = pandas.read_csv("samples.csv")

all_samples = []

for sample in df["sample"]:
	all_samples[sample] = pandas.read_table(base + sample + "_clout/" + "genes.fpkm_tracking") ["FPKM"]
	
df = pandas.DataFrame(all_samples)

print df