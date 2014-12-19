import numpy as np

fp = '/home/fearofchou/data/KKBOX/libmf/'
tr_fn = 'train_11'
te_fn = 'test_11'

#load libfm data
k = UID.keys()
FM = {}
FM['tr'] ={}
FM['te'] ={}

FM['tr']['tar'] = UID[k[0]]
FM['tr']['uid'] = UID[k[5]]
FM['tr']['sid'] = UID[k[3]]

FM['te']['tar'] = UID[k[1]]
FM['te']['uid'] = UID[k[2]]
FM['te']['sid'] = UID[k[4]]

#convert sid
sid_mask = {}
sm = 0
for i in FM['tr']['sid']:
    if i not in sid_mask:
        sid_mask[i] = sm
        sm +=1
for i in FM['te']['sid']:
    if i not in sid_mask:
        sid_mask[i] = sm
        sm +=1

#convert uid
uid_mask = {}
sm = 0
for i in FM['tr']['uid']:
    if i not in uid_mask:
        uid_mask[i] = sm
        sm +=1
for i in FM['te']['uid']:
    if i not in uid_mask:
        uid_mask[i] = sm
        sm +=1

#write train
f = open(fp+tr_fn,'w')
for idx,val in enumerate(FM['tr']['tar']):
    val = np.log2(val+1)
    if idx>1000000000:
        break
    f.write( "%d %d %f\n"%(uid_mask[FM['tr']['uid'][idx]],sid_mask[FM['tr']['sid'][idx]],val)  )
f.close()
# write test
f = open(fp+te_fn,'w')
for idx,val in enumerate(FM['te']['tar']):
    val = np.log2(val+1)
    if idx>1000000000:
        break
    f.write( "%d %d %f\n"%(uid_mask[FM['te']['uid'][idx]],sid_mask[FM['te']['sid'][idx]],val)  )
f.close()
