#!/bin/bash

#SBATCH --job-name=sobursra
#SBATCH -c 8
#SBATCH --time=08:00:00
#SBATCH --mem=1gb

# Activate your virtual environment

mamba activate fastqdump

# Run the Python script

python3 << EOF
import subprocess

# samples correspond to Het_1, Het_2, Imm_1, Imm_2
sra_numbers = [
    "SRR2121685", "SRR2121686", "SRR2121687", "SRR2121688"
    ]

# this will download the .sra files to ~/ncbi/public/sra/ (will create directory if not present)
for sra_id in sra_numbers:
    print("Currently downloading: " + sra_id)
    prefetch = "prefetch " + sra_id
    print("The command used was: " + prefetch)
    subprocess.call(prefetch, shell=True)

# this will extract the .sra files from above into a folder named 'fastq'
for sra_id in sra_numbers:
    print("Generating fastq for: " + sra_id)
    fastq_dump = "fastq-dump --outdir fastq --gzip --skip-technical  --readids --read-filter pass --dumpbase --split-3 --clip ~/ncbi/public/sra/" + sra_id + ".sra"
    print("The command used was: " + fastq_dump)
    subprocess.call(fastq_dump, shell=True)
EOF
