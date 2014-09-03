#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
#

echo "There are around 6 mistakes"

ONE="893"
TWO="903"
THREE="905"
FOUR="915"

FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1
SAMPLE_PREFIX="SRR072"

GENOME_DIR=/Users/cmdb/data/genomes
INDEX_DIR=/dmel5_out 
ANNOTATION=dmel-all-r5.57
CUFFLINKS_RES=/accepted_hits.bam

CORES=4

for i in $ONE $TWO $THREE $FOUR
do
  echo fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  echo tophat -p $CORES -G $OUTPUT_DIR/$ANNOTATION.gff -o $OUTPUT_DIR/$INDEX_DIR --no-novel-juncs --segment-length 20 $GENOME_DIR/$ANNOTATION $FASTQ_DIR/$SAMPLE_PREFIX$i
  #not sure if $ANNOTATION will be right because .gff at the end
  #removed .gff in $ANNOTATION variable
  echo cufflinks -p $CORES -G $OUTPUT_DIR/$ANNOTATION -o $OUTPUT_DIR/fastq.gz -o $OUTPUT_DIR/$INDEX_DIR $OUTPUT_DIR/$INDEX_DIR/$SAMPLE_PREFIX$i/$CUFFLINKS_RES
done

#no errors