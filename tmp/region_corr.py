#!/bin/bash
#SBATCH --job-name=region_corr
#SBATCH --get-user-env
#SBATCH --partition testivd                   
#SBATCH --cpus-per-task=1            
#SBATCH --mem 8G

import numpy as np
import pandas as pd
import pickle

with open('/screening/notebooks/zhuang/summer_2024/data/region_ids.pkl', 'rb') as f:
        region_ids = pickle.load(f)

with open('/screening/notebooks/zhuang/summer_2024/data/df_ldt.pkl', 'rb') as f:
        df_ldt = pickle.load(f)

region_corr_sp = df_ldt.loc[:,region_ids].corr(method = 'spearman')
region_corr_sp_triu = region_corr_sp.values[np.triu_indices_from(region_corr_sp, k=1)]

with open('/screening/notebooks/zhuang/summer_2024/data/region_corr_sp.pkl', 'wb') as f:
    pickle.dump(region_corr_sp_triu, f)

print("save!")

region_corr_pr = df_ldt.loc[:,region_ids].corr(method='pearson')
region_corr_pr_triu = region_corr_pr.values[np.triu_indices_from(region_corr_pr, k=1)]

with open('/screening/notebooks/zhuang/summer_2024/data/region_corr_pr.pkl', 'wb') as f:
    pickle.dump(region_corr_pr_triu, f)

print("save!")
