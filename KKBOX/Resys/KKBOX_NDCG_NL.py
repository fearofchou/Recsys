from NDCG import *
import glob
import sys
sys.path.append('/home/fearofchou/code/KKBOX/stats')
from stats import *

def RANK(True_rank,UIP,UIT):
    Pred_rank = {}
    T_NDCG = []
    for i in True_rank.keys():
        if len(UIP[i])<5:
            continue
        if len(np.unique(UIT[i]))==1:
            continue
        Pred_rank[i] = True_rank[i][np.argsort(UIP[i])][::-1]
        T_NDCG.append( NDCG(Pred_rank[i]) )
        #T_NDCG[i] =  NDCG(Pred_rank[i])
    print np.mean(T_NDCG)
    return T_NDCG

data_id = 11
pred_fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/'
pred_fn = 'ID_%02d*'%(data_id)

uid_fn= pred_fp + 'rel_uid_%02d.test'%(data_id)
sid_fn= pred_fp + 'rel_sid_%02d.test'%(data_id)
sid_fnt= pred_fp + 'rel_sid_%02d.train'%(data_id)
tar_fn= pred_fp + 'rel_target_%02d.test'%(data_id)
fl = glob.glob(pred_fp + pred_fn)

with open(uid_fn) as f:
    uid = np.array(f.readlines()).astype('int')
with open(sid_fn) as f:
    sid = np.array(f.readlines()).astype('int')
with open(sid_fnt) as f:
    sidt = np.array(f.readlines()).astype('int')
with open(tar_fn) as f:
    tar = np.array(f.readlines()).astype('int')

NL_idx,HL_idx,NL_sid = find_never_listen_idx(sid,sidt)
#NL_idx =HL_idx
sid = sid[NL_idx]
uid = uid[NL_idx]
tar = tar[NL_idx]

UIS= {}
UIT= {}
UIP= {}

for idx,val in enumerate(uid):
    try:
        UIS[val].append(sid[idx])
    except:
        UIS[val] = [sid[idx]]
    try:
        UIT[val].append(tar[idx])
    except:
        UIT[val] = [tar[idx]]

True_rank ={}
for i in UIT.keys():
    un_pl = np.unique(UIT[i])
    rank = []
    for j in UIT[i]:
        rank.append(np.where(un_pl==j)[0][0])
    True_rank[i] = np.array(rank)


for fn in fl:
    UIP = {}
    with open(fn) as f:
        pre = np.array(f.readlines()).astype(float)
    pre = pre[NL_idx]
    for idx,val in enumerate(uid):
        try:
            UIP[val].append(pre[idx])
        except:
            UIP[val] = [pre[idx]]
    print fn
    T_NDCG = RANK(True_rank,UIP,UIT)

