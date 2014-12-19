import numpy as np
import time,glob,os
from collections import Counter

def RMSE(true,pred):
    #Root mean square error
    MSE_val = ((pred - true) ** 2).mean()
    RMSE_val = np.sqrt(MSE_val)
    return RMSE_val

def song_idx(pred_song_file):
    pred_song_idx={}
    with open(pred_song_file) as f:
        pred_song = map(int,f.readlines())
    for idx,val in enumerate(pred_song):
        try:
            pred_song_idx[val].append(idx)
        except:
            pred_song_idx[val]=[]
            pred_song_idx[val].append(idx)
    return pred_song_idx
def Rank_song(true,pred,pred_song_file):
    pred_song_idx = song_idx(pred_song_file)
    sid = np.sort(pred_song_idx.keys())
    True_pc = []
    Pred_pc = []
    for i in sid:
        True_pc.append(true[pred_song_idx[i]].sum())
        Pred_pc.append(pred[pred_song_idx[i]].sum())

    True_rank = sid[np.argsort(True_pc)][::-1]
    Pred_rank = sid[np.argsort(Pred_pc)][::-1]
    return True_rank,Pred_rank
import pickle
import numpy as np
def write_topsong(target_fn,sid_fn,topsong_fn):
    with open(target_fn) as f:
        pred = np.array(f.readlines()).astype(float)
    pred_song_idx = song_idx(sid_fn)
    sid = np.sort(pred_song_idx.keys())
    Pred_pc = []
    for i in sid:
        Pred_pc.append(pred[pred_song_idx[i]].sum())

    Pred_rank = sid[np.argsort(Pred_pc)][::-1]
    with open('/home/fearofchou/data/KKBOX/stats/song_meta.dict') as f:
        song_meta = pickle.load(f)
    song_id = sorted(np.load('/home/fearofchou/data/KKBOX/stats/AW_song_id.npy'))
    f=open(topsong_fn,'w')

    sort_idx = np.argsort(Pred_pc)
    playcount = np.array(Pred_pc)[sort_idx][::-1]
    Show_meta = ['song_name','artist_name','release','genre']
    for idx,i in enumerate(Pred_rank):
        f.write(str(playcount[idx])+'\t')
        for sm in Show_meta:
            f.write(song_meta[song_id[i]][sm]+'\t')
        f.write('\n')
    f.close()





def AP_k(true,pred,k):
    if len(pred) > k:
        pred = pred[:k]
    if len(true) > k:
        true = true[:k]

    score = 0.0
    num_hits = 0.0

    for i,p in enumerate(pred):
        if p in true and p not in pred[:i]:
            num_hits += 1.0
            score += num_hits / (i + 1.0)
            #print score

    apk = score / min(len(true),k)

    return apk

def read_true_pred(pred_fp,true_fn,pred_fn):
    with open(pred_fp+true_fn) as f:
        true = np.array(f.readlines()).astype(float)
    with open(pred_fn) as f:
        pred = np.array(f.readlines()).astype(float)

    return true,pred

def chechk_result_file(fn,metric):
    with open(fn,'w') as f:
        f.write('Features,'+metric+'\n')

if __name__ == '__main__':
    #all path
    trte_fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/'
    split_type = ['split_by_random','split_by_month']
    split_time = ['short_term_playcount','long_term_playcount','long_term_playcount_mean']
    T_fp = []
    for sty in split_type:
        for sti in split_time:
            T_fp.append(trte_fp+sty+'/'+sti+'/')

    #PMSE
    out_RMSE = '/home/fearofchou/data/KKBOX/libfm/out_result/'
    out_fn = out_RMSE+'RMSE.csv'
    f = open(out_fn,'w')
    f.write('RMSE---Features\n')

    for pred_fp in T_fp:
        p = pred_fp.split('/')
        print 'exe:%s---%s'%(p[-3],p[-2])
        f.write('%s---%s\n'%(p[-3],p[-2]))
        FL = sorted(glob.glob(pred_fp+'ID*'))
        for pred_fn in FL:
            f_ID = pred_fn[len(pred_fp)+3:len(pred_fp)+5]
            true_fn = 'rel_target_%s.test'%(f_ID)
            true,pred = read_true_pred(pred_fp,true_fn,pred_fn)
            f.write('%0.4f---%s\n'%(RMSE(true,pred),pred_fn.split('/')[-1]))
    f.close()

    with open(out_fn) as f:
        print f.read()
    '''
    #mAP top pop song
    k = [10,50,100,500,1000]
    T_fp=[]
    for sti in split_time:
        T_fp.append(trte_fp+split_type[1]+'/'+sti+'/')
    out_fp = '/home/fearofchou/data/KKBOX/libfm/out_result/'
    out_fn = out_fp+'mAP_TopSong.csv'
    f = open(out_fn,'w')
    f.write('Features,mAP,k\n')
    for pred_fp in T_fp:
        print 'mAP'+pred_fp
        FL = sorted(glob.glob(pred_fp+'ID*'))
        for pred_fn in FL:
            f_ID = pred_fn[len(pred_fp)+3:len(pred_fp)+5]
            true_fn = 'rel_target_%s.test'%(f_ID)
            sid = 'rel_sid_%s.test'%(f_ID)
            true,pred = read_true_pred(pred_fp,true_fn,pred_fn)
            True_rank,Pred_rank = Rank_song(true,pred,pred_fp+sid)
            for mapk in k:
                mAP_k = AP_k(True_rank,Pred_rank,mapk)
                f.write('%s,%0.4f,%d\n'%(pred_fn,mAP_k,mapk))
    f.close()

    #baseline
    fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount/'
    fn = 'rel_target_11.train'
    true,pred = read_true_pred(fp,'rel_target_11.test',fp+fn)
    sid = 'rel_sid_11.test'
    True_rank,a = Rank_song(true,true,fp+sid)
    sid = 'rel_sid_11.train'
    a,Pred_rank = Rank_song(pred,pred,fp+sid)
    print Pred_rank[:10]
    P_rank=[]
    for i in Pred_rank:
        if i in True_rank:
            P_rank.append(i)
    Pred_rank = np.array(P_rank)
    print Pred_rank[:10]
    k = [10,50,100,500,1000]
    for mapk in k:
        mAP_k = AP_k(True_rank,Pred_rank,mapk)
        #f.write('%s,%0.4f,%d\n'%(pred_fn,mAP_k,mapk))
        print mAP_k
    '''
