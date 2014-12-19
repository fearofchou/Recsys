import numpy as np

def DCG(rank):
    PDCG = rank[0]
    for idx,val in enumerate(rank[1:]):
        PDCG += ( val/np.log2(idx+2) )
    return PDCG

def NDCG(rank):
    Irank = sorted(rank)[::-1]
    return DCG(rank)/DCG(Irank)

