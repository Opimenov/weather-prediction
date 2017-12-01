import random
import numpy as np

#Generates random example features to be placed in a map.

#For example, a meteorlogical variable t850 at location 300 on lookaheada day 8 
#will have the format string:
#
#300_t850_8

#This is the format I'll stick to when creating the final filtered list of 
#features

#You can let this script save this as a file (called genvars.py) to load with
#numpy or you can copy-paste/import the function to where you need it
	
def genmapvars(genfile=False):
	meteo_vars = ['pw','t850','v850','u850','v300','u300','z1000','z500','z300']
	length = random.randint(25, 50)
	arr = np.array([])


	for i in range(0, length):
		loc = random.randint(1, 5328) 
		day = random.randint(7,10)
		var = meteo_vars[random.randint(0,8)]
		string = '%d_%s_%d' % (loc, var, day)
		random.randint(6,9)
		arr = np.append(arr, string)

	if(genfile):
		np.save(file='genvars.npy', arr=arr)
		
	return arr
	
print(genmapvars(genfile=False))