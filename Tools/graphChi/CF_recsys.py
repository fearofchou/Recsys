import numpy as np
import subprocess
import os,sys
import shutil

ex = '/home/fearofchou/Tools/graphchi-cpp/toolkits/collaborative_filtering/'
def write_read_for_evul(fn,ofn):
    pred_tar = {}
    start = 3
    splitter =' '
    with open(fn) as f:
        pred = f.readlines()
    pred = pred[start:]
    pred_tar = []
    for i in pred:
        pred_tar.append(i.split(splitter)[-1])

    f = open(ofn,'w')
    for i in pred_tar:
        f.write('%s'%(i))
    f.close()

def SGD(ex,tr,te,mi,vf):
    me = 'sgd '
    sg = '--sgd_gamma=1e-4 '
    sl = '--sgd_lambda=1e-4 '
    cmd = ex+me+tr+te+sg+sl+mi
    print cmd
    subprocess.call( cmd,shell = True)

def SVDpp(ex,tr,te,mi,vf):
    me = 'svdpp '
    sg = '--biassgd_gamma=1e-4 '
    sl = '--biassgd_lambda=1e-4 '
    cmd = ex+me+tr+te+sg+sl+mi
    print cmd
    subprocess.call( cmd,shell = True)

norm_tar = ['log2p1']
data_id = 11
vector_size = 20
ite =40
fp = '/home/fearofchou/data/KKBOX/graphchi/'
for tt in norm_tar:
    tr_fn = '/home/fearofchou/data/KKBOX/graphchi/rel_%s_%02d.train.gar'%(tt,data_id)
    te_fn = '/home/fearofchou/data/KKBOX/graphchi/rel_%s_%02d.test.gar'%(tt,data_id)

    tr = '--training=%s '%(tr_fn)
    te = '--test=%s '%(te_fn)
    mi = '--max_iter=%d'%(ite)
    vf = '--D=%d'%(vector_size)

    SGD(ex,tr,te,mi,vf)
    fn = 'ID_%d_TAR_%s_DIM_%d_ITE_%d_FEA_%s_.pred'%(data_id,tt,vector_size,ite,'MFSGD')
    write_read_for_evul(te_fn+'.predict',fp+fn)
    SVDpp(ex,tr,te,mi,vf)
    fn = 'ID_%d_TAR_%s_DIM_%d_ITE_%d_FEA_%s_.pred'%(data_id,tt,vector_size,ite,'SVD++')
    write_read_for_evul(te_fn+'.predict',fp+fn)


