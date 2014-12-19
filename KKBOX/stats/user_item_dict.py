import numpy as np

import glob
data_id = 11
pred_fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/'
fn_ty = ['*uid_%02d*'%(data_id),'*sid_%02d*'%(data_id),'*target_%02d*'%(data_id)]

UID = {}
for ty in fn_ty:
    fl = glob.glob(pred_fp+ty)

    for fn in fl:
        with open(fn) as f:
            UID[fn] = np.array(f.readlines()).astype('float')

fl = UID.keys()
SID_dict = {}
UID_dict = {}
for idx,val in enumerate(UID[fl[0]]):
    uid = UID[fl[5]]
    sid = UID[fl[3]]
    try:
        UID_dict[uid[idx]].append(val)
    except:
        UID_dict[uid[idx]] = [val]
    try:
        SID_dict[sid[idx]].append(val)
    except:
        SID_dict[sid[idx]] = [val]

tuid = UID[fl[2]]
tsid = UID[fl[4]]
ttar = UID[fl[1]]
