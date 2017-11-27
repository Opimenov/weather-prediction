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
	
for day in range(0,4):
	for f in range(0, 9):
		
		data = np.load('./preproc_data2/%s.npy' % (meteo_vars[f]))
		ddata = data[offset+day:time+offset+day,:]
		karr = np.empty(0)
		karri = 0
		for loc in range (0, locations):
			# TODO: Preserve location number in array so it can be mapped later
			ti = pd.DataFrame(ddata[:,loc])
			
			z = zs(c, ti)
			
			if abs(z) < 1.96:
				continue
			
			# Ugly bad hack in order to grow data frame from nothing
			# There might be a better way to do this, I don't know pandas or
			# python very well
			
			#TODO: Test this part...
			
			# In the first loop we label all features that have some sort of
			# correlation with 
			#pdb.set_trace()
			
			if st[day].shape[0] == 0  and karr.shape[0] == 0:
				karr = ti.as_matrix()
				karri = loc
			elif st[day].shape[0] == 0:
				pdb.set_trace()
				st[day] = pd.DataFrame(np.concatenate((karr, ti.as_matrix()), axis=1))
			else:
				pdb.set_trace()
				st[day] = pd.concat([st[day], ti], axis=1)
			# In subsequent loops, we either prune features from the previous
			# set of features or discard the current feature depending on 
			# how previous features and the current feature correlate with
			# the class attribute and each other
			if day != 0:
				if disc_prune(ti, st[day-1]) == False:
					continue
				else:
					st[day] = st[day].concat(ti, axis=1)
					
					
				
		
