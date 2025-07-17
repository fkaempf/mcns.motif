#!/bin/bash

#SBATCH --job-name=motif_extract
#SBATCH -c 112
#SBATCH --mem=754G
#SBATCH --time=72:00:00

/lmb/home/fkampf/miniconda3/bin/jupyter nbconvert --execute --to notebook --inplace subfig_a.ipynb
