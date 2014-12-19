import numpy as np
import time
def us_fre(UID_dict,song_meta,real_sid):
    UID_fre_dict = []
    for i in UID_dict.keys():
        uid_fre = 0
        c_fre = 0
        for j in UID_dict[i]:
            c_fre += 1
            rel = song_meta[real_sid[j]]['release']
            ts = time.mktime(time.strptime(rel, '%Y-%m-%d'))
            #rel = rel[0]*10000 + rel[1]*100 +rel[2]
            uid_fre += ts

        UID_fre_dict.append(uid_fre / float(c_fre) )
    #UID_fre_dict = UID_fre_dict / UID_fre_dict.max()
    return np.array(UID_fre_dict)
