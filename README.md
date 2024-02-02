# SRA_file_download


parallel-fastq-dump is a good options 

https://github.com/rvalieris/parallel-fastq-dump

Firs create a environment
```
mamba create -n fastqdump -c conda-forge -c bioconda parallel-fastq-dump
conda activate fastqdump
conda install parallel-fastq-dump 'sra-tools>=3.0.0'
parallel-fastq-dump --sra-id SRR7635124 --threads 4 --outdir out/ --split-files --gzip
```
