import os
import numpy as np
import scipy.io
import pickle
import glob


def Read_AW_feature_mat(AW_path,out_fn):
    AW_FL = os.listdir(AW_path)
    AW_dict = {}
    for idx,f in enumerate(AW_FL):
        AW_feature = scipy.io.loadmat(AW_path + f)['data']
        #sparse
        #AW_dict[int(f[:-4])] = np.array(AW_feature.todense()).reshape(-1)
        AW_dict[int(f[:-4])] = np.squeeze(AW_feature)
        print str(idx)+'-'+str(len(AW_FL))

    with open(out_fn,'wb') as handle:
        pickle.dump(AW_dict,handle)

def Read_Fea_csv(MAG_path,fea_name,out_path):
    FL= os.listdir(MAG_path + fea_name)
    Fea_dict = {}
    for idx,f in enumerate(FL):
        print str(idx) + '-' + str(len(FL))
        with open(MAG_path + fea_name + f,'r') as h:
            data = h.readlines()

        Fea_dict[int(f[:-4])] = np.array(map(float,data[0][:-1].split(',')))

    with open(out_path,'wb') as f:
        pickle.dump(Fea_dict,f)

if __name__ == '__main__':
    #MAG_path = '/home/fearofchou/network_drive/MAC_198/masked/predicted_label/spectrum_ODL_4096_SC_USPOP_polar_simple/'
    #AW_path = '/home/fearofchou/network_drive/MAC_198/masked/feature/spectrum_ODL_4096_SC_USPOP_polar_simple/'
    MFCC_fp = '/home/fearofchou/test/masked/feature/MFCC/'
    out_path = '/home/fearofchou/data/KKBOX/feature/'
    #Read_Fea_csv(MAG_path,'CAL10k/',out_path+'rel_genre')
    #Read_Fea_csv(MAG_path,'CAL10kA/',out_path+'rel_acoustic')
    #Read_Fea_csv(MAG_path,'MER31k/',out_path+'rel_mood')

    Read_AW_feature_mat(MFCC_fp,out_path+'rel_MFCC.dict')


