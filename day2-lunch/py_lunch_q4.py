#!/usr/bin/env python

number_alignments_sam = "/Users/cmdb/data/day2/accepted_hits.sam"

f = open(number_alignments_sam)

for i, line in enumerate(f):
    fields = line.rstrip("\r\n").split("\t")
    if i > 0:
        print fields[2],

