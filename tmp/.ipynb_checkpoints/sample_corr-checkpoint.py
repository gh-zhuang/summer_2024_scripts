#!/usr/bin/env python3
#SBATCH --job-name=sample_corr
#SBATCH --get-user-env
#SBATCH --partition testivd                   
#SBATCH --cpus-per-task=1            
#SBATCH --mem 8G  

import numpy as np
import pandas as pd
import pickle

with open('../data/region_ids.pkl', 'rb') as f:
        region_ids = pickle.load(f)

with open('../data/df_ldt.pkl', 'rb') as f:
        df_ldt = pickle.load(f)

sample_corr_sp = df_ldt.loc[:,region_ids].T.corr(method = 'spearman')
sample_corr_sp_triu = sample_corr_sp.values[np.triu_indices_from(sample_corr_sp, k=1)]

with open('/screening/notebooks/zhuang/summer_2024/data/sample_corr_sp.pkl', 'wb') as f:
    pickle.dump(sample_corr_sp_triu, f)

print("save!")

sample_corr_pr = df_ldt.loc[:,region_ids].T.corr(method='pearson')
sample_corr_pr_triu = sample_corr_pr.values[np.triu_indices_from(sample_corr_pr, k=1)]

with open('/screening/notebooks/zhuang/summer_2024/data/sample_corr_pr.pkl', 'wb') as f:
    pickle.dump(sample_corr_pr_triu, f)

print("save!")
