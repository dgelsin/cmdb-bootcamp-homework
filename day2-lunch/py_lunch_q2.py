#!/usr/bin/env python

number_alignments_sam = "/Users/cmdb/data/day2/accepted_hits.sam"

f = open(number_alignments_sam)

n_al = 0
while True:
    line = f.readline()
    if "NM:i:0" in line:
        n_al = n_al + 1
    else: 
        if line == "":
            break
        
print "\nThere are " +str(n_al) + " alignments that are a perfect match"


     
     



