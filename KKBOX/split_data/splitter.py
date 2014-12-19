from sklearn import cross_validation
import os
import numpy as np
FP = '/home/fearofchou/data/KKBOX/libfm/filter_data_BS/month_sid/'

def Read_all_log_data(FP):
    FL = os.listdir(FP)
    FT = ['uid','sid','target']
    DATA = {}
    for ftype in FT:
        DATA[ftype]={}
    #read all log data
    for idx,fn in enumerate(FL):
        print str(idx)+'-'+str(len(FL))
        for ftype in FT:
            if ftype in fn:
                with open(FP+fn) as f:
                    DATA[ftype][fn[-15:]] = map(int,f.readlines())
                continue

    return DATA

def month_short_term_playcount(DATA,out_fp):
    tr_te = ['train','test']
    for ft in DATA.keys():
        for idx,fn in enumerate(sorted(DATA[ft].keys())):
            print ft+':'+fn
            #test
            f = open(out_fp+'rel_%s_%02d.test'%(ft,idx),'w')
            for data in DATA[ft][fn]:
                f.write(str(data)+'\n')
            f.close()
            #train
            train_fi = set(DATA[ft].keys()).difference([fn])
            f = open(out_fp+'rel_%s_%02d.train'%(ft,idx),'w')
            for tfi in train_fi:
                for data in DATA[ft][tfi]:
                    f.write(str(data)+'\n')
            f.close()


import random
def short_term_playcount(DATA,out_fp,ts):
    tr_te = ['train','test']
    STP = {}
    for ft in DATA.keys():
        STP[ft]=[]
        for fn in DATA[ft].keys():
            STP[ft].extend(DATA[ft][fn])
    le_dt = len(STP[ft])
    print le_dt
    data_idx={}
    data_idx['test'] = random.sample(range(le_dt),int(np.floor(le_dt*ts)))
    print len(data_idx['test'])
    data_idx['train'] = set(range(le_dt)).difference(data_idx['test'])
    print len(data_idx['train'])
    for trte in tr_te:
        for ftn in DATA.keys():
            out_fn = 'rel_%s_%02d.%s'%(ftn,0,trte)
            f = open(out_fp+out_fn,'w')
            for idx in data_idx[trte]:
                f.write(str(STP[ftn][idx])+'\n')
            f.close()


from sklearn import cross_validation
def random_split(DATA,ts):
    #combine playcount
    U_I_R = {} #user item rating dictionary
    All_fn = DATA['uid'].keys()
    for idx,fn in enumerate(All_fn):
        print str(idx)+'-'+str(len(All_fn))
        for uid,sid,tar in zip(DATA['uid'][fn],DATA['sid'][fn],DATA['target'][fn]):
            try:
                U_I_R[str(uid)+':'+str(sid)] += tar
            except:
                U_I_R[str(uid)+':'+str(sid)] = tar

    All_row = U_I_R.keys()
    R_train,R_test = cross_validation.train_test_split(All_row,test_size=ts,random_state=0)

    tr_te = ['train','test']
    R_data = {}
    R_data[0]={}
    for trte in tr_te:
        R_data[0]['train']={}
        R_data[0]['test']={}
        for tr in R_train:
            R_data[0]['train'][tr] = U_I_R[tr]
        for te in R_test:
            R_data[0]['test'][te] = U_I_R[te]

    return R_data

#DATA = Read_all_log_data(FP)

def month_split(DATA):
    #combine playcount
    U_I_R = {} #user item rating dictionary
    All_fn = DATA['uid'].keys()
    sort_fn = sorted(All_fn)

    for idx,fn in enumerate(sort_fn):
        print str(idx)+'-'+str(len(All_fn))
        U_I_R[idx]={}
        U_I_R[idx]['train'] = {}
        U_I_R[idx]['test'] = {}
        #for test to dict
        for uid,sid,tar in zip(DATA['uid'][fn],DATA['sid'][fn],DATA['target'][fn]):
            try:
                U_I_R[idx]['test'][str(uid)+':'+str(sid)] += tar
            except:
                U_I_R[idx]['test'][str(uid)+':'+str(sid)] = tar
        #for train to dict
        tr_fn = set(sort_fn).difference([fn])
        print fn
        print tr_fn
        for tfn in tr_fn:
            for uid,sid,tar in zip(DATA['uid'][tfn],DATA['sid'][tfn],DATA['target'][tfn]):
                try:
                    U_I_R[idx]['train'][str(uid)+':'+str(sid)] += tar
                except:
                    U_I_R[idx]['train'][str(uid)+':'+str(sid)] = tar
    return U_I_R

#U_I_R = month_split(DATA)

def write_UIR_to_BS_format(U_I_R,out_fp):
    tr_te = ['train','test']
    FT = ['uid','sid','target']
    UIR_val = {}
    UIR_f = {}
    for idx in U_I_R.keys():
        print idx
        for trte in tr_te:
            for ftn in FT:
                out_fn = 'rel_%s_%02d.%s'%(ftn,idx,trte)
                UIR_f[ftn] = open(out_fp+out_fn,'w')

            for UI in U_I_R[idx][trte].keys():
                U_I = UI.split(':')
                UIR_val[FT[0]] = U_I[0]
                UIR_val[FT[1]] = U_I[1]
                UIR_val[FT[2]] = U_I_R[idx][trte][UI]
                for ftn in FT:
                    UIR_f[ftn].write(str(UIR_val[ftn])+'\n')

            for ftn in FT:
                UIR_f[ftn].close()


#out_fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount/'
#write_UIR_to_BS_format(U_I_R,out_fp)
#def split_month(DATA):


