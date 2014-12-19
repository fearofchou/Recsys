import glob,sys
sys.path.append('/home/fearofchou/code/KKBOX/Resys/')
sys.path.append('/home/fearofchou/code/KKBOX/stats/')
import evul,stats
import numpy as np
def NL_RMSE_multi(pred_path,data_id):
    pred_fl = glob.glob(pred_path+'ID_%02d*'%(data_id))
    with open(pred_path+'rel_sid_%02d.train'%(data_id)) as f:
        train_sid= np.array(f.readlines()).astype('int')
    with open(pred_path+'rel_sid_%02d.test'%(data_id)) as f:
        test_sid = np.array(f.readlines()).astype('int')

    with open(pred_path+'rel_target_%02d.test'%(data_id)) as f:
        true = np.array(f.readlines()).astype('float')

    NL_sid_idx,HL_idx,  NL_sid = stats.find_never_listen_idx(test_sid, train_sid)
    print 'NL_sid:%d NL_records:%d'%(len(NL_sid),len(NL_sid_idx))
    for fn in pred_fl:
        with open(fn) as f:
            pred= np.array(f.readlines()).astype('float')

        print evul.RMSE(pred[NL_sid_idx],true[NL_sid_idx])
        print fn.split('/')[-1]
    return NL_sid_idx





