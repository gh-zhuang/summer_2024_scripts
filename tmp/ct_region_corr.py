import numpy as np
import pandas as pd
import pickle

with open('/screening/notebooks/zhuang/summer_2024/data/region_ids.pkl', 'rb') as f:
        region_ids = pickle.load(f)

with open('/screening/notebooks/zhuang/summer_2024/data/df_ldt.pkl', 'rb') as f:
        df_ldt = pickle.load(f)


for cancer_type in df_ldt.sample_group.unique():
    tmp = df_ldt.query('sample_group == @cancer_type').\
        loc[:,region_ids]
    for method in ["spearman","pearson"]:
        corr = tmp.corr(method = method)
        corr_triu = corr.values[np.triu_indices_from(corr, k=1)]
        file_name = '/screening/notebooks/zhuang/summer_2024/data/' + cancer_type + "_" + "corr_" + method[0:2] + ".pkl"
        
        with open(file_name, 'wb') as f:
            pickle.dump(corr_triu, f)
        print("save!")
