from collections import Counter
import numpy as np


test_fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount/'
test_fn = 'rel_uid_11.test'
def Top_k_users_for_listen_song(test_fp,test_fn,k):
    with open(test_fp+test_fn) as f:
        uid = np.array(f.readlines()).astype(int)

    uid_number_of_listening_song = Counter(uid)
    user_id = np.sort(uid_number_of_listening_song.keys())
    user_pl = []
    for u in user_id:
        user_pl.append(uid_number_of_listening_song[u])
    user_pl = np.array(user_pl)
    sort_idx_user_pl = np.argsort(user_pl)[::-1]
    print user_pl[sort_idx_user_pl]
    print user_id[sort_idx_user_pl]

    return user_id[sort_idx_user_pl][:k],user_pl[sort_idx_user_pl][:k]

Top_user,Top_user_pl  = Top_k_users_for_listen_song(test_fp,test_fn,100)

#uid index sid


with open(test_fp+test_fn) as f:
    uid = np.array(f.readlines()).astype(int)
test_fn = 'rel_sid_11.test'
with open(test_fp+test_fn) as f:
    sid = np.array(f.readlines()).astype(int)

sid_index = {}
for idx,val in enumerate(uid):
    try:
        sid_index[val].append(idx)
    except:
        sid_index[val]=[idx]
Total_idx = []
for uid in Top_user:
    Total_idx.extend(sid_index[uid])
Total_idx = np.array(Total_idx)
C_sid = np.array(Counter(sid[Total_idx]).items())


