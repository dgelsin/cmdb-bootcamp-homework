#!/usr/bin/env python

import pandas

df_plus = pandas.read_table("/Users/cmdb/data/day4/transcrips_+_only.csv")

df_minus = pandas.read_table("/Users/cmdb/data/day4/transcrips_-_only.csv")

start_plus = df_plus[4]
start_minus = df_minus[5]

chrom_plus = df_plus[1]
chrom_minus = df_minus[1]

print df_plus
print df_minus



#awk '$3 == "transcript"' transcripts.gtf | grep "+" > transcrips_+_only.csv
#awk '$3 == "transcript"' transcripts.gtf | grep "+" > transcrips_-_only.csv