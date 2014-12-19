import numpy as np
import random
from collections import Counter
fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/rel_uid_11.train'
with open (fp) as f:
    UID = np.array(f.readlines()).astype(int)
fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/rel_sid_11.train'
with open (fp) as f:
    SID = np.array(f.readlines()).astype(int)

UID_dict = {}
for idx,val in enumerate(UID):
    try:
        UID_dict[val].append(SID[idx])
    except:
        UID_dict[val] = [SID[idx]]

CO_UID = np.array(Counter(UID).items())
#top user
print 'Total users = %d'%(len(CO_UID[:,0]))
N = 200
TOP_N_uid_idx = CO_UID[:,1]>N
TOP_N_uid = CO_UID[:,0][TOP_N_uid_idx]
#TOP_N_uid = CO_UID[:,0]

#random
N = 1000
#N = len(CO_UID[:,0])
RAN_UID = np.sort(random.sample(CO_UID[:,0],N))
lis_sid = []
for i in RAN_UID:
    lis_sid.extend( UID_dict[i])
lis_sid = np.unique(lis_sid)

#write filte
N = 99
ofp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS'+\
    '/rel_uid_%d.test'%(N)
fuid = open(ofp,'w')

ofp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS'+\
    '/rel_sid_%d.test'%(N)
fsid = open(ofp,'w')

ofp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS'+\
    '/rel_target_log2p1_%d.test'%(N)
ftar = open(ofp,'w')

for idx,val in enumerate(RAN_UID):
    for iidx,j in enumerate(lis_sid):
        print '%d-%d'%(idx,len(lis_sid))
        fuid.write('%d\n'%(val))
        fsid.write('%d\n'%(j))
        ftar.write('%d\n'%(0))
fuid.close()
fsid.close()
ftar.close()


