import numpy as np
import pickle,sys
sys.path.append('/home/fearofchou/code/pro_bar/')
from mybar import *

def write_user_item(uid_val,sid_val):
    T_user = 28372
    T_song = 124716

    rel_uid_file = '/home/fearofchou/data/KKBOX/libfm/rel_uid_' + str(T_user)
    rel_sid_file = '/home/fearofchou/data/KKBOX/libfm/rel_sid_' + str(T_song)

    f = open(rel_uid_file,'w')
    for i in range(T_user):
        f.write('0 ' + str(i)  + ':1\n' )
    f.close()

    f = open(rel_sid_file,'w')
    for i in range(T_song):
        f.write('0 ' + str(i)  + ':1\n' )
    f.close()

def norm_binary(fea_dict,Top_N,norm):
    fea_ary_norm = {}
    for i in fea_dict.keys():
        fea_ary_norm[i] =np.zeros(len(fea_dict[i]))
        Top_idx = np.argsort(fea_dict[i])[::-1]
        if 'pos' in norm:
            fea_ary_norm[i][Top_idx[:Top_N]] = 1
        if 'neg' in norm:
            fea_ary_norm[i][Top_idx[-Top_N:]] = -1
    return fea_ary_norm

from scipy import stats
def dict_to_lib(ifile,ofile,Nroot,norm,Top_N):
    Nroot = float(Nroot)
    with open(ifile) as handle:
        fea_dict = pickle.load(handle)

    fea_key = sorted(fea_dict.keys())
    fea_ary = np.zeros([len(fea_key),len(fea_dict[fea_key[0]])])

    for idx,val in enumerate(sorted(fea_key)):
        fea_ary[idx,:] = fea_dict[val]

    if norm == 'zs':
        fea_ary_norm = stats.zscore(fea_ary,axis=1,ddof=1)
    if norm == 'non':
        fea_ary_norm = fea_ary
    if 'bin' in norm:
        fea_ary_norm = norm_binary(fea_dict,Top_N,norm)

    print ofile+':'
    pbar = mybar('',len(fea_key))

    with open(ofile,'w') as f:
        for val in sorted(fea_ary_norm):
            f.write('0')
            for fea_idx,fea_val in enumerate(fea_ary_norm[val]):
                if fea_val!=0:
                    f.write(' ' + str(fea_idx) + ':' + str(fea_val**(1/Nroot)))
            f.write('\n')
            pbar.update(idx)

fea = ['AW_genre','AW_acoustic','AW_mood','MFCC','AW']
norm = 'binpos'
Nroot = 1
Top_N = [10]
import subprocess,shutil
CT = 'python /home/fearofchou/code/Tools/libFM/Convert_Transpose.py'
fp = '/home/fearofchou/data/KKBOX/libfm/feature_data_BS/'
for i in fea:
    for T in Top_N:
        fea_ifile = '/home/fearofchou/data/KKBOX/feature/rel_%s.dict'%(i)
        if 'bin' in norm:
            fea_ofile = '/home/fearofchou/data/KKBOX/feature/rel_%s_%s_%d.lib'%(i,norm,T)
        if norm == 'non':
            fea_ofile = '/home/fearofchou/data/KKBOX/feature/rel_%s_%s_%d.lib'%(i,norm,Nroot)

        dict_to_lib(fea_ifile,fea_ofile,Nroot,norm,T)

        subprocess.call(CT+' '+fea_ofile,shell=True)
        shutil.copy(fea_ofile+'.xt',fp+fea_ofile.split('/')[-1]+'.xt')


