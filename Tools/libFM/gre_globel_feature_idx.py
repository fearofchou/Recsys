import numpy as np
import glob

rel_fl = glob.glob('/home/fearofchou/data/KKBOX/libfm/filter_data_BS/month_sid/*release*')

def globel_feature(d):
    MESR_dict = {}
    for idx,val in enumerate(d):
        MESR_dict[val] = idx

    MESR_fn = {}
    for fn in rel_fl:
        with open(fn) as f:
            MESR_fn[fn.split('/')[-1]] = map(int,f.readlines())

    for i in sorted(MESR_fn.keys()):
        te_fn = '/home/fearofchou/data/KKBOX/libfm/filter_data_BS/month_sid/'
        f = open(te_fn+i,'w')
        for j in MESR_fn[i]:
            f.write(str(MESR_dict[j])+'\n')
        f.close()

MESR_fn = {}
for fn in rel_fl:
    with open(fn) as f:
        MESR_fn[fn.split('/')[-1]] = map(int,f.readlines())

s_fn = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/short_term_playcount/'
for idx,fn in enumerate(sorted(MESR_fn.keys())):
    te_fn = s_fn+'rel_MESR_%02d.test'%(idx)
    f = open(te_fn,'w')
    for i in MESR_fn[fn]:
        print i
        if i>12:
            i=12
        if i==-99:
            i==0
        if i<0:
            i==0
        f.write(str(i)+'\n')
        print i
    f.close()

    tr_fn = s_fn+'rel_MESR_%02d.train'%(idx)
    f = open(tr_fn,'w')
    for tr_fn in MESR_fn.keys():
        if tr_fn != fn:
            for i in MESR_fn[tr_fn]:
                if i>12:
                    i=12
                if i==-99:
                    i==0
                if i<0:
                    i==0
                f.write(str(i)+'\n')
    f.close()

