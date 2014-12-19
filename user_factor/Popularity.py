import numpy as np

def us_pop(UID_dict,SID_pop):

    #user popularity
    UID_pop_dict = []
    for i in UID_dict.keys():
        uid_pop = 0
        for j in UID_dict[i]:
            uid_pop += SID_pop[j]

        UID_pop_dict.append( uid_pop/len(UID_dict[i]) )
    return np.array(UID_pop_dict)
