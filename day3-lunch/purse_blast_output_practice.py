#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it.
"""

from fasta import FASTAReader
import sys
        
reader = FASTAReader(sys.stdin)        
for sid, sequence, in reader:
    #taking return value and give it to reader.next()
    print sequence #, sid
    