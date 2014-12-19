import numpy as np
import time,glob,os
from collections import Counter

def find_never_listen_song_id(target_sid, train_sid):
    C_tar_sid = Counter(target_sid)
    C_tra_sid = Counter(train_sid)
    return set(C_tar_sid.keys()).difference(C_tra_sid)

def find_never_listen_idx(target_sid, train_sid):
    NL_sid = find_never_listen_song_id(target_sid,train_sid)

    #sid to idx
    sid_idx = {}
    for idx,val in enumerate(target_sid):
        try:
            sid_idx[val].append(idx)
        except:
            sid_idx[val] = [idx]

    Total_NL_sid_idx = []
    for sid in NL_sid:
        Total_NL_sid_idx.extend(sid_idx[sid])
    NL_idx = np.sort(Total_NL_sid_idx)
    HL_idx = np.array( list(set(range(len(target_sid))).difference(NL_idx)) )
    return NL_idx,HL_idx,np.array(list(NL_sid))

data_id = 2
us = ['uid','sid']
ifp  = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/'
ofp = '/home/fearofchou/data/KKBOX/stats/NL_usid/'
for i in us:
    fn = 'rel_%s_%02d.train'%(i,data_id)
    with open(ifp+fn) as f:
        train = np.array(f.readlines()).astype(int)
    fn = 'rel_%s_%02d.test'%(i,data_id)
    with open(ifp+fn) as f:
        test = np.array(f.readlines()).astype(int)

    NL_idx,HL_idx,NL_sid = find_never_listen_idx(test,train)
    out_fn = ofp+'%s_NLidx_%d'%(i,data_id)
    np.save(out_fn,NL_idx)
    out_fn = ofp+'%s_HLidx_%d'%(i,data_id)
    np.save(out_fn,HL_idx)
