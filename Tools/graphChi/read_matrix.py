import numpy as np

fp = '/home/fearofchou/data/KKBOX/graphchi/'
fn = 'rel_11_train.graphchi'


#def out_to_Ma(fn):
with open(fp+fn+'_U.mm') as f:
    UF = f.readlines()
with open(fp+fn+'_V.mm') as f:
    VF = f.readlines()


U_TN = np.int_(UF[2].split(' '))[0]
U_FN = np.int_(UF[2].split(' '))[1]

U_FM = np.zeros([U_TN,U_FN])

for i in range(3,len(UF)):
    U_FM[i-3] = np.float_(UF[i].split(' ')[:-1])

V_TN = np.int_(VF[2].split(' '))[0]
V_FN = np.int_(VF[2].split(' '))[1]
V_FM = np.zeros([V_TN,V_FN])

for i in range(3,len(VF)):
    V_FM[i-3] = np.float_(VF[i].split(' ')[:-1])
