import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
import pickle
import glob

def diff_month_feature(sid_dict,song_mask_id,song_meta):
    fp = '/home/fearofchou/data/KKBOX/fearure_extraction/song_age/'
    no_meta_sid = []
    for mn in sid_dict.keys():
        print mn
        fn = 'rel_songage_'+mn
        f = open(fp + fn,'w')
        for idx,sid in enumerate(sid_dict[mn]):
            rel_date = song_meta[song_mask_id[sid]]['release'].replace('-','')
            if rel_date == '':
                f.write(str(-99)+'\n')
                no_meta_sid.append(song_mask_id[sid])
                continue
            diff_year = int(mn[:4]) - int(rel_date[:4])
            diff_month = int(mn[4:6]) - int(rel_date[4:6])
            diff_year_month = diff_year*12 + diff_month
            if diff_year_month < 0:
                #f.write(str(0)+'\n')
                f.write(str(diff_year_month)+'\n')
            else:
                f.write(str(diff_year_month)+'\n')
        f.close()
    return no_meta_sid

def plt_month_playcount_same_month():
    rel_fl = glob.glob('/home/fearofchou/data/KKBOX/fearure_extraction/song_age/*songage*')
    tar_fl = glob.glob('/home/fearofchou/data/KKBOX/libfm/filter_data_BS/month_sid/*target*')
    uid_fl = glob.glob('/home/fearofchou/data/KKBOX/libfm/filter_data_BS/month_sid/*sid*')
    sid_fl = glob.glob('/home/fearofchou/data/KKBOX/libfm/filter_data_BS/month_sid/*uid*')
    rel_fl = sorted(rel_fl)
    tar_fl = sorted(tar_fl)
    sid_fl = sorted(sid_fl)
    uid_fl = sorted(uid_fl)

    sam_mon = {}
    sam_sid = {}
    for idx,val in enumerate(rel_fl):
        print  val
        with open(rel_fl[idx]) as f:
            rel = map(int,f.readlines())
        with open(tar_fl[idx]) as f:
            tar = map(int,f.readlines())
        with open(uid_fl[idx]) as f:
            uid = map(int,f.readlines())
        with open(sid_fl[idx]) as f:
            sid = map(int,f.readlines())

        for idx,val in enumerate(rel):
            try:
                sam_mon[val].append(tar[idx])
                sam_sid[val].append(sid[idx])
            except:
                sam_mon[val] = [tar[idx]]
                sam_sid[val] = [sid[idx]]
    pl_sum = []
    pl_sid = []
    diff_rel_m = np.sort(sam_mon.keys())
    for i in diff_rel_m:
        pl_sid.append(len(set(sam_sid[i])))
        pl_sum.append(sum(sam_mon[i]))

    month = np.array(diff_rel_m)
    m_pl = np.array(pl_sum)
    m_sid = np.array(pl_sid)

    return month,m_pl,m_sid
#def plot(m,p,s)
    #plt.plot(diff_rel_m,pl_sum,'ro')
    #plt.axis([mont,month_e,pl_s,pl_e])
    #plt.savefig('test')



