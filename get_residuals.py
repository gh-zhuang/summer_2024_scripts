import numpy as np
import pandas as pd
import statsmodels.formula.api as sm

def get_residuals(df,
                  regions,
                  phenotypes):

    '''
    Obtain residuals

    Parameters:
    -----
    df : {pandas.DataFrame}
        a n x p data frame

    regions : list
        a list columns that represents the regions

    phenotypes : list
        a list of phenotypes of interest

    Return:
    -----
    residuals : {pandas.DataFrame}
    '''

    assert all([i in df.columns for i in regions]), "Invalid 'regions' "
    assert all([i in df.columns for i in phenotypes]), "Invalid 'phenotypes' "

    if not isinstance(regions, list):
        raise TypeError(f" 'regions' should be a 'list' object")

    if not isinstance(phenotypes, list):
        raise TypeError(f" 'phenotypes' should be a 'list' object")

    ## filter
    df = df.loc[:,regions + phenotypes]
    residuals = pd.DataFrame()

    for region in regions:
        res = _ols_residuals(df,
                             y = region,
                             X = phenotypes)

        residuals = pd.concat([residuals, res], axis=1)

    return residuals

def _ols_residuals(df, y, X):
     
    model = sm.ols(formula=f"{y}~{'+'.join(X)}",
                   data=df.loc[:,[y]+X]).fit()
    residuals = model.resid.to_frame(y)

    return residuals
