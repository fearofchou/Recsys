from NDCG import *
import glob,sys
def RANK(True_rank,UIP,UIT,N):
    Pred_rank = {}
    T_NDCG = {}
    USER = 0
    for i in UIP.keys():
        if len(UIP[i])<=N:
            continue
        if len(np.unique(UIT[i]))==1:
            continue
        Pred_rank[i] = True_rank[i][np.argsort(UIP[i])][::-1][:N]
        if len(np.unique(Pred_rank[i]))==1:
            continue
        T_NDCG[i] = NDCG(Pred_rank[i])
        USER+=1
    return T_NDCG

def KKBOX_NDCG(fp,data_id,test_idx,pred_tar,N):
    #fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/'

    uid_fn= fp + 'rel_uid_%02d.test'%(data_id)
    sid_fn= fp + 'rel_sid_%02d.test'%(data_id)
    tar_fn= fp + 'rel_target_log2p1_%02d.test'%(data_id)

    with open(uid_fn) as f:
        uuid = np.array(map(int,f.readlines()))
    with open(sid_fn) as f:
        ssid = np.array(map(int,f.readlines()))
    with open(tar_fn) as f:
        ttar = np.array(map(float,f.readlines()))

    NDCG_result = {}
    for NHL in sorted(test_idx.keys()):
        uid = uuid[test_idx[NHL]]
        sid = ssid[test_idx[NHL]]
        tar = ttar[test_idx[NHL]]

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


        for fn in sorted(pred_tar.keys()):
            UIP = {}
            pre = np.array(pred_tar[fn])
            pre = pre[test_idx[NHL]]
            for idx,val in enumerate(uid):
                try:
                    UIP[val].append(pre[idx])
                except:
                    UIP[val] = [pre[idx]]

            T_NDCG = RANK(True_rank,UIP,UIT,N)
            try:
                NDCG_result[fn][NHL] = T_NDCG
            except:
                NDCG_result[fn] = {}
                NDCG_result[fn][NHL] = T_NDCG
    return NDCG_result

