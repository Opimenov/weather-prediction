import numpy as np
import pandas as pd
import copy as cp
import pdb
import time as tm

# note: zs function has been tested
# Takes two pandas frames as arguments
def zs(crf1, crf2):
	# Pearson correlation coefficient, r
	r = crf1[0].corr(crf2[0])
	#print('Pearson coefficient %f' % (r))
	# Fisher Z transformation on r'
	rp = np.arctanh(r)
	#print('Fisher Z trans %f' % (rp))
	# Standard Error Calculation for transformed correlation r'
	N = time
	srp = 1/((N - 3.0)**(0.5))
	#print('Z-score: %f' %(rp/srp))
	return rp/srp

# Discard feature or prune features from the previous set based on current feature

#old discard/prune functiono

#def disc_prune(fi, flist, st1):
	# Probably kind of bad to refer to c as a free var here but whatever
	
	# iterate across the features stored in the selected feature set
#	for i in st1.shape[1]:
#		y = st1[i]
#		
		# This checks for redundancy of the feature
#		if abs(zs(y, c)) > abs(zs(fi, c)) and abs(zs(fi, y)) > 1.96:
#			pdb.set_trace()
#			return False
		
		# Newly found fi makes Y redundant -- fi is closer to the target feature
		# than fi
#		if abs(zs(fi, c)) > abs(zs(y, c)) and abs(zs(fi, y)) > 1.96:
#			pdb.set_trace()
#			st1.drop(i, axis=1)


def disc_prune(fi, flist, ddata):

	#iterate across the features stored in the selected feature set
	
	# need to iterate from top of array since we're deleting elements as we go
	for i in xrange(len(flist)-1, -1, -1):
		#pdb.set_trace()
		y = pd.DataFrame(ddata[:,flist[i]])
		
		# This checks for redundancy of the feature
		if abs(zs(y, c)) > abs(zs(fi, c)) and abs(zs(fi, y)) >= 1.96:
			#pdb.set_trace()
			return False
		
		# Newly found fi makes Y redundant -- fi is closer to the target feature
		# than fi
		if abs(zs(fi, c)) > abs(zs(y, c)) and abs(zs(fi, y)) >= 1.96:
			#print('deleting featuer at %d' % (i))
			#pdb.set_trace()
			del flist[i]
	#if(len(flist) > 0):
		#print('flist length now: %d' % (len(flist)))
		
def disc_prune2(fi, flist, ddata):

	#iterate across the features stored in the selected feature set
	
	# need to iterate from top of array since we're deleting elements as we go
	for i in xrange(len(flist)-1, -1, -1):
		#pdb.set_trace()
		y = pd.DataFrame(ddata[:,flist[i]])
		
		# This checks for redundancy of the feature
		if abs(zs(y, c)) > abs(zs(fi, c)) and abs(zs(fi, y)) >= abs(zs(fi, c)):
			#pdb.set_trace()
			return False
		
		# Newly found fi makes Y redundant -- fi is closer to the target feature
		# than fi
		if abs(zs(fi, c)) > abs(zs(y, c)) and abs(zs(fi, y)) >= abs(zs(fi, c)):
			#print('deleting featuer at %d' % (i))
			#pdb.set_trace()
			del flist[i]
	#if(len(flist) > 0):
		#print('flist length now: %d' % (len(flist)))

	
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
bflist = [[], [], [], [], [], [], [], [], []]
	
<<<<<<< HEAD

for type in range(0, 9):

	print('Processing feature type %s' % (meteo_vars[type]))
	data = np.load('./preproc_data2/%s.npy' % (meteo_vars[type]))
	
	for day in range(0,4):
		ddata = data[offset+day:time+offset+day,:]
	
		flist = []
		#flist = bflist[type]
		nextflist = []
	
		print('Processing day %d' % (day))
		for loc in range (0, locations):
			# TODO: Preserve location number in array so it can be mapped later
			ti = pd.DataFrame(ddata[:,loc])
			
			z = zs(c, ti)
			
			# If feature passes this first correlation, it is relevant. If it doesn't pass, it's irrelevant.
			if abs(z) < 1.96:
				continue
			
			# Ugly bad hack in order to grow data frame from nothing
			# There might be a better way to do this, I don't know pandas or
			# python very well
			
			# In the first loop we label all features that have some sort of
			# correlation with 
			
			#pdb.set_trace()
			
			if( disc_prune2(ti, flist, ddata) == False):
				continue
				
			flist.append(loc)
			
			#print('adding feature location %d of type %s' % (loc, meteo_vars[type]))
			#flist.append('%d__%d_%s' % (loc, day, meteo_vars[f]))
			#if(day == 0):
			#	nextflist.append(loc)
			#else:
			#	nextflist = flist + [loc]
			#print('z score: %f' % (abs(z)))

			#tm.sleep(5)
			
			
			
			# TODO: Need to add 
			
			#if st[day].shape[0] == 0  and karr.shape[0] == 0:
			#	karr = ti.as_matrix()
			#	karri = loc
			#elif st[day].shape[0] == 0:
			#	#pdb.set_trace()
			#	st[day] = pd.DataFrame(np.concatenate((karr, ti.as_matrix()), axis=1))
			#else:
			#	#pdb.set_trace()
			#	st[day] = pd.concat([st[day], ti], axis=1, copy=False)
			
			# In subsequent loops, we either prune features from the previous
			# set of features or discard the current feature depending on 
			# how previous features and the current feature correlate with
			# the class attribute and each other
			
			#if day != 0:
			#	pdb.set_trace()
			#	if disc_prune(ti, st[day-1]) == False:
			#		continue
			#	else:
			#		st[day] = st[day].concat(ti, axis=1)
=======
-
					
					
				
>>>>>>> 9c4ecf3e46cb92a708350b08e0a14b9013457233
		
		bflist[type] = flist
		print(flist)
		print('Number of features found for %s on day %d: %d' % (meteo_vars[type], day, len(flist)))
		tm.sleep(5)
	print('Processed day %d' % (day))