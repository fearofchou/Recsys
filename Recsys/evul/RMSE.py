import numpy as np

def RMSE(train,test):
    #return np.sqrt( ((train - test)**2).mean() )
    return (train - test)**2

