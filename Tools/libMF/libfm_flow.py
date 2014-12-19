import numpy as np
import subprocess
import os,sys
import shutil
#input Resys format
#user_id::item_id::rating
#1 10 5

def libMF_convert(data):
    ex = '/home/fearofchou/Tools/libmf-1.1/libmf'
    co = ' convert'
    da = ' %s'%(data)
    out_da = ' %s'%(data+'.binary')
    print ex + co + da + out_da
    subprocess.call( ex + co + da +out_da,shell = True)

def libMF_train(data):
    ex = '/home/fearofchou/Tools/libmf-1.1/libmf'
    co = ' train'
    bin_da = ' %s'%(data+'.binary')
    out_da = ' %s'%(data+'.model')
    print ex + co + bin_da + out_da
    subprocess.call( ex + co + bin_da +out_da,shell = True)

def libMF_predict(tr_da,te_da):
    ex = '/home/fearofchou/Tools/libmf-1.1/libmf'
    co = ' predict'
    tes_da = ' %s'%(te_da+'.binary')
    mod_da = ' %s'%(tr_da+'.model')
    pre_da = ' %s'%(te_da+'.pred')
    subprocess.call( ex + co + tes_da + mod_da  + pre_da,shell = True)


tr_fn = '/home/fearofchou/data/KKBOX/libmf/train_11'
te_fn = '/home/fearofchou/data/KKBOX/libmf/test_11'
'''
libMF_convert(tr_fn)
libMF_convert(te_fn)

libMF_train(tr_fn)
libMF_predict(tr_fn,te_fn)
'''

