import pandas as pd
import itertools
import csv
import openpyxl as px
import numpy as np

# Empty array to fetch all the relavant features in the CSV file.
feature = []
with open('./sample_data/generated/relevant_features/kendall.csv') as csvfile:
	readCSV = csv.reader(csvfile)
	# Fetching the 1st row
	for row in itertools.islice(readCSV, 1):
		# Adding the row in the feature array 
		feature.append(row)		
	# Iterating through the length of feature array	and for each feature splitting it into 3 parts (Location ID, feature, Day)
	for i in range(1,len(feature[0])):
		name=feature[0][i]
		parts = name.split("_")
		# Reading the longtitude_latitude xlsx file and parsing the sheet1
		xl = pd.ExcelFile("./longtitude_latitude2.5.xlsx")	
		df = xl.parse("Sheet1")
		#Iterating through all the rows of xlsx file and comparing the ID field with the parts[0]. Parts[0] is the location we got from split.
		for index, row in df.iterrows():
			# If both are equal, fetch the corresponding latitude and longtitude.
			if parts[0] == str(int(row['ID'])):
				#Latitude of the location			
				print "LAT \n " + str(row['lat'])
				#Longitude of the location
				print "LONG \n " + str(row['long'])
				#Relavant feature 
				print "part 1 \n " + parts[1] 
				#Particular day
				print "part 2 \n " + parts[2]
					
					