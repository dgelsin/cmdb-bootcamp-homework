#!/usr/bin/env python

"""
Print sequence name, ratio of identifies, and ratio of gaps

"""

#import sys 

line = sys.stdin.readline()
#ratio_iden_gaps = sys.stdin.readratio_iden_gaps()
#ratio_gaps = sys.stdin.readratio_gaps()

#assert line.startswith(">")
#assert line.startswith("Query=")
#assert line.startswith("Ident")

#sid = line[1:].rstrip("\r\n")

sequences = []
#make a list
while True:
    line = sys.stdin.readline()
    #reads one line, can either get a header or sequence
    #if line.startswith("Query ="):
        #print line.strip(),
    if line.startswith("> NM"): 
        print line.strip("> "),
    if line.startswith(" Identities"):
        print "".join(line.replace(" Identities =", " ").replace("Gaps =", " ")
        #split two strings with .join
    #or line.startswith("Query=") or line.startswith("Ident"):
    if line == "":
        break 
    #if line starts with > aka a header, we stop and move to sequence
    else: 
        continue
        #what to get ride of the end space (black space) from the end of the sequence lines

