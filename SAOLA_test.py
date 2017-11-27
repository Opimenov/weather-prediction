import numpy as np
import pandas as pd

meteo_vars = ['pw','t850','v850','u850','v300','u300','z1000','z500','z300']

target = np.load('./preproc_data2/target_1980_2010.npy')
#Data frame of feature attributes, c
c = pd.DataFrame(target[:,0])

locations = 5328
time = 13300

#Takes two pandas frames as arguments
def z_score(crf1, crf2):
	# Correlation r
	r = crf1[0].corr(crf2[0])
	#Fisher Z transformation, r'
	rp = np.arctanh(r)
	# Standard Error Calculation for transformed correlation r'
	N = time
	srp = 1/((N - 3.0)**(0.5))
	return rp/srp

for day in range(6,9):
	for f in range(0, 9):
		data = np.load('./preproc_data2/%s.npy' % (meteo_vars[f]))
		for i in range (0, locations):
			#TODO: Preserve location number so it can be mapped later
			ti = pd.DataFrame(data[:,i])
			
			z = z_score(c, ti)
			
			if abs(z) < 1.96:
				continue
				
			#TODO: Implement the rest...
		
