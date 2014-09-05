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

print longest_100_seq

#seq_sort > "longest_100_seq.fa" 

def ReverseComplement1(seq):
    seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
    return "".join([seq_dict[base] for base in reversed(seq)])   
#reverse complements from longest_100_seq

    
#ReverseComplement1 > "longest_100_reverse_comp.fa" 
#./100long_assem_transcr.py < /Users/cmdb/data/day1/SRR072893_thout/cufflinks_result/transcripts.fa | less 
# to show 100 longest transcripts