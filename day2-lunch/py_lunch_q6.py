#!/usr/bin/env python

number_alignments_sam = "/Users/cmdb/data/day2/accepted_hits.sam"

f = open(number_alignments_sam)

total = 0

n_al = 0
#chromosome = {}
#need a dictionary 
for line in f:
    fields = line.split("\t")
    #if fields[2] in chromosome:
    #    chromosome[fields[2]] = chromosome[fields[2]] + 1
    #else:
     #   chromosome[fields[2]] = 1
    total = total + int(fields[4])
    n_al = n_al + 1
#for i in chromosome:
        
print "\nAvg MAPQ score = %.2f" % (float(total)/n_al) 
#i, chromosome[i]

