import numpy as np
import read_file as rf

data_id = 11
tp = 'libfm'
pnp = '/home/fearofchou/data/KKBOX/libfm'+\
    '/tr_te_data_BS/split_by_month/long_term_playcount_mean'+\
    '/libfm_OUT_RLS/'
pred_fn = '*%d*.pred'%(data_id)

tnp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/*tar*%02d*.test'%(data_id)

#======================================================
#load file
pred_tar = rf.pred_read(pnp+pred_fn,tp,data_id)
true_tar = rf.true_read(tnp,data_id)
test_idx = rf.test_split(data_id,true_tar['log2p1'])
#======================================================


#======================================================
#RMSE
import KKBOX_RMSE as KR
RMSE_fn = KR.all_pred_RMSE(data_id,test_idx,pred_tar,true_tar)
#======================================================

#======================================================
#NDCG
N=10
fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/'
import KKBOX_NDCG as KN
NDCG_fn = KN.KKBOX_NDCG(fp,data_id,test_idx,pred_tar,N)
#======================================================
#======================================================
#write evul file
import out_write as OW
evul_me = 'NDCG@%d'%(N)
ofp = '/home/fearofchou/data/KKBOX/result/'
OW.out_format_1(pnp,data_id,tp,evul_me,NDCG_fn)
#======================================================
#======================================================
#write evul file
import out_write as OW
evul_me = 'RMSE'
ofp = '/home/fearofchou/data/KKBOX/result/'
OW.out_format_1(pnp,data_id,tp,evul_me,RMSE_fn)
#======================================================
#'''
