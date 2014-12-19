import numpy as np

fp = '/home/fearofchou/network_drive/KKBOX_76/KKBOX_cooperation/masked/50K_song-meta/'

fn = '50K_maskedSongs.txt'

with open(fp + fn) as f:
    mask_sid = f.readlines()
mask_id = {}
for i in mask_sid:
    msid = i[:-1].split('\t')
    mask_id[msid[1]] = int(msid[0])

fn = '50K_kkbox_real_song_id.info'
with open(fp + fn) as f:
    sid_info = f.readlines()

meta_type = ['sid','album_id','artist_id',\
             'release','genre']

song_info_dict = {}
for i in sid_info:
    si = i[:-1].split('\t')
    sid = mask_id[si[0]]
    song_info_dict[sid] = {}
    for idx,j in enumerate(si[1:]):
        song_info_dict[sid][meta_type[idx+1]] = si[idx+1].split('T')[0]



import pickle
with open('/home/fearofchou/data/KKBOX/stats/song_info.dict','w') as f:
    pickle.dump(song_info_dict,f)

