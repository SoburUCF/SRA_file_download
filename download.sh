#!/bin/bash
#SBATCH -J ecolipop
#SBATCH -o ecolipop-%j.out
#SBATCH -e ecolipop-%j.err
#SBATCH -N 1 
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=4
#SBATCH -t 24:00:00
#SBATCH --mem=16G

SRA_IDS_FILE="sra_ids_1-20.txt"

while read -r ID; do
    parallel-fastq-dump --sra-id $ID --threads 8 --outdir seq_fastq2/ --split-files --gzip
done < "$SRA_IDS_FILE"
