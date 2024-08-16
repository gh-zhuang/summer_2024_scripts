#!/bin/bash
#SBATCH --job-name ct_r_corr
#SBATCH --get-user-env
#SBATCH --partition testivd
#SBATCH --mem 32G
#SBATCH --cpus-per-task 1

echo "$(date)"

python3 -m region_corr.py 

echo "$(date)"
