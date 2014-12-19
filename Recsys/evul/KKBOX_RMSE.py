import numpy as np
import glob
import RMSE

def all_pred_RMSE(data_id,test_idx,pred_tar,true_tar):
    RMSE_fn ={}
    for i in sorted(pred_tar.keys()):
        if '_log2p1' in i:
            k='log2p1'
        elif '5Ilog2p1' in i:
            k='5Ilog2p1'
        elif '5I' in i:
            k='5I'
        else:
            k='%02d.test'%(data_id)

        RMSE_fn[i] = {}
        for j in test_idx.keys():
            NHL = test_idx[j]

            RMSE_val = RMSE.RMSE(true_tar[k][NHL],np.array(pred_tar[i])[NHL])
            RMSE_fn[i][j] = RMSE_val
    return RMSE_fn

