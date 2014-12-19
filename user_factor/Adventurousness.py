import numpy as np

#tran to artist id
def tran_to_sid2aid(UID_SID_tr_dict,song_info,real_sid):
    UID_AID_dict = {}
    for uid in UID_SID_tr_dict:
        UID_AID_dict[uid] = {}
        for sid in UID_SID_tr_dict[uid]:
            AID = song_info[ real_sid[sid] ]['artist_id']
            try:
                UID_AID_dict[uid].append(AID)
            except:
                UID_AID_dict[uid] = [AID]

    return UID_AID_dict

def us_adv(UID_AID_tr_dict,UID_rank,song_info,real_sid):
    UID_AID_rank = tran_to_sid2aid(UID_rank,song_info,real_sid)
    ADV_dict = []
    for uid in UID_rank:
        un_aid = np.unique(UID_AID_rank[uid])
        re_songs = len(set(un_aid).difference(UID_AID_tr_dict[uid]))
        ADV_dict.append(re_songs/float(len(un_aid)))
    return np.array(ADV_dict)

