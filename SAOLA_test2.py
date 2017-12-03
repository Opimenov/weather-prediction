import numpy as np
import pandas as pd
import copy as cp
import pdb
import time as tm

# note: zs function has been tested
# Takes two pandas frames as arguments
def zs(crf1, crf2):
	#pdb.set_trace()
	# Pearson correlation coefficient, r
	r = crf1[crf1.columns[0]].corr(crf2[crf2.columns[0]])
	#print('Pearson coefficient %f' % (r))
	# Fisher Z transformation on r'
	rp = np.arctanh(r)
	#print('Fisher Z trans %f' % (rp))
	# Standard Error Calculation for transformed correlation r'
	N = time
	srp = 1/((N - 3.0)**(0.5))
	#print('Z-score: %f' %(rp/srp))
	return rp/srp
	
def disc_prune(fi, m_b):

	#iterate across the features stored in the selected feature set
	
	# need to iterate from top of array since we're deleting elements as we go
	col_ind = m_b.columns.values
	
	for column in m_b:
		y = pd.DataFrame(m_b[column])
		
		# This checks for redundancy of the feature
		if abs(zs(y, c)) > abs(zs(fi, c)) and abs(zs(fi, y)) >= abs(zs(fi, c)):
			return False
		
		# Newly found fi makes Y redundant -- fi is closer to the target feature
		# than fi
		if abs(zs(fi, c)) > abs(zs(y, c)) and abs(zs(fi, y)) >= abs(zs(fi, c)):
			m_b.drop(column, axis=1, inplace=True)


meteo_vars = ['pw','t850','v850','u850','v300','u300','z1000','z500','z300']

target = np.load('./preproc_data2/target_1980_2010.npy')

c = pd.DataFrame(target[:,0], columns=['target'])

locations = 5328
time = 11300
offset = 6	

markov_b = pd.DataFrame([])
	
for var in range(0, 9):
	data = np.load('./preproc_data2/%s.npy' % (meteo_vars[var]))
	
	print('Processing feature type %s' % (meteo_vars[var]))
	
	for day in range(0, 4):
		
		print('Processing day %d' % (day))
		
		ddata = data[offset+day:time+offset+day,:]
		
		for loc in range(0, locations):
			colname = '%d_%s_%d' % (loc, meteo_vars[var], day)
			
			#print('processing %s: ' % (colname))
			
			f_i = pd.DataFrame(ddata[:,loc], columns=[colname])
			
			if abs(zs(c, f_i)) < 1.96: 
				continue
				
			if (disc_prune(f_i, markov_b) == False):
				continue
			
			markov_b = pd.concat([markov_b, f_i], axis=1)
		
		print('Finished processing day %d' % (day))
		
		
	#pdb.set_trace()
	print('Finished processing feature type %s' % (meteo_vars[var]))
		
			