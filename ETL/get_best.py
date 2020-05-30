import re
import csv
import time, random
import requests
import pandas as pd
import urllib.request
from config import url_best_seller
from tqdm import tqdm
from bs4 import BeautifulSoup as bs

# get weekly best sellers

# most likely insert into a local db (postgres)

def get_urls(base_url):
    pass 

def get_books(weekly_url):
    """
    will get weeks on the list, title, and author

    """
    bs_list = []
    get_title = pass
    get_author = pass
    weeks = pass
     bs_list.append({'title':get_title, 
                    'author':get_author,
                    'weeks': weeks})
    pass


def insert_into_db():
    """
    COPY output from get_books() into db
    """

    pass