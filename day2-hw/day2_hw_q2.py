#!/usr/bin/env python

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

Slx_file_list = []
for i, in total:
    f = open (i)
    fields = line.rstrip("\r\n").split("\t")
    if "Slx" in line:
        Slx_file_list.append(fields[9])

print sorted(Slx_file_list)