#!/usr/bin/env python


import pandas as pd
import csv


m10_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
m11_output = "/Users/cmdb/data/results/SRR072894_clout/genes.fpkm_tracking"
m12_output = "/Users/cmdb/data/results/SRR072895_clout/genes.fpkm_tracking"
m13_output = "/Users/cmdb/data/results/SRR072896_clout/genes.fpkm_tracking"
m14a_output = "/Users/cmdb/data/results/SRR072897_clout/genes.fpkm_tracking"
m14b_output = "/Users/cmdb/data/results/SRR072899_clout/genes.fpkm_tracking"
m14c_output = "/Users/cmdb/data/results/SRR072901_clout/genes.fpkm_tracking"
m14d_output = "/Users/cmdb/data/results/SRR072903_clout/genes.fpkm_tracking"

f10_output = "/Users/cmdb/data/results/SRR072905_clout/genes.fpkm_tracking"
f11_output = "/Users/cmdb/data/results/SRR072906_clout/genes.fpkm_tracking"
f12_output = "/Users/cmdb/data/results/SRR072907_clout/genes.fpkm_tracking"
f13_output = "/Users/cmdb/data/results/SRR072908_clout/genes.fpkm_tracking"
f14a_output = "/Users/cmdb/data/results/SRR072909_clout/genes.fpkm_tracking"
f14b_output = "/Users/cmdb/data/results/SRR072911_clout/genes.fpkm_tracking"
f14c_output = "/Users/cmdb/data/results/SRR072913_clout/genes.fpkm_tracking"
f14d_output = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
#used terminal to find pathway


df_f10 = pd.read_table(f10_output)
df_f11 = pd.read_table(f11_output)
df_f12 = pd.read_table(f12_output)
df_f13 = pd.read_table(f13_output)
df_f14a = pd.read_table(f14a_output)
df_f14b = pd.read_table(f14b_output)
df_f14c = pd.read_table(f14c_output)
df_f14d = pd.read_table(f14d_output)


total = []

total = []
total.append(m10_output) 
total.append(m11_output)
total.append(m12_output) 
total.append(m13_output) 
total.append(m14a_output) 
total.append(m14b_output) 
total.append(m14c_output) 
total.append(m14d_output) 
total.append(f10_output) 
total.append(f11_output) 
total.append(f12_output) 
total.append(f13_output) 
total.append(f14a_output) 
total.append(f14b_output) 
total.append(f14c_output) 
total.append(f14d_output)
#get error Traceback (most recent call last): File "./day2_hw_q2.py", line 43, in <module> for i, in total: ValueError: too many values to unpack, not sure what to do
 
#open files


#Slx_file_list9 = df_f10["FPKM"].str.contains("Sxl")
#Slx_file_list10 = df_f11["FPKM"].str.contains("Sxl")
#Slx_file_list11 = df_f12["FPKM"].str.contains("Sxl")
#Slx_file_list12 = df_f13["FPKM"].str.contains("Sxl")
#Slx_file_list13 = df_f14a["FPKM"].str.contains("Sxl")
#Slx_file_list14 = df_f14b["FPKM"].str.contains("Sxl")
#Slx_file_list15 = df_f14c["FPKM"].str.contains("Sxl")
#Slx_file_list16 = df_f14d["FPKM"].str.contains("Sxl")

deeper_list = []
for i in total:
    with open (i) as total:
        for row in total:
            if "Sxl" in row:
                #row = row.strip()
                deeper_list.append(row)
                
deepest_list = []


print deeper_list 

#for i, in total:
#    f = open (i)
#    fields = line.rstrip("\r\n").split("\t")
#    if "Slx" in line:
#        Slx_file_list.append(fields[9])

#print sorted(Slx_file_list)

Slx_file_list = []
for i, in total:
    f = open (i)
    fields = line.rstrip("\r\n").split("\t")
    if "Slx" in line:
        Slx_file_list.append(fields[9])

print sorted(Slx_file_list)

