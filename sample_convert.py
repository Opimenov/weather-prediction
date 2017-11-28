#Script to convert the sample data already generated to npy files

import pandas as pd
import numpy as np

meteo_vars = ['pw','t850','v850','u850','v300','u300','z1000','z500','z300']

for i in range(0,9):
    df1 = pd.read_csv('./sample_data/generated/csv_format/%s__0.csv'%(meteo_vars[i]),header=None)
    df2 = pd.read_csv('./sample_data/generated/csv_format/%s__9.csv' % (meteo_vars[i]),header=None)
    print('read in %s variables\n' % (meteo_vars[i]))
    df2 = df2.tail(9)
    df2.index = range(11314, 11323)
    df1 = df1.append(df2)
    np.save(file=('./sample_data/generated/npy_format/preproc_data2/%s.npy' % (meteo_vars[i])), arr=df1.as_matrix())
    print('%s variables saved\n' %(meteo_vars[i]))
	
#Note that this will be smaller than the npy files provided, since they're
#aren't stored as strings... I don't know if this is good or bad...
