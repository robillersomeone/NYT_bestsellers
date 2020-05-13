import re
import csv
import time, random
import requests
import pandas as pd
import urllib.request
from tqdm import tqdm
from bs4 import BeautifulSoup as bs

# webb scraping the data in three parts

# part 1: get genre urls for given year

# part 2: get book urls in every genre

# part 3: get data from each book's page

# part 1
def genre_url_list(url):
    """
    Parameters
    -------
    url: one word string

    Returns
    -------
    list of every genre url for given year
    """
    soup = bs(urllib.request.urlopen(url), 'html.parser')
    # soup.find_all('a', {'class':'categoriesList__categoryLink'}) #categoriesList__categoryLink--current
    every_genre_list = []
    for a in soup.find_all('a',{'class':"categoriesList__categoryLink"},  href=True):
        every_genre_list.append('https://www.goodreads.com' + (a['href']))
    return every_genre_list

# part 2 
def book_url_list(genre_urls):
    """
    Parameters
    -------
    genre_urls: list of every genre url for given year

    Returns
    -------
    list of all book urls for given year
    """
    book_list = []
    for url in tqdm(genre_urls):
        soup = bs(urllib.request.urlopen(url), 'html.parser')
        for a in soup.find_all('a',{"class":"pollAnswer__bookLink"},  href=True):
            book_list.append('https://www.goodreads.com' + (a['href']))
    return book_list

# part 3
def get_description(book_links):
    """
    Parameters
    -------
    book_links: list of all book urls for given year

    This function makes a request for every book in the list ~400 requests

    Returns
    -------
    pandas DataFrame of books with descriptions
    """
    book_info = []
    for url in tqdm(book_links):
        time.sleep(random.randint(1, 10)/10)
        r = requests.get(url)
        soup = bs(r.text)

        description = soup.find('div', id='description').text[1:-9]

        get_title = soup.find('h1',{"id":"bookTitle"}).get_text().replace('\n', '').replace('  ', '')
        
        get_genre = soup.find('a', {'class':"actionLinkLite bookPageGenreLink"}).get_text()
        
        get_rating = soup.find('span',{"itemprop":"ratingValue"}).get_text().replace('\n', '').replace(' ', '')
        
        get_author = soup.find('span', {'itemprop':"name"}).get_text()
        
        get_pages = soup.find('span', {'itemprop':"numberOfPages"}).get_text().split(' ')[0]
        
        get_format = soup.find('span', {'itemprop':"bookFormat"}).get_text()

        date_pattern = """(?:January|February|March|April|May|June|
                        July|August|September|October|November|December) .*(?=\n)"""

        get_date_pub = soup.find('div', {'id':"details"}).contents[3].get_text()
        get_date = re.findall(date_pattern, get_date_pub)[0]

        get_publisher = re.findall(r'by .*(?=\n)', get_date_pub)[0][3:]
        
        book_info.append({
            'title': get_title, 'author': get_author, 'description':description, 
            'genre': get_genre, 'rating': get_rating,
            'publisher': get_publisher, 'pages':get_pages, 
            'format': get_format, 'date': get_date,
            'url': url
            })
        
    return pd.DataFrame(book_info)



# run on a url for that year (ie 2016, 2017, 2018)
genre_url = 'https://www.goodreads.com/choiceawards/best-fiction-books-2016'

if __name__ == "__main__":
    # part 1
    #this extracts the url for every genre category of 2019 (or other year) choice awards
    genre_url_list_ = genre_url_list(genre_url)
    print("got the genres")

    # part 2
    book_url_list_ = book_url_list(genre_url_list_)
    print("got the books")

    # part 3
    book_df = get_description(book_url_list_)


    # save data as csv
    book_df.to_csv('../data/2016_goodread.csv)





# nyt_2018_df = pd.DataFrame.from_dict(all_books)
# # nyt_2018_df.to_csv('csv_files/nyt_2018_df.csv', encoding='utf-8', index=False)

# nyt_2017_df = pd.DataFrame.from_dict(all_books_2017)
# # nyt_2017_df.to_csv('csv_files/nyt_2017_df.csv', encoding='utf-8', index=False)

# nyt_2016_df = pd.DataFrame.from_dict(all_books_2016)
# # nyt_2016_df.to_csv('csv_files/nyt_2016_df.csv', encoding='utf-8', index=False)