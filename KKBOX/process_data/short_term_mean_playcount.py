import numpy as np
#need to run KKBOX_load

#combine in dict
# ex: data[uid][sid]=playcount
listeing_date = sorted(SM_data['uid'].keys())
FP = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/'

#write data
for ld_idx,ld in enumerate(listeing_date):
    #test
    print ld
    tr_te = 'test'
    uid =  SM_data['uid'][ld]
    sid =  SM_data['sid'][ld]
    tar =  SM_data['target'][ld]
    u_f = open(FP+'rel_uid_%02d.%s'%(ld_idx,tr_te),'w')
    s_f = open(FP+'rel_sid_%02d.%s'%(ld_idx,tr_te),'w')
    t_f = open(FP+'rel_target_%02d.%s'%(ld_idx,tr_te),'w')
    for idx in range(len(uid)):
        u_f.write(str(uid[idx])+'\n')
        s_f.write(str(sid[idx])+'\n')
        t_f.write(str(tar[idx])+'\n')

    #mean playcount in training
    STMP = {} #short-term mean playcount
    for tr_ld in listeing_date:
        if tr_ld == ld:
            continue

        uid =  SM_data['uid'][tr_ld]
        sid =  SM_data['sid'][tr_ld]
        tar =  SM_data['target'][tr_ld]

        for idx in range(len(uid)):
            ll = '%d-%d'%(uid[idx],sid[idx])
            try:
                STMP[ll].append(tar[idx])
            except:
                STMP[ll] =[tar[idx]]

    #write training
    tr_te = 'train'
    u_f = open(FP+'rel_uid_%02d.%s'%(ld_idx,tr_te),'w')
    s_f = open(FP+'rel_sid_%02d.%s'%(ld_idx,tr_te),'w')
    t_f = open(FP+'rel_target_%02d.%s'%(ld_idx,tr_te),'w')
    for log in sorted(STMP.keys()):
        log = log.split('-')
        uid = log[0]
        sid = log[1]
        tar = np.mean(STMP['%s-%s'%(uid,sid)])
        u_f.write(str(uid)+'\n')
        s_f.write(str(sid)+'\n')
        t_f.write(str(tar)+'\n')



