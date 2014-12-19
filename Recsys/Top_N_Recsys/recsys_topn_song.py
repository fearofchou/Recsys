import numpy as np
import glob
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

UID_SID_tr_dict = {}
for idx,val in enumerate(UID_tr):
    try:
        UID_SID_tr_dict[val].append(SID[idx])
    except:
        UID_SID_tr_dict[val] = [SID[idx]]
'''
UID_SID_te_dict = {}
for idx,val in enumerate(UID):
    try:
        UID_SID_te_dict[val].append(SID[idx])
    except:
        UID_SID_te_dict[val] = [SID[idx]]
'''

UID_dict = {}
for fn in pred_fn.keys():
    UID_dict[fn] = {}
    UID_SID_dict[fn] = {}
    for idx,val in enumerate(UID):
        try:
            UID_dict[fn][val].append(pred_fn[fn][idx])
        except:
            UID_dict[fn][val] = [pred_fn[fn][idx]]

SID = np.unique(SID)
N = 100
UID_rank = {}
for fn in pred_fn.keys():
    UID_rank[fn] = {}
    for i in UID_dict[fn].keys():
        UID_rank[fn][i] = SID[ np.argsort(UID_dict[fn][i])[-N:] ]

print 'fn,div,fer,pop\n'
for fn in pred_fn.keys():
    pop_val = POP.us_pop(UID_rank[fn],SID_dict_pop)
    div_val = DIV.us_div(UID_rank[fn],song_meta,real_sid)
    fre_val = FRE.us_fre(UID_rank[fn],song_meta,real_sid)
    idx = pop_val!=0
    pop_val = pop_val[idx]
    fre_val = fre_val[idx]
    div_val = div_val[idx]
    #pop_val = (pop_val[idx] - pop_val[idx].min()) / ( pop_val[idx].max()-pop_val[idx].min()  )
    #div_val = (div_val[idx] - div_val[idx].min()) / ( div_val[idx].max()-div_val[idx].min()  )
    #fre_val = (fre_val[idx] - fre_val[idx].min()) / ( fre_val[idx].max()-fre_val[idx].min()  )
    print 'org|%s,%f,%f,%f\n'%(fn.split('/')[-1],div_val.mean(),fre_val.mean(),pop_val.mean())

    pop_val = (pop_val - pop_val.min()) / ( pop_val.max()-pop_val.min()  )
    div_val = (div_val - div_val.min()) / ( div_val.max()-div_val.min()  )
    fre_val = (fre_val - fre_val.min()) / ( fre_val.max()-fre_val.min()  )

    print 'norm|%s,%f,%f,%f\n'%(fn.split('/')[-1],div_val.mean(),fre_val.mean(),pop_val.mean())

A_SID = {}
A_SID[0] = lis_sid

pop_val = POP.us_pop(A_SID,SID_dict_pop)
div_val = DIV.us_div(A_SID,song_meta,real_sid)
fre_val = FRE.us_fre(A_SID,song_meta,real_sid)
print 'base|%s,%f,%f,%f\n'%(fn.split('/')[-1],div_val.max(),fre_val.max(),pop_val.max())
