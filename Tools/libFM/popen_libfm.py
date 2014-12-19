import subprocess
import os,time
run_exe = 'python /home/fearofchou/code/Tools/libFM/libfm_flow.py'

def libfm_popen(data_id,fea_id,norm_tar,dim,iterations,features):
    t = time.time()
    #mv argv
    term = ['long','short']
    split = ['month','random']
    split=split[0]
    term=term[0]
    data_path = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS'+ \
        '/split_by_%s/%s_term_playcount_mean/'%(split,term)
    exe_path = '/home/fearofchou/data/KKBOX/libfm/feature_data_BS/'
    try:
        os.mkdir(data_path+'libfm_out')
    except:
        pass

    #mv tr_te data to exe path
    mv_cmd = run_exe+' '+'-mv '+'%02d'%(data_id)+' '+data_path+' '\
        +exe_path+' '+norm_tar
    mv = subprocess.call(mv_cmd,shell=True)
    #libfm argv
    train_file = 'rel_target.lib.train'
    test_file = 'rel_target.lib.test'
    out_libfm = ''
    rel = ''
    me= 'mcmc'
    #MAIN()
    pro={}
    for idx,fea in enumerate(fea_id):
        #rel = 'rel_uid.lib,'+features[fea]
        rel = 'rel_uid.lib,'+features[fea]
        fea = features[fea].split('rel_')[1].split('.')[0]
        #out_file
        out_libfm =out_libfm + '%s_.pred'%(fea)

        cmd = run_exe+' '+'-main'+' '+exe_path\
            +' '+train_file+' '+test_file+' '\
            +out_libfm+' '+rel+' '+me+ ' '+dim+ ' '+iterations

        pro[idx] = subprocess.Popen(cmd,shell=True)
        #time.sleep(1)
    for i in pro.keys():
        pro[i].wait()


#feature
fea_id = [0,1,2,3,4,5,6,7]
norm = 'non'
nroot = 2
features = ['rel_sid.lib','rel_AW.lib','rel_AW3R.lib','rel_AW_mood.lib'\
            ,'rel_AW_genre.lib','rel_AW_acoustic.lib','rel_MFCC.lib'\
            ,'rel_AW_%s_%d.lib'%(norm,nroot)]
#file
data_id = 11
#target
norm_tar = ['org','5Ilog2p1','log2p1','5I']
#libfm par
dim = '1,1,8'
iterations = str(50)
out_libfm = data_path+'libfm_out/'+\
    'ID_%02d_TAR_%s_DIM_%s_FEA_'%(data_id,norm_tar[2],dim)
        '''
        out_libfm = '/home/fearofchou/data/KKBOX/libfm/'+\
            'WORST_ID_%02d_TAR_%s_DIM_%s_FEA_%s_.pred'\
            %(data_id,norm_tar,dim,fea)
        '''
#==================================

libfm_popen(data_id,fea_id,norm_tar[2],dim,iterations,features)


#====find max RMSE result==========
'''
import numpy as np
cpfn = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/rel_target_5Ilog2p1_11.test'
with open(cpfn) as f:
    true = np.array(f.readlines()).astype(float)

import os
for i in range(10000):
    cpfn = '/home/fearofchou/data/KKBOX/libfm/ID_11_TAR_5Ilog2p1_DIM_1,1,8_FEA_sid_.pred'
    with open(cpfn) as f:
        worst = np.array(f.readlines()).astype(float)

    libfm_popen(data_id,fea_id,norm_tar[1],dim,iterations,features)

    wpfn = '/home/fearofchou/data/KKBOX/libfm/WORST_ID_11_TAR_5Ilog2p1_DIM_1,1,8_FEA_sid_.pred'
    with open(wpfn) as f:
        pred = np.array(f.readlines()).astype(float)

    worst = np.sqrt( ((worst - true)**2).mean() )
    pred = np.sqrt( ((pred - true)**2).mean() )

    print '%.4f ? %.4f'%(worst,pred)
    if pred > worst:
        os.rename(wpfn,cpfn)
'''


