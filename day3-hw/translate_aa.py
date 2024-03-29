#!/usr/bin/env python

import sys

table = {"TTT ": "F ", "TTC ": "F ", "TTA ": "L ", "TTG ": "L ", "TCT ": "S ",
         "TCC ": "s ", "TCA ": "S ", "TCG ": "S ", "TAT ": "Y ", "TAC ": "Y ", 
         "TAA ": "STOP ", "TAG ": "STOP ", "TGT ": "C ", "TGC ": "C ", "TGA ":
         "STOP ", "TGG ": "W ", "CTT ": "L ", "CTC ": "L ", "CTA ": "L ", "CTG ":
         "L ", "CCT ": "P ", "CCC ": "P ", "CCA ": "P ", "CCG ": "P ", "CAT ": "H ",
         "CAC ": "H ", "CAA ": "Q ", "CAG ": "Q ", "CGT ": "R ", "CGC ": "R ", "CGA ":
         "R ", "CGG ": "R ", "ATT ": "I ", "ATC ": "I ", "ATA ": "I ", "ATG ": "M ",
         "ACT ": "T ", "ACC ": "T ", "ACA ": "T ", "ACG ": "T ", "AAT ": "N ", "AAC ": "N ", "AAA ": "K ", "AAG ": "K ", "AGT ": "S ", "AGC ": "S ", "AGA ": "R ", "AGG ": "R ", "GTT ": "V ", "GTC ": "V ", "GTA ": "V ", "GTG ": "V ", "GCT ": "A ", "GCC ": "A ", "GCA ": "A ", "GCG ": "A ", "GAT ": "D ", "GAC ": "D ", "GAA ": "E ", "GAG ": "E ", "GGT ": "G ", "GGC ": "G ", "GGA ": "G ", "GGG ": "G "}

#Remove any spaces from keys
new_table = {}
for key, value in table.iteritems():
    new_table[key.strip()] = value.strip()    

to_translate = sys.argv[1]

start = to_translate.find("ATG")

# accumulate AA here
result = ""
for i in range(start, len(to_translate), 3):
    #translate codon to amino acid
    codon = new_table[to_translate[i:i+3]]       
    # Stop if we hit a stop codon
    if codon == "STOP":
        break
    result += codon
   
        
print result