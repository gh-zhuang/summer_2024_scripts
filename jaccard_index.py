def jaccard_index(x,y):

    '''
    Compute the Jaccard index between two sets

    Parameters:
    -----
    x : set
    y : set

    Return
    -----
    jaccard_index : float

    '''
    intersection = x.intersection(y)
    union = x.union(y)
    jaccard_index = intersection/union

    return jaccard_index
    