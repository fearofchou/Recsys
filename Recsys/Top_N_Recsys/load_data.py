import numpy as np
import glob
#load data
fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/libfm_out_recsys/'
pred_fn = {}
fl = glob.glob(fp+'*.pred')
for fn in fl:
    with open(fn) as f:
        pred_fn[fn] = np.array(f.readlines()).astype(float)
fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/'
did= 99
with open(fp + 'rel_uid_%d.test'%(did)) as f:
    UID = np.array(f.readlines()).astype(int)
with open(fp + 'rel_sid_%d.test'%(did)) as f:
    SID = np.array(f.readlines()).astype(int)
with open(fp + 'rel_uid_%d.train'%(did)) as f:
    UID_tr = np.array(f.readlines()).astype(int)
with open(fp + 'rel_sid_%d.train'%(did)) as f:
    SID_tr = np.array(f.readlines()).astype(int)

import pickle
with open('/home/fearofchou/data/KKBOX/stats/song_info.dict') as f:
    song_info  = pickle.load(f)

real_sid = np.unique(np.load('/home/fearofchou/data/KKBOX/stats/AW_song_id.npy'))


#process data
UID_SID_tr_dict = {}
for idx,val in enumerate(UID_tr):
    try:
        UID_SID_tr_dict[val].append(SID[idx])
    except:
        UID_SID_tr_dict[val] = [SID[idx]]

UID_dict = {}
for fn in pred_fn.keys():
    UID_dict[fn] = {}
    for idx,val in enumerate(UID):
        try:
            UID_dict[fn][val].append(pred_fn[fn][idx])
        except:
            UID_dict[fn][val] = [pred_fn[fn][idx]]

SID = np.unique(SID)
N = 1000
UID_rank = {}
for fn in pred_fn.keys():
    UID_rank[fn] = {}
    for i in UID_dict[fn].keys():
        UID_rank[fn][i] = SID[ np.argsort(UID_dict[fn][i])[::-1][:N] ]

#tran to artist id
UID_AID_tr_dict = {}
for uid in UID_SID_tr_dict:
    UID_AID_tr_dict[uid] = {}
    for sid in UID_SID_tr_dict[uid]:
        AID = song_info[ real_sid[sid] ]['artist_id']
        try:
            UID_AID_tr_dict[uid].append(AID)
        except:
            UID_AID_tr_dict[uid] = [AID]

#sid pop
SID_pop = {}
for sid in SID_tr:
    try:
        SID_pop[sid] +=1
    except:
        SID_pop[sid] = 1




