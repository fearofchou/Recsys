import numpy as np
import glob

fea_song_age_fp = '/home/fearofchou/data/KKBOX/fearure_extraction/song_age/*'
fl = glob.glob(fea_song_age_fp)
SM_key = sorted(SM_data['uid'].keys())

playcount_for_month = np.zeros((124716,13))
user_for_month = np.zeros((124716,13))

user_pl_month = np.zeros((28372,13))
for idx,fn in enumerate(sorted(fl)):
    print fn
    with open(fn) as f:
        song_age = np.array(f.readlines()).astype('int')

    uid = SM_data['uid'][SM_key[idx]]
    sid = SM_data['sid'][SM_key[idx]]
    tar = SM_data['target'][SM_key[idx]]

    for idx,val in enumerate(uid):
        sa = song_age[idx]
        if song_age[idx]>12:
            sa = 12
        if song_age[idx]<0:
            sa = 0
        playcount_for_month[sid[idx],sa] += tar[idx]
        user_for_month[sid[idx],sa] +=1

Tsid = np.argsort(playcount_for_month.sum(aixs=1))


