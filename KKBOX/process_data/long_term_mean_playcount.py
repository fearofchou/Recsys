import numpy as np
import sys
sys.path.append('/home/fearofchou/code/KKBOX/stats/')
import stats
from sklearn import cross_validation
def write_tr_te(data,tr_te):
    uf = open(FP+'rel_uid_00.%s'%(tr_te),'w')
    sf = open(FP+'rel_sid_00.%s'%(tr_te),'w')
    tf = open(FP+'rel_target_00.%s'%(tr_te),'w')
    for log in data:
        log = log.split('-')
        uid = log[0]
        sid = log[1]
        tar = np.mean(STMP['%s-%s'%(uid,sid)])
        uf.write('%s\n'%(uid))
        sf.write('%s\n'%(sid))
        tf.write('%d\n'%(tar))
#need to run KKBOX_load
def combine_to_dict(SM_data):
    #combine in dict
    # ex: data[uid][sid]=playcount
    listeing_date = sorted(SM_data['uid'].keys())
    FP = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_random/long_term_playcount_mean/'
    STMP = {}
    for idx,ld in enumerate(listeing_date):
        print ld
        tr_te = 'test'
        uid =  SM_data['uid'][ld]
        sid =  SM_data['sid'][ld]
        tar =  SM_data['target'][ld]

        for idx in range(len(uid)):
            ll = '%d-%d'%(uid[idx],sid[idx])
            try:
                STMP[ll].append(tar[idx])
            except:
                STMP[ll] =[tar[idx]]
    T_sid = []
    for i in STMP.keys():
        T_sid.append(i.split('-')[-1])
    return STMP,np.array(T_sid)

#STMP,T_sid = combine_to_dict(SM_data)


for i in range(1):
    tr_te_spd = cross_validation.train_test_split(range(len(STMP.keys())),test_size=0.1)
    NL_idx,NL_sid = stats.find_never_listen_idx(T_sid[tr_te_spd[1]],T_sid[tr_te_spd[0]])
    print len(NL_sid)
    if len(NL_sid)<1000:
        break
SK = np.array(STMP.keys())
write_tr_te(SK[tr_te_spd[0]],'train')
write_tr_te(SK[tr_te_spd[1]],'test')


