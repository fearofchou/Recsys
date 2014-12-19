import subprocess
import os,time
run_exe = 'python ./libfm_flow.py'
import popen_libfm as LP
#def libfm_popen(ofp,data_id,norm_tar,para):

#feature
norm = 'binpos'
n=5
features = ['rel_sid.lib','rel_AW.lib','rel_AW3R.lib','rel_AW_mood.lib'\
            ,'rel_AW_genre.lib','rel_AW_acoustic.lib','rel_MFCC.lib'\
            ,'rel_AW_%s_%d.lib'%(norm,n),\
            'rel_AW_acoustic_%s_%d.lib'%(norm,n),\
            'rel_AW_genre_%s_%d.lib'%(norm,n),\
            'rel_AW_mood_%s_%d.lib'%(norm,n),\
            'rel_MFCC_%s_%d.lib'%(norm,n)]
fea_id = [0,-1,-2,-3,-4,-5]
fea2_id = [-1,-2,-3,-4,-5]
nroot = [5]
user_fea = 'rel_uid.lib'
#file
data_id = 99
#target
norm_tar = ['org','5Ilog2p1','log2p1','5I']
#libfm par
#dim = '1,1,8'
#iterations = str(50)
dim_k = [8]
iter_k = [50]
para = {}
idx = 0
for n in nroot:
    for i in iter_k:
        for d in dim_k:
            for f in fea_id:
                para[idx] = {}
                para[idx]['fea'] = user_fea+','+features[f]
                para[idx]['ite'] = str(i)
                para[idx]['dim'] = '1,1,%d'%(d)
                idx += 1
            for f in fea2_id:
                para[idx] = {}
                para[idx]['fea'] = user_fea+','+features[0]+','+features[f]
                #para[idx]['fea'] = user_fea+','+features[0]+','+features[-2]+','+features[-3]+','+features[f]
                para[idx]['ite'] = str(i)
                para[idx]['dim'] = '1,1,%d'%(d)
                idx += 1

ofp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS'+ \
        '/split_by_month/long_term_playcount_mean/libfm_out_recsys/'

LP.libfm_popen(ofp,data_id,norm_tar[2],para)




