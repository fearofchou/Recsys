import numpy as np

data_id = 2
tnp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/'


with open(tnp + 'rel_uid_%02d.train'%(data_id)) as f:
    uid_tr = np.array(f.readlines()).astype(int)
with open(tnp + 'rel_uid_%02d.test'%(data_id)) as f:
    uid_te = np.array(f.readlines()).astype(int)


with open(tnp + 'rel_sid_%02d.train'%(data_id)) as f:
    sid_tr = np.array(f.readlines()).astype(int)
with open(tnp + 'rel_sid_%02d.test'%(data_id)) as f:
    sid_te = np.array(f.readlines()).astype(int)


NL_uid_idx = np.load('/home/fearofchou/data/KKBOX/stats/NL_usid/uid_NLidx_%d.npy'%(data_id))
NL_uid_len = len(np.unique(uid_te[NL_uid_idx]))

NL_sid_idx = np.load('/home/fearofchou/data/KKBOX/stats/NL_usid/sid_NLidx_%d.npy'%(data_id))
NL_sid_len = len(np.unique(sid_te[NL_sid_idx]))

len_uid_tr = len(np.unique(uid_tr))
len_sid_tr = len(np.unique(sid_tr))

print 'train uid num = %d'%(len_uid_tr)
print 'train sid num = %d'%(len_sid_tr)
print 'train records num = %d'%(len(sid_tr))

range_te = np.zeros(len(uid_te))

range_te[NL_uid_idx]=-1
range_te[NL_sid_idx]=-1
CS_te_idx = range_te>-1


print 'warm-start test'
print 'test uid = %d'%(len(np.unique(uid_te[CS_te_idx])))
print 'test sid = %d'%(len(np.unique(sid_te[CS_te_idx])))
print 'test records = %d'%(len(sid_te[CS_te_idx]))


range_te = np.zeros(len(uid_te))
range_te[NL_sid_idx]= 1
range_te[NL_uid_idx]= 0
CS_te_idx = range_te==1

print 'cold-start test'
print 'test uid = %d'%(len(np.unique(uid_te[CS_te_idx])))
print 'test sid = %d'%(len(np.unique(sid_te[CS_te_idx])))
print 'test records = %d'%(len(sid_te[CS_te_idx]))


range_te = np.zeros(len(uid_te))
range_te[NL_uid_idx]= 1
CS_te_idx = range_te==0

print 'ALL'
print 'test uid = %d'%(len(np.unique(uid_te[CS_te_idx])))
print 'test sid = %d'%(len(np.unique(sid_te[CS_te_idx])))
print 'test records = %d'%(len(sid_te[CS_te_idx]))

