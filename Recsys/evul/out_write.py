import numpy as np


def out_format_1(ofp,data_id,method,evul,result):
    fn = ofp + '%s_%s_%02d_file.csv'%(evul,method,data_id)
    print fn
    f = open(fn,'w')
    f.write('ID,TAR,DIM,FEA,TS1,TS2,TS3,Avg_TS1_2\n')
    for fn in sorted(result.keys()):
        PAR = fn.split('_')
        ID = PAR[1]
        TAR = PAR[3]
        DIM = PAR[5].split(',')[-1]
        FEA = PAR[7]
        for i in range(8,len(PAR)-1):
            FEA = FEA + '-' +PAR[i]

        #feature
        AVG_TS = {}
        for TS in sorted(result[fn].keys()):
            if 'RMSE' in evul:
                RMSE = np.sqrt(result[fn][TS].mean())
                f.write('%.4f,'%( np.sqrt(result[fn][TS].mean()) ) )
                AVG_TS[TS]=RMSE
            if 'NDCG' in evul:
                NDCG = np.array(result[fn][TS].items())[:,1].mean()
                AVG_TS[TS]=NDCG
                f.write('%.4f,'%(NDCG) )

        f.write('%s,%s,%s,%s'%(ID,TAR,DIM,FEA))
        AVG_TS = (AVG_TS['TS1']+AVG_TS['TS2'])/2
        #f.write(',%.4f'%(AVG_TS) )
        f.write('\n')
    f.close()





