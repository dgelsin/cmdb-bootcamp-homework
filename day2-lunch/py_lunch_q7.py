#!/usr/bin/env python

number_alignments_sam = "/Users/cmdb/data/day2/accepted_hits.sam"

f = open(number_alignments_sam)

bt_10000_20000 = 0
#total = 0

#n_al = 0
#chromosome = {}
#need a dictionary 
for line in f:
    fields = line.split("\t")
    if fields[2] == "2L" and int(fields[3]) >= 10000 and int(fields[3]) <= 20000: 
        #chromosome:
        bt_10000_20000 = bt_10000_20000 + 1
        
    #    chromosome[fields[2]] = chromosome[fields[2]] + 1
    #else:
     #   chromosome[fields[2]] = 1
    #total = total + int(fields[4])
    #n_al = n_al + 1
#for i in chromosome:
        
print str(bt_10000_20000) + " reads between base 10000 & 20000"
#i, chromosome[i]

