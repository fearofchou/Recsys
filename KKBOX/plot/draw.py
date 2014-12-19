import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import glob

test_fp ='/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/'
fmp_term = ['short','long']
fmp_split = ['month','random']
test_fmp = 'split_by_%s/%s_term_playcount/'%(fmp_split[0],fmp_term[0])
data_id = 11
test_fn = 'rel_target_%2d.test'%(data_id)

def read_file(fn):
    with open(fn,'r') as f:
        ans = np.array(f.readlines()).astype(float)

    return ans

print test_fp+test_fmp+test_fn
true = read_file(test_fp+test_fmp+test_fn)
#true = np.log2(true+1)

pred_fl = glob.glob('%s%sID_%02d*'%(test_fp,test_fmp,data_id))

ax = plt.gca()
ax.set_xticks(np.arange(0,len(true),100000))

for fl in pred_fl:
    pl_true, = plt.plot(true,'r',label = 'True playcount')
    pred = read_file(fl)
    #pred = np.log2(pred+1)
    pl_pred, = plt.plot(pred,'b',label = 'Pred playcount')
    fn = fl.split('/')[-1]
    fn = fn.split('.')[0]+'_'+fn.split('.')[1]
    plt.legend(loc=1)
    plt.savefig(fn)


