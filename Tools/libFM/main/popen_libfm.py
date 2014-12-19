import subprocess
import os,time
run_exe = 'python /home/fearofchou/code/Tools/libFM/libfm_flow.py'

def fea_iden(fea):
    fea_fn = ''
    if 'uid' in fea:
        fea_fn = fea_fn+'U'
    if 'sid' in fea:
        fea_fn = fea_fn+'+S'
    if 'MFCC' in fea:
        fea_fn = fea_fn+'+MFCC'
    if 'AW_b' in fea:
        fea_fn = fea_fn+'+AW'
    if 'AW_a' in fea:
        fea_fn = fea_fn+'+AWA'
    if 'AW_g' in fea:
        fea_fn = fea_fn+'+AWG'
    if 'AW_m' in fea:
        fea_fn = fea_fn+'+AWM'
    return fea_fn

def libfm_popen(ofp,data_id,norm_tar,para):
    t = time.time()
    #mv argv
    term = ['long','short']
    split = ['month','random']
    split=split[0]
    term=term[0]
    data_path = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/'
    print data_path
    #data_path = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS'+ \
    #    '/split_by_%s/%s_term_playcount_mean/'%(split,term)
    exe_path = '/home/fearofchou/data/KKBOX/libfm/feature_data_BS/'
    try:
        os.mkdir(ofp)
    except:
        pass

    #mv tr_te data to exe path
    mv_cmd = run_exe+' '+'-mv '+'%02d'%(data_id)+' '+data_path+' '\
        +exe_path+' '+norm_tar
    mv = subprocess.call(mv_cmd,shell=True)
    #libfm argv
    train_file = 'rel_target.lib.train'
    test_file = 'rel_target.lib.test'
    me= 'mcmc'
    #MAIN()
    pro={}
    for idx,val in enumerate(para):
        dim = para[val]['dim']
        rel = para[val]['fea']
        ite = para[val]['ite']

        fea = fea_iden(rel)

        dim_fn = dim.split(',')[-1]
        out_libfm =ofp + 'ID_%d_TAR_%s_DIM_%s_ITE_%s_FEA_%s_.pred'\
            %(data_id,norm_tar,dim_fn,ite,fea)

        cmd = run_exe+' '+'-main'+' '+exe_path +\
            ' '+train_file+' '+test_file+' '+\
            out_libfm+' '+rel+' '+me+ ' '+dim+ ' '+ite
        pro[idx] = subprocess.Popen(cmd,shell=True)
        #time.sleep(1)
    for i in pro.keys():
        pro[i].wait()



