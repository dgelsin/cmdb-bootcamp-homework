#!/usr/bin/env python

number_alignments_sam = "/Users/cmdb/data/day2/accepted_hits.sam"

f = open(number_alignments_sam)

chromosome = {}
#need a dictionary 
for line in f:
    fields = line.split("\t")
    if fields[2] in chromosome:
        chromosome[fields[2]] = chromosome[fields[2]] + 1
    else:
        chromosome[fields[2]] = 1
    
for i in chromosome:
        
    print i, chromosome[i]

