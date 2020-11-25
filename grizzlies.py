import pandas as pd

def from_dummies(df,dummy_vars,var_name='from_dummies'):
    
    """Convert dummy variables in a pandas.DataFrame back to a single 
    categorial variable.
    
    Parameters
    ----------
    df: pandas.DataFrame
        The data frame which contains the dummy variables.
    
    dummy_vars: list
        A list of the names of the dummy variables.
    
    var_name: str
        The name of the new categorial variable.
    
    Returns
    -------
    df: pandas.DataFrame
        A data frame where the dummy variables of interest are replaced
        with a single categorial variable.
        
    Notes
    -----
    This function will 'hopefully' be implemented in the pandas library. There's
    already a GitHub Issue on this problem:
    https://github.com/pandas-dev/pandas/issues/8745
    
    """
    dummies_stacked = df.loc[:,dummy_vars].stack()
    
    # get vectors with categories and coresponding indices
    categorial_var_indices = dummies_stacked[dummies_stacked!=0].index.get_level_values(0)
    categorial_var_categories = dummies_stacked[dummies_stacked!=0].index.get_level_values(1)

    categorial_var = pd.Series(pd.Categorical(categorial_var_categories),
                           index=categorial_var_indices)
    
    df = df.drop(dummy_vars,axis=1)
    df[var_name] = categorial_var
    
    return df
    
    
    
