import re
import numpy as np

def no_html(text):
    '''remove html tags
    -------
    text: a string of the description for one book
    '''
    return re.sub('<.{1,9}>',' ', text)

def no_nums(text):
    '''remove years and numbers
    -------
    text: a string of the description
    '''
    return re.sub('\d+', ' ', text)

def no_punc(text):
    '''remove punctuation
    -------
    text: a string of the description
    '''
    return re.sub('\.|-|\(|\)|\"|,|\?|\!', ' ', text)

def no_upper(text):
    '''remove uppercase
    -------
    text: a string of the description
    '''
    return text.lower()

# vectorize text processing functions
no_html_v = np.vectorize(no_html)

no_nums_v = np.vectorize(no_nums)

no_punc_v = np.vectorize(no_punc)

no_upper_v = np.vectorize(no_upper)

def nlp_preprocessing(text):
    h_text = no_html_v(text)
    n_text = no_nums_v(h_text)
    p_text = no_punc_v(n_text)
    u_text = no_upper_v(p_text)
    return u_text
