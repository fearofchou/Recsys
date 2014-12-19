import numpy as np
import glob
fp = '/home/fearofchou/data/KKBOX/libfm/filter_data_BS/month_sid/'

uid_fl = sorted(glob.glob(fp + '*uid*'))
sid_fl = sorted(glob.glob(fp + '*sid*'))
tar_fl = sorted(glob.glob(fp + '*tar*'))

sid = []
uid = []
tar = []
for i in uid_fl:
    with open(i) as f:
        uid.extend( map(int,f.readlines()) )
for i in sid_fl:
    with open(i) as f:
        sid.extend( map(int,f.readlines()) )
for i in tar_fl:
    with open(i) as f:
        tar.extend( map(int,f.readlines()) )

uid = np.array(uid)
sid = np.array(sid)
tar = np.array(tar)

rec = {}
for idx,val in enumerate(sid):
    try:
        rec['%d_%d'%(uid[idx],sid[idx])].append(tar[idx])
    except:
        rec['%d_%d'%(uid[idx],sid[idx])] =[ tar[idx] ]
'''
print 'uid len = %d'%(len(uid))
print 'sid len = %d'%(len(sid))
print 'tar len = %d'%(len(tar))

rec = {}
for idx,val in enumerate(sid):
    rec['%d_%d'%(uid[idx],val)] = 1

print 'total recorsd = %d'%(len(rec))

all_da={}
all_da['uid'] = uid
all_da['sid'] = sid
all_da['tar'] = tar
'''
'''
uid = {}
sid = {}
tar = {}
for i in sorted(uid_fl):
    fn = i.split('/')[-1]
    fn = fn.split('uid_')[-1]
    with open(i) as f:
        uid[fn] =  map(int,np.array(f.readlines()))
for i in sorted(sid_fl):
    fn = i.split('/')[-1]
    fn = fn.split('sid_')[-1]
    with open(i) as f:
        sid[fn] =  map(int,np.array(f.readlines()))
for i in sorted(tar_fl):
    fn = i.split('/')[-1]
    fn = fn.split('target_')[-1]
    with open(i) as f:
        tar[fn] =  map(int,np.array(f.readlines()))
'''
'''
res = {}
for i in sorted(sid.keys()):
    rec[i]= {}
    for idx,val in enumerate(sid[i]):
        rec[i]['%d_%d'%(uid[i][idx],sid[i][idx])] = 1

    print 'uid=%d sid=%d tar=%d fix=%d'%(len(uid[i]),len(sid[i]),len(tar[i]),len(rec[i]))
'''
'''
#split RLS
data = {}
data['uid'] = uid
data['sid'] = sid
data['tar'] = tar
fea = ['uid','sid','tar']
RLS_tr = {}
sid_key = sorted(sid.keys())
te_key = sid_key[-1]
sid_key = sid_key[:-1]
#train
for f in fea:
    RLS_tr[f] = []
    for i in sid_key:
        RLS_tr[f].extend(data[f][i])
RLS={}
RLS['tr'] = {}
uid = RLS_tr['uid']
sid = RLS_tr['sid']
tar = RLS_tr['tar']
for idx,val in enumerate(RLS_tr['uid']):
    try:
        RLS['tr']['%d_%d'%(uid[idx],sid[idx])].append(tar[idx])
    except:
        RLS['tr']['%d_%d'%(uid[idx],sid[idx])] =[ tar[idx] ]


RLS['te'] = {}
uid = data['uid'][te_key]
sid = data['sid'][te_key]
tar = data['tar'][te_key]
for idx,val in enumerate(uid):
    try:
        RLS['te']['%d_%d'%(uid[idx],sid[idx])].append(tar[idx])
    except:
        RLS['te']['%d_%d'%(uid[idx],sid[idx])] =[ tar[idx] ]

def write_data(fp,data_dict,data_id,tr_te):
    fu = open(fp + 'rel_uid_%02d.%s'%(data_id,tr_te),'w')
    fs = open(fp + 'rel_sid_%02d.%s'%(data_id,tr_te),'w')
    ft = open(fp + 'rel_target_log2p1_%02d.%s'%(data_id,tr_te),'w')

    for i in data_dict:
        ust = i.split('_')
        fu.write('%s\n'%(ust[0]))
        fs.write('%s\n'%(ust[1]))
        log_tar = np.mean(data_dict[i])
        log_tar = np.log2(1+log_tar)
        ft.write('%f\n'%(log_tar))

    fu.close()
    fs.close()
    ft.close()
fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/'
write_data(fp,RLS['te'],11,'test')
write_data(fp,RLS['tr'],11,'train')
'''
#random
def write_data(fp,data_dict,data_id,tr_te):
    fu = open(fp + 'rel_uid_%02d.%s'%(data_id,tr_te),'w')
    fs = open(fp + 'rel_sid_%02d.%s'%(data_id,tr_te),'w')
    ft = open(fp + 'rel_target_log2p1_%02d.%s'%(data_id,tr_te),'w')

    for i in data_dict:
        ust = i.split('_')
        fu.write('%s\n'%(ust[0]))
        fs.write('%s\n'%(ust[1]))
        log_tar = np.mean(data_dict[i])
        log_tar = np.log2(1+log_tar)
        ft.write('%f\n'%(log_tar))
    fu.close()
    fs.close()
    ft.close()

import random
da_le = len(uid)
te_le = int(np.ceil(da_le*0.081))
rs_idx = random.sample( range(da_le),te_le )

da_ze = np.zeros(da_le)
da_ze[rs_idx] = 1

da_ra = np.arange(da_le)

te_idx = da_ra[da_ze==1]
tr_idx = da_ra[da_ze==0]

RLS ={}
RLS['te'] = {}
RLS['tr'] = {}
for idx in da_ra[te_idx]:
    try:
        RLS['te']['%d_%d'%(uid[idx],sid[idx])].append(tar[idx])
    except:
        RLS['te']['%d_%d'%(uid[idx],sid[idx])] =[ tar[idx] ]

for idx in da_ra[tr_idx]:
    try:
        RLS['tr']['%d_%d'%(uid[idx],sid[idx])].append(tar[idx])
    except:
        RLS['tr']['%d_%d'%(uid[idx],sid[idx])] =[ tar[idx] ]
print len(RLS['tr'])
print len(RLS['te'])
fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/'
write_data(fp,RLS['te'],2,'test')
write_data(fp,RLS['tr'],2,'train')
