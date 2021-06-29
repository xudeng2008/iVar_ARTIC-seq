# iVar_ARTIC-seq
Using iVar analyze amplicon sequencing data

# Usage:
1. align_bwa.py
Run align_bwa.py to align paired-end amplicon reads to the reference genome
Parameters:

* `-fq` or `--fastq_dir`: path to directory containing fastq files
* `-fa` or `--fasta_dir`: path to directory containing genome fasta file
Example:
```
nohup python align_bwa.py -fq fastq_dir -fa fasta_dir &
```
