import numpy as np
import glob

#libfm format to graphchi
data_id = 11
tr_or_te = ['train','test']
norm_tar = ['log2p1']

for tr_te in tr_or_te:
    print tr_te
    fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/'
    uid_fn = 'rel_uid_%02d.%s'%(data_id,tr_te)
    sid_fn = 'rel_sid_%02d.%s'%(data_id,tr_te)

    with open(fp+uid_fn) as f:
        uid = np.array(f.readlines()).astype(int)
    with open(fp+sid_fn) as f:
        sid = np.array(f.readlines()).astype(int)
    uid = uid+1
    sid = sid+1
    for nt in norm_tar:
        tar_fn = 'rel_target_%s_%02d.%s'%(nt,data_id,tr_te)
        with open(fp+tar_fn) as f:
            tar = np.array(f.readlines()).astype(float)

        sfp = '/home/fearofchou/data/KKBOX/graphchi/'
        sfn = 'rel_%s_%02d.%s.gar'%(nt,data_id,tr_te)

        f = open(sfp+sfn,'w')
        f.write('%%MatrixMarket matrix coordinate real general\n')
        f.write('%d %d %d\n'%(28372,124716,len(uid)))

        for idx,val in enumerate(uid):
            f.write('%d %d %f\n'%(uid[idx],sid[idx],tar[idx]))
        f.close()
