import pandas as pd

# read in data
gr_2016_df = pd.read_csv('../data/2016_goodreads.csv')
gr_2017_df = pd.read_csv('../data/2017_goodreads.csv')
gr_2018_df = pd.read_csv('../data/2018_goodreads.csv')
gr_2019_df = pd.read_csv('../data/2019_goodreads.csv')

# need to account for list elements in 'publisher' and 'data' in 2016-18 data
# if there are two dates, index 375 in 2016, take first element
# if there are null values
choiceawards_df = pd.concat([gr_2016_df, gr_2017_df, gr_2018_df, gr_2019_df])

print('total books', choiceawards_df.shape)


# check duplicates
doubled_books_df = choiceawards_df[choiceawards_df.duplicated(['title'], keep=False)]

print('doubled books', doubled_books_df.shape)

# drop duplicate titles
df = choiceawards_df.drop_duplicates(subset='title', keep='last')

# add column for best seller
# set to 0 to start


# read from database
# if the title is in the database, set to 1



# export to csv
# book_df.to_csv('../data/16_19_goodreads.csv')
