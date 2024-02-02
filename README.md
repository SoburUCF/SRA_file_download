# SRA_file_download


parallel-fastq-dump is a good option 

Details steps are in the link:
https://github.com/rvalieris/parallel-fastq-dump

First, create an environment.
```
mamba create -n fastqdump -c conda-forge -c bioconda parallel-fastq-dump
conda activate fastqdump
conda install parallel-fastq-dump 'sra-tools>=3.0.0'
```

Then run the code with your SRA ID, Here output is the directory where all the files will be downloaded,
--split-files, if they are pair end read, will be separated 
--gzip convert them in gzip file

```
parallel-fastq-dump --sra-id SRR7635124 --threads 4 --outdir output/ --split-files --gzip
```
