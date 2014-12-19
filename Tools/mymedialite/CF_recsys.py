import numpy as np
import subprocess
import os,sys
import shutil

ex = '/home/fearofchou/Tools/mymedialite/bin/rating_prediction '

def MF(ex,tr_fn,te_fn):
    re = '--recommender=MatrixFactorization '
    tr = '--training-file=%s '%(tr_fn)
    te = '--test-file=%s '%(te_fn)
    pf = '--prediction-file=%s '%(te_fn+'.pred')
    sf = '--save-model=%s '%(tr_fn+'.model')
    cmd = ex+re+tr+te+pf+sf
    print cmd
    subprocess.call( cmd,shell = True)

tr_fn = '/home/fearofchou/data/KKBOX/mymedialite/rel_11_train.uir'
te_fn = '/home/fearofchou/data/KKBOX/mymedialite/rel_11_test.uir'

MF(ex,tr_fn,te_fn)

