import numpy as np
#load sid uid
fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/'
with open(fp+'rel_uid_11.train') as f:
    UID = np.array(f.readlines()).astype(int)
with open(fp+'rel_uid_11.test') as f:
    UID_test = np.array(f.readlines()).astype(int)
with open(fp+'rel_sid_11.train') as f:
    SID = np.array(f.readlines()).astype(int)
#========================================================

SID_dict_pop =np.zeros(124716)
for i in SID:
    SID_dict_pop[i] +=1

#each user dict
UID_dict = {}
for idx,val in enumerate(UID):
    try:
        UID_dict[val].append(SID[idx])
    except:
        UID_dict[val] = [SID[idx]]
#========================================================

#load song meta
import pickle
song_meta_fn = '/home/fearofchou/data/KKBOX/stats/song_meta.dict'
with open(song_meta_fn) as f:
    song_meta = pickle.load(f)
#========================================================

#real sid
song_id_fn = '/home/fearofchou/data/KKBOX/stats/AW_song_id.npy'
real_sid = np.sort(np.load(song_id_fn))
#========================================================

#each user dict
SID_dict = {}
for idx,val in enumerate(SID):
    try:
        SID_dict[val].append(UID[idx])
    except:
        SID_dict[val] = [UID[idx]]
#========================================================

import Diversity as DIV
import Popularity as POP
import Freshness as FRE
UID_div = DIV.us_div(UID_dict,song_meta,real_sid)
UID_fre = FRE.us_fre(UID_dict,song_meta,real_sid)
UID_pop = POP.us_pop(SID,UID_dict)

UID_us = {}
UID_us['Freshness'] = UID_fre
UID_us['Popularity'] = UID_pop
UID_us['Diversity'] = UID_div

import sys
sys.path.append('/home/fearofchou/code/Recsys/evul/')
from evul_all import *
