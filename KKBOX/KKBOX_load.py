import numpy as np
import pickle

#base data
song_id_fn = '/home/fearofchou/data/KKBOX/stats/AW_song_id.npy'
user_id_fn = '/home/fearofchou/data/KKBOX/stats/log_user_id.npy'
log_fn = '/home/fearofchou/data/KKBOX/stats/All_log_filter_sort_timestamp.npy'
song_meta_fn = '/home/fearofchou/data/KKBOX/stats/song_meta.dict'

KKBOX = {}
KKBOX['song_id'] = np.sort(np.load(song_id_fn))
KKBOX['user_id'] = np.sort(np.load(user_id_fn))
log = np.load(log_fn)
print 'load all log'
user_log_dict = {}
for i in log:
    user_log_dict[i[2][0]] = i

print 'load meta'
with open(song_meta_fn) as f:
    song_meta = pickle.load(f)

#timestamp to date
import datetime,time
def ts2time(ts):
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
def time2ts(date,time_format):
    return time.mktime(time.strftime(date,time_format))

#split month data
print 'load month data'
import glob
fp = '/home/fearofchou/data/KKBOX/libfm/filter_data_BS/month_sid/'
ft = ['uid','sid','target']
SM_data = {}
for t in ft:
    SM_data[t] = {}
    fl = glob.glob('%s*%s*'%(fp,t))
    for f in fl:
        fn = f.split('/')[-1]
        fn = fn.split('_')
        fn = fn[-4]+fn[-3]+fn[-2]+fn[-1]

        with open(f) as fd:
            SM_data[t][fn] = np.array(fd.readlines()).astype(int)

print 'load mean playcount'
fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/'
fl = glob.glob(fp+'rel*11*')
MMP_data = {}
for fn in fl:
    with open(fn) as f:
        MMP_data[fn.split('/')[-1]] = np.array(f.readlines()).astype(float)

