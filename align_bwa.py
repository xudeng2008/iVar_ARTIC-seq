#!/usr/bin/python3

import os
import sys

params = sys.argv #input parameters

fastq_dir = None # path to directory containing amplicon fastq files
fasta_dir = None # path to directory containing genome fasta file

for i in range(len(params)-1): #loop through parameters
    if params[i] == '-fq' or params[i] == '--fastq_dir': #if parameter is amplicon fastq directory
        fastq_dir = params[i + 1]
    elif params[i] == '-fa' or params[i] == '--fasta_dir': #if parameter is genome index
        fasta_dir = params[i+1]
    

if fastq_dir == None or fasta_dir == None:
    print('Error: Invalid input parameters. \nSet amplicon fastq directory with -f or --fastq_dir.\nSet path to directory containing genome fasta file with -fa or --fasta_dir.')

else:

    for file in os.listdir(str(fastq_dir)): #loop through files in data directory
        if file.endswith('_R1_001.fastq.gz'): #if file is first read in pair
            base = file.split('_R1_001.fastq.gz')[0] #get basename of file
            r1 = str(fastq_dir) + str(base) + '_R1_001.fastq.gz' #path to read 1
            r2 = str(fastq_dir) + str(base) + '_R2_001.fastq.gz' #path to read 2
            outname = base.split('/')[-1] #get name of file
            cmd = 'bwa mem -t 4 ' + str(fasta_dir) + ' ' + r1 + ' ' + r2 + ' | samtools view -b -F 4 -F 2048 | samtools sort -o ' + outname + '.sorted.bam'   # BWA command
            print('Aligning reads with BWA')
            print(cmd)
            os.system(cmd)