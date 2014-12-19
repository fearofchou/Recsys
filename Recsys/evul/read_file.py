import numpy as np
import glob

def pred_read(fnp,tp,data_id):
    NL_uid_idx = np.load('/home/fearofchou/data/KKBOX/stats/NL_usid/uid_NLidx_%d.npy'%(data_id))
    if tp == 'libfm':
        fl = glob.glob(fnp)
        pred_tar={}
        for fn in fl:
            kfn = fn.split('/')[-1]
            with open(fn) as f:
                pred_tar[kfn] = np.array(f.readlines()).astype(float)
            pred_tar[kfn][NL_uid_idx] = 0
    if tp == 'graphchi':
        start = 3
        splitter = ' '
        fl = glob.glob(fnp)
        pred_tar = {}
        for fn in fl:
            with open(fn) as f:
                pred = f.readlines()
            kfn = fn.split('/')[-1]
            pred = pred[start:]
            pred_tar[kfn] = []
            for i in pred:
                pred_tar[kfn].append(float(i.split(splitter)[-1]))
            pred_tar[kfn] = np.array(pred_tar[kfn])
            pred_tar[kfn][NL_uid_idx] = 0
    return pred_tar

def true_read(fnp,data_id):
    NL_uid_idx = np.load('/home/fearofchou/data/KKBOX/stats/NL_usid/uid_NLidx_%d.npy'%(data_id))
    fl =glob.glob(fnp)
    true = {}
    for fn in fl:
        k = fn.split('/')[-1].split('_')[2]
        with open(fn) as f:
            true[k] = np.array(f.readlines()).astype(float)
        true[k][NL_uid_idx] = 0
    return true

def test_split(data_id,pred):
    #load NL_idx
    fp = '/home/fearofchou/data/KKBOX/stats/NL_usid/'
    fn = 'sid_NLidx_%d.npy'%(data_id)

    test_idx = {}
    test_idx['TS1'] = np.load(fp + fn) #never listening in training cold start
    fn = 'sid_HLidx_%d.npy'%(data_id)
    test_idx['TS2'] = np.load(fp + fn) #have listening in tarining walm start
    test_idx['TS3'] = np.array(range(len(pred))) #all test
    return test_idx

