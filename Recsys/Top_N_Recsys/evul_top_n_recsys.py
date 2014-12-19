import numpy as np
import sys
sys.path.append('/home/fearofchou/code/user_factor')
import Diversity as DIV
import Freshness as FRE
import Popularity as POP
import Adventurousness as ADV

div_N_val = {}
fre_N_val = {}
pop_N_val = {}
adv_N_val = {}

ran_N = range(0,1050,50)
ran_N[0] +=10
for N in ran_N:
    UID_N_rank = {}
    for fn in UID_rank.keys():
        UID_N_rank[fn] = {}
        for i in UID_rank[fn]:
            UID_N_rank[fn][i] = UID_rank[fn][i][:N]
    div_N_val[N] = {}
    fre_N_val[N] = {}
    adv_N_val[N] = {}
    pop_N_val[N] = {}
    print 'N = %d'%(N)
    print 'fn--div--fer--pop--adv\n'
    for fn in UID_N_rank.keys():
        fre_val = FRE.us_fre(UID_N_rank[fn],song_info,real_sid)
        pop_val = POP.us_pop(UID_N_rank[fn],SID_pop)
        div_val = DIV.us_div(UID_N_rank[fn],song_info,real_sid)
        adv_val = ADV.us_adv(UID_AID_tr_dict,UID_N_rank[fn],song_info,real_sid)
        print '%s'%(fn.split('/')[-1]),
        print '--%.4f'%(div_val.mean()),
        print '--%d'%(fre_val.mean()),
        print '--%d'%(pop_val.mean()),
        print '--%.3f'%(adv_val.mean())
        div_N_val[N][fn] = div_val.mean()
        fre_N_val[N][fn] = fre_val.mean()
        adv_N_val[N][fn] = adv_val.mean()
        pop_N_val[N][fn] = pop_val.mean()




'''
print 'fn,div,fer,pop\n'
for fn in pred_fn.keys():
    pop_val = POP.us_pop(UID_rank[fn],SID_dict_pop)
    div_val = DIV.us_div(UID_rank[fn],song_meta,real_sid)
    fre_val = FRE.us_fre(UID_rank[fn],song_meta,real_sid)
    idx = pop_val!=0
    pop_val = pop_val[idx]
    fre_val = fre_val[idx]
    div_val = div_val[idx]
    #pop_val = (pop_val[idx] - pop_val[idx].min()) / ( pop_val[idx].max()-pop_val[idx].min()  )
    #div_val = (div_val[idx] - div_val[idx].min()) / ( div_val[idx].max()-div_val[idx].min()  )
    #fre_val = (fre_val[idx] - fre_val[idx].min()) / ( fre_val[idx].max()-fre_val[idx].min()  )
    print 'org|%s,%f,%f,%f\n'%(fn.split('/')[-1],div_val.mean(),fre_val.mean(),pop_val.mean())

    pop_val = (pop_val - pop_val.min()) / ( pop_val.max()-pop_val.min()  )
    div_val = (div_val - div_val.min()) / ( div_val.max()-div_val.min()  )
    fre_val = (fre_val - fre_val.min()) / ( fre_val.max()-fre_val.min()  )

    print 'norm|%s,%f,%f,%f\n'%(fn.split('/')[-1],div_val.mean(),fre_val.mean(),pop_val.mean())

A_SID = {}
A_SID[0] = lis_sid

pop_val = POP.us_pop(A_SID,SID_dict_pop)
div_val = DIV.us_div(A_SID,song_meta,real_sid)
fre_val = FRE.us_fre(A_SID,song_meta,real_sid)
print 'base|%s,%f,%f,%f\n'%(fn.split('/')[-1],div_val.max(),fre_val.max(),pop_val.max())
'''

