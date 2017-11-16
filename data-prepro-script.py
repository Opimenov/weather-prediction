import pandas
years = range(1980, 2011)
#set up list of meteorological variables
meteo_vars = ['pw_','t850_','v850_','u850_','v300_','u300_','z1000_','z500_','z300_']
days = range(0,10)#,10)
df = pandas.DataFrame()
#for each day (we have 10 days 0-9, one sample has 10 days of data) 
for day in days:
    #print day
    #for each meteorological variable
    for met_var in meteo_vars:
        #print met_var
        #create an empty data frame to be used as a container
        df = pandas.DataFrame()
        #for each year 1980 - 2011
        for year in years:
            #print year
            #print 'df shape ', df.shape
            #create a path based on meteo var and year
            path = './raw_data/%s%d.csv' % (met_var,year)
            #read one file from raw data
            frame = pandas.read_csv(path)
            #print 'frame shape ', frame.shape
            #drop  first four columns
            frame.drop(frame.columns[[0,1,2,3]], axis=1, inplace=True)
            # add frame that we just read to the bottom of container
            df = df.append(frame)
            #print 'after concat df shape ', df.shape
            #print 'end of inner for'
        ## we need to delete 
        #day number of top rows
        indexes_to_drop_top = set(range(0,day))
        # 9 - day number of bottom rows
        indexes_to_drop_bot = set(range(df.shape[0], df.shape[0]- (10-day),-1))
        #so the indecies that we need to drop are
        to_drop = indexes_to_drop_bot.union(indexes_to_drop_top)
        # for improved performance it is better to take rows that we need
        indexes_to_keep = set(range(df.shape[0])) - to_drop
        # take only needed rows since we are putting these frames side by side 
        #and shifting each one row up (like a staircase)
        df = df.take(list(indexes_to_keep))
        #print 'after drop df shape ', df.shape
        #print 'end of middle for loop'
        #write one meteo variable for one day in separate file => 10 days x 9 vars = 90 files    
        df.to_csv(r'./sample_data/%s_%d.csv'%(met_var,day), header=None,index=None,sep=',')
