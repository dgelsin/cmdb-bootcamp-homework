#!/usr/bin/env python

number_alignments_sam = "/Users/cmdb/data/day2/accepted_hits.sam"

f = open(number_alignments_sam)

for line in f:
    fields = line.split("\t")
    #if line > 0:
    print fields[2]

