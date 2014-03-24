def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    for x in len(aTup):
        if x % 2 != 2:
            newTup = (aTup[x::], )
    return(newTup)
