import numpy as np
import glob


def log2plus1(tar):
    return np.log2(tar+1)
def N_interval(uid,tar,uid_tar_max,N):
    N_tar = []
    for idx,val in enumerate(uid):
        N_tar.append( (tar[idx]/uid_tar_max[val])*N  )
    return np.array(N_tar)
def N_interval_log2p1(uid,tar,uid_tar_max,N):
    N_tar = []
    tar = np.log2(tar+1)
    for idx,val in enumerate(uid):
        N_tar.append( (tar[idx]/np.log2(uid_tar_max[val]+1))*N  )
    return np.array(N_tar)

fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/'
def load_target(fp):
    data_id = ['02','11']

    tar = {}
    uid = {}
    for did in data_id:
        fl = glob.glob(fp+'*target_%s.*'%(did))
        for fn in fl:
            with open(fn) as f:
                tar[fn.split('/')[-1].split('_')[-1]] = np.array(f.readlines()).astype(float)

        fl = glob.glob(fp+'*uid_%s.*'%(did))
        for fn in fl:
            with open(fn) as f:
                uid[fn.split('/')[-1].split('_')[-1]] = np.array(f.readlines()).astype(float)

    uk = sorted(uid.keys())
    tk = sorted(tar.keys())
    uid_tar = {}
    uid_tar_max = {}
    for idx,i in enumerate(uk):
        uid_tar[i] = {}
        uid_tar_max[i] = {}
        tar_idx = idx
        for idx,val in enumerate(uid[i]):
            try:
                uid_tar[i][val].append(tar[tk[tar_idx]][idx])
            except:
                uid_tar[i][val] = [tar[tk[tar_idx]][idx]]
        vk = uid_tar[i].keys()
        for j in vk:
            uid_tar_max[i][j] = max( uid_tar[i][j]  )

    return uid,tar,uid_tar_max
def write_file(fp,tar,of_name):
    f = open(fp+of_name,'w')
    for i in tar:
        f.write(str(i)+'\n')

uid,tar,uid_tar_max = load_target(fp)
k =uid.keys()

for i in k:
    '''
    logk = log2plus1(tar[i])
    of_name = 'rel_target_log2p1_'+i
    write_file(fp,logk,of_name)
    NIk = N_interval(uid[i],tar[i],uid_tar_max[i],5)
    of_name = 'rel_target_5I_'+i
    write_file(fp,NIk,of_name)
    '''
    NIk = N_interval_log2p1(uid[i],tar[i],uid_tar_max[i],5)
    of_name = 'rel_target_5Ilog2p1_'+i
    write_file(fp,NIk,of_name)

