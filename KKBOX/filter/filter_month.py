import numpy as np
from datetime import datetime
import time
from collections import Counter
import pickle

def to_Resys_format(log_data,out_file,ST,ET,AW_song_id):
    ST = time.mktime(time.strptime(ST,'%Y_%m')) * 1000
    ET = time.mktime(time.strptime(ET,'%Y_%m')) * 1000
    RF_file = open(out_file,'wb')

    for i in range(len(log_data)):
        song_id = log_data[i][0]
        user_id = log_data[i][2][0]
        timestamp = log_data[i][1]
        filter_index = (timestamp>ST) & (timestamp<ET)
        song_id = song_id[filter_index]
        csi = Counter(song_id)
        print out_file+':'+str(i)+'---'+str(len(log_data))

        S_key = set(csi.keys()).intersection(AW_song_id)
        for j in S_key:
            RF_file.write(str(csi[j])+' '+str(user_id)+':1 '+str(AW_song_id[j])+':1\n')

    RF_file.close()

def to_libfm_BS_format(log_data,out_path,ST,ET,song_idx,user_idx):
    target_file = open(out_path+'rel_target_'+ST+'_'+ET,'w')
    uid_file = open(out_path+'rel_uid_'+ST+'_'+ET,'w')
    sid_file = open(out_path+'rel_sid_'+ST+'_'+ET,'w')

    ST = time.mktime(time.strptime(ST,'%Y_%m')) * 1000
    ET = time.mktime(time.strptime(ET,'%Y_%m')) * 1000
    for i in range(len(log_data)):
        song_id = log_data[i][0]
        user_id = log_data[i][2][0]
        timestamp = log_data[i][1]
        filter_index = (timestamp>ST) & (timestamp<ET)
        song_id = song_id[filter_index]
        csi = Counter(song_id)
        print out_file+':'+str(i)+'---'+str(len(log_data))

        S_key = set(csi.keys()).intersection(song_idx)
        for j in S_key:
            target_file.write(str(csi[j])+'\n')
            uid_file.write(str(user_idx[user_id])+'\n')
            sid_file.write(str(song_idx[j])+'\n')

    target_file.close()
    uid_file.close()
    sid_file.close()

if __name__ == '__main__':
    log_data = np.load('/home/fearofchou/data/KKBOX/stats/All_log_filter_sort_timestamp.npy')
    log_user = np.load('/home/fearofchou/data/KKBOX/stats/log_user_id.npy')
    user_idx = {}
    for idx,val in enumerate(sorted(log_user)):
        user_idx[val] = idx
    AW_song_id = np.load('/home/fearofchou/data/KKBOX/stats/AW_song_id.npy')
    song_idx = {}
    for idx,val in enumerate(sorted(AW_song_id)):
        song_idx[val] = idx

    out_file = '/home/fearofchou/code/KKBOX/data/KKBOX_have_timestamp.resys'
    '''
    for i in range(2,11):
        ST = '2013_%02d' % (i-1)
        ET = '2013_%02d' % (i)
        out_path = '/home/fearofchou/data/KKBOX/libfm/'
        to_libfm_BS_format(log_data,out_path,ST,ET,song_idx,user_idx)

    for i in range(11,13):
        ST = '2012_%02d' % (i-1)
        ET = '2012_%02d' % (i)
        out_path = '/home/fearofchou/data/KKBOX/libfm/'
        to_libfm_BS_format(log_data,out_path,ST,ET,song_idx,user_idx)

    '''
    ST = '2012_%02d' % (12)
    ET = '2013_%02d' % (1)
    out_path = '/home/fearofchou/data/KKBOX/libfm/'
    to_libfm_BS_format(log_data,out_path,ST,ET,song_idx,user_idx)
