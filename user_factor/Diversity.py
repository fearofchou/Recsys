import numpy as np

def trans_to_genre_hist(UID_dict,song_meta,real_sid):
    UID_genre_dict = {}
    error = 0
    for idx,val in enumerate(UID_dict.keys()):
        UID_genre_dict[val] = np.zeros(32)

        for sid in UID_dict[val]:
            genre = song_meta[real_sid[sid]]['genre']
            try:
                genre = np.array(genre.split(',')).astype(int)
            except:
                error+=1
                continue
            for g in genre:
                UID_genre_dict[val][g]+=1
    return UID_genre_dict

def us_div(UID_dict,song_meta,real_sid):
    UID_genre_dict = trans_to_genre_hist(UID_dict,song_meta,real_sid)
    import scipy.stats as ss
    UID_div_dict = []
    for idx,uid in enumerate(UID_genre_dict.keys()):
        UID_div_dict.append(ss.entropy(UID_genre_dict[uid]))
    UID_div_dict = np.array(UID_div_dict)
    a= np.isnan(UID_div_dict)
    UID_div_dict[a]=0

    return UID_div_dict
