import numpy as np
import pandas as pd
import statsmodels.formula.api as sm

def ols_wrapper(df, y, X):
    
    '''
    Perform OLS

    Parameters:
    -----
    df : {pandas.DataFrame}
        a n x p data frame

    y : str
        the column that represents the dependent variable

    X : list
        a list of columns that represents the independent variables

    Return:
    -----
    res : dictionary
        a dictionary containings keys of ['r2','adj_r2','coefficient','residuals']

    '''
    assert y in df.columns, "Invalid 'y' "
    assert all([i in df.columns for i in X]), "Invalid 'X' "

    if not isinstance(X, list):
        raise TypeError(f" 'X' should be a 'list' object")
    
    if not isinstance(y, str):
        raise TypeError(f" 'X' should be a 'str' object")

    res = {}
    model = sm.ols(formula=f"{y}~{'+'.join(X)}",
                   data=df.loc[:,[y]+X]).fit()

    res['r2'] = model.rsquared
    res['r2_adj'] = model.rsquared_adj
    res['coefficient'] = pd.DataFrame("coefficient":model.params,
                                      "pvalue":model.pvalues})
    
    res['residuals'] = model.resid.to_frame(y)

    return res
    
