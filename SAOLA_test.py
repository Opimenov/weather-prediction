import numpy as np
import pandas as pd
import pdb

# note: zs function has been tested
# Takes two pandas frames as arguments
def zs(crf1, crf2):
	# Pearson correlation coefficient, r
	r = crf1[0].corr(crf2[0])
	# Fisher Z transformation on r'
	rp = np.arctanh(r)
	# Standard Error Calculation for transformed correlation r'
	N = time
	srp = 1/((N - 3.0)**(0.5))
	return rp/srp
	
# Discard feature or prune features from the previous set based on current feature
	
def disc_prune(fi, st1):
	# Probably kind of bad to refer to c as a free var here but whatever
	
	# iterate across the features stored in the selected feature set
	for i in st1.shape[1]:
		y = st1[i]
		
		if abs(zs(y, c)) > abs(zs(fi, c)) and abs(zs(fi, y)) > 1.96:
			return False
		
		if abs(zs(fi, c)) > abs(zs(y, c)) and abs(zs(fi, y)) > 1.96:
			st1.drop(i, axis=1)
	
meteo_vars = ['pw','t850','v850','u850','v300','u300','z1000','z500','z300']

target = np.load('./preproc_data2/target_1980_2010.npy')
#Data frame of feature attributes, c
c = pd.DataFrame(target[:,0])

#Feature set at time st
st = [pd.DataFrame([]), pd.DataFrame([]), pd.DataFrame([]), pd.DataFrame([])]

# Total number of locations
locations = 5328
# Historical data time frame
time = 11300
# Offset of days
offset = 6	
	
-
					
					
				
		
