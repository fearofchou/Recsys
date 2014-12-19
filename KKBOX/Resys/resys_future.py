import os
import numpy as np

def cross_by_month(file_path):
    file_list = os.listdir(file_path)
    file_list = sorted(file_list)

    uid_data = {}
    sid_data = {}
    tar_data = {}
    uc = 0
    sc = 0
    tc = 0
    for i in file_list:
        if 'uid' in i:
            with open(file_path + i,'r') as f:
                uid_data[uc] = f.read()
            uc += 1
        if 'sid' in i:
            with open(file_path + i,'r') as f:
                sid_data[sc] = f.read()
            sc += 1
        if 'target' in i:
            with open(file_path + i,'r') as f:
                tar_data[tc] = f.read()
            tc += 1

    cv_path = '/home/fearofchou/data/KKBOX/libfm/feature_BS/'
    for i in range(uc):
        with open('%srel_uid_%02d.test'%(cv_path,i),'w') as te:
            te.write(uid_data[i])
        with open('%srel_sid_%02d.test'%(cv_path,i),'w') as te:
            te.write(sid_data[i])
        with open('%srel_target_%02d.test'%(cv_path,i),'w') as te:
            te.write(tar_data[i])
        tr_uid = open('%srel_uid_%02d.train'%(cv_path,i),'w')
        tr_sid = open('%srel_sid_%02d.train'%(cv_path,i),'w')
        tr_tar = open('%srel_target_%02d.train'%(cv_path,i),'w')
        for j in range(uc):
            if i!=j:
                tr_uid.write(uid_data[j])
                tr_sid.write(sid_data[j])
                tr_tar.write(tar_data[j])

        tr_uid.close()
        tr_sid.close()
        tr_tar.close()

if __name__ == '__main__':
    file_path = '/home/fearofchou/data/KKBOX/libfm/'
    cross_by_month(file_path)


