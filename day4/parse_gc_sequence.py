#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it.
"""
import sys

from fasta import FASTAReader

        
reader = FASTAReader(sys.stdin)        
all_seqs = []
for sid, sequence in reader:
    #taking return value and give it to reader.next()
    #print sequence #, sid
    all_seqs.append(sequence)

seq_sort = sorted(all_seqs, key = len, reverse = True)

longest_100_seq = seq_sort[0:100]

print seq_sort 