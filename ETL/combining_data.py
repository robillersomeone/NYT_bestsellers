import pandas as pd

# read in data
gr_2016_df = pd.read_csv('../data/2016_goodreads.csv')
gr_2017_df = pd.read_csv('../data/2017_goodreads.csv')
gr_2018_df = pd.read_csv('../data/2018_goodreads.csv')
gr_2019_df = pd.read_csv('../data/2019_goodreads.csv')

# need to account for list elements in 'publisher' and 'data' in 2016-18 data
# if there are two dates, index 375 in 2016, take first element
# if there are null values

# drop duplicate titles
# column for bs
# concat not bs dataframes
# add column for non bs
# concat bs and not

# check duplicates

# export to csv