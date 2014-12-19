import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from collections import Counter

def plt_hist(data,bins,plt_log,out_name):
    plt.clf()
    plt.hist(data, bins, log=plt_log)
    plt.savefig(out_name)

#his playcount frequency
train = MMP_data['rel_target_11.train']

#per each user-song
train_max = int(np.ceil(train.max()) )
bins = range(1,train_max+1)
out_name = 'per user-song playcount'

#per user
UID_key = UID_dict.keys()
UID_mean_PC = []
UID_listen_len = []
for uid in UID_key:
    UID_mean_PC.append(np.mean(UID_dict[uid]))
    UID_listen_len.append(len(UID_dict[uid]))

out_name = 'Mean users playcount'
UID_max = int( np.ceil(max(UID_mean_PC)) )
plt_hist(UID_mean_PC,range(UID_max), True, out_name)
out_name = 'Mean users number of listening'
UID_max = int( np.ceil(max(UID_listen_len)) )
plt_hist(UID_listen_len,range(UID_max), True, out_name)


#per song
SID_key = SID_dict.keys()
SID_mean_PC = []
SID_listen_len = []
for uid in SID_key:
    SID_mean_PC.append(np.mean(SID_dict[uid]))
    SID_listen_len.append(len(SID_dict[uid]))

out_name = 'Mean songs playcount'
SID_max = int( np.ceil(max(SID_mean_PC)) )
plt_hist(SID_mean_PC,range(SID_max), True, out_name)
out_name = 'Mean song number of listening'
SID_max = int( np.ceil(max(SID_listen_len)) )
plt_hist(SID_listen_len,range(SID_max), True, out_name)


