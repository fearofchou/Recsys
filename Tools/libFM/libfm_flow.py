import numpy as np
import subprocess
import os,sys,glob
import shutil
#input Resys format
#user_id::item_id::rating
#1::10::5

def libfm_BS(train_tar,test_tar,out_file,task,me,dim,rel,iterations):
    lf = '/home/fearofchou/Tools/libfm-1.40.src/bin/libFM'
    ta = ' -task ' + task
    Fi = ' -train ' + train_tar + ' -test ' + test_tar
    di = ' -dim ' + dim
    me = ' -method ' + me
    re = ' -relation ' + rel
    ou = ' -out ' + out_file
    it = ' -iter ' + iterations
    subprocess.call( lf+Fi+ta+di+it+me+re+ou,shell = True)
def mv_data(cv_id,ofp,nfp,norm_tar):
    fea = ['uid','sid','target']
    tr_te = ['train','test']
    if norm_tar=='org_':
        norm_tar=''
    for i in fea:
        for j in tr_te:
            if i == 'target':
                ofn = 'rel_%s_%s_%02d.%s'%(i,norm_tar,cv_id,j)
                nfn = 'rel_%s.lib.%s'%(i,j)
                shutil.copy(ofp+ofn,nfp+nfn)
            else:
                ofn = 'rel_%s_%02d.%s'%(i,cv_id,j)
                nfn = 'rel_%s.lib.%s'%(i,j)
                shutil.copy(ofp+ofn,nfp+nfn)
            #print 'mv:'+ofp+ofn
            #print 'to:'+nfp+nfn
    fea_path = '/home/fearofchou/data/KKBOX/feature/*.xt'
    fl = glob.glob(fea_path)
    #move xt to exe path
    for i in fl:
        xt_fn = i.split('/')[-1]
        shutil.copy(i,nfp+xt_fn)
        shutil.copy(i[:-1],nfp+xt_fn[:-1])

    new_fea = ['sid:MFCC','sid:AW','sid:AW_genre',\
               'sid:AW_mood','sid:AW_acoustic']
               #'gid:MESR']
    for fn in fl:
        for j in tr_te:
            #feature
            for fea in new_fea:
                nf = fea.split(':')
                t_id = nf[0]
                fea = nf[1]
                fn_fea = fn.split('/')[-1].split('.')[0]
                if fea in fn:
                    fea = fea.split('.')[0]
                    ofn = 'rel_%s_%02d.%s'%(t_id,cv_id,j)
                    nfn = '%s.lib.%s'%(fn_fea,j)
                    print fn
                    print nfn
                    shutil.copy(ofp+ofn,nfp+nfn)
                    break



if __name__ == '__main__':
    if sys.argv[1] == '-mv':
        data_id = int(sys.argv[2])
        data_path = sys.argv[3]
        exe_path = sys.argv[4]
        norm_tar = sys.argv[5]
        mv_data(data_id,data_path,exe_path,norm_tar)
        print 'mv to : '+exe_path

    if sys.argv[1] == '-main':
        exe_path = sys.argv[2]
        tr = sys.argv[3]
        te = sys.argv[4]
        out_libfm = sys.argv[5]
        rel = sys.argv[6]
        me = sys.argv[7]
        dim = sys.argv[8]
        iterations = sys.argv[9]
        os.chdir(exe_path)
        print 'START: '+out_libfm
        libfm_BS(tr,te,out_libfm,'r',me,dim,rel,iterations)
        print 'Finish: '+out_libfm

