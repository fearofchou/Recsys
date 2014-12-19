import numpy as np
import glob

def read(fn):
    pred_tar = {}
    start = 3
    splitter =' '
    with open(fn) as f:
        pred = f.readlines()
    pred = pred[start:]
    pred_tar = []
    for i in pred:
        pred_tar.append(i.split(splitter)[-1])
    return np.array(pred_tar).astype(float)

if __name__ == '__main__':
    data_id = 2
    fp = '/home/fearofchou/data/KKBOX/graphchi/'
    fn = '*%02d*.predict'%(data_id)
    fl = glob.glob(fp+fn)
    pred_tar = read(fl[0])

