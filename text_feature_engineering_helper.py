import re
import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.feature_extraction import text as txt
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer


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
    return re.sub('\.|-|\(|\)|\"|,|\?', ' ', text)

def no_upper(text):
    '''remove uppercase
    -------
    text: a string of the description
    '''
    return text.lower()

# lemmatize

# POS keys
# ADJ = adjective
# NOUN = noun
# VERB = verb
# ADV = adverb

lemmatizer = WordNetLemmatizer()
# n = noun
# v = verb
# a = adjective
# r = adverb


def mapping_pos(word):
    '''helper function to map part of speech to use in WordNetLemmatizer

    Parameters
    -------
    word: one word string

    Returns
    -------
    Part of Speech for the WordNetLemmatizer as a string
    '''
    if word.isdigit():
        return ' '
    # naive mapping of the nltk word pos to the WordNetLemmatizer pos
    else:
        tag = nltk.pos_tag([word])[0][1][0]
        if tag == 'J':
            return 'a'
        elif tag == 'V':
            return 'v'
        elif tag == 'R':
            return 'r'
        else:
            return 'n'


def lemmtize_it(sentences):
    '''map part of speech to use in WordNetLemmatizer

    Parameters
    -------
    sentences: a string of the description,
        with no html, intergers, or punctuation

    Returns
    -------
    sentence as lemmas
    '''
    # split the string of sentences
    sentence = sentences.split(' ')
    cleaned = [lemmatizer.lemmatize(i, mapping_pos(i)) for i in sentence if i is not '']
    return " ".join(cleaned)


# stop words
nyt_stop_words = ['new', 'york', 'bestseller', 'besteller', 'bestselling']

# add custom stop words to list of stop words, which is a frozen set
stop_words = txt.ENGLISH_STOP_WORDS.union(nyt_stop_words)

'''
Parameters
-------
no_function: earlier text processing functions

Returns
-------
no_function_v: vectorized verison of the function
'''


# vectorize text processing functions
no_html_v = np.vectorize(no_html)

no_nums_v = np.vectorize(no_nums)

no_punc_v = np.vectorize(no_punc)

no_upper_v = np.vectorize(no_upper)

v_lemmtize_it =  np.vectorize(lemmtize_it)

def nlp_processing(text):
    h_text = no_html_v(text)
    n_text = no_nums_v(h_text)
    p_text = no_punc_v(n_text)
    u_text = no_upper_v(p_text)
    l_text = v_lemmtize_it(u_text)
    return l_text
# TODO

# fit the CountVectorizer?
# probs in a different notebook

# this notebook will just be to clean the text
# make another file for  fiting a count vectorizer



# X_test = no_html_v(X_test)
# X_test = no_nums_v(X_test)
# X_test = no_punc_v(X_test)
# X_test = no_upper_v(X_test)
# X_test = v_lemmtize_it(X_test)
#
# cv = CountVectorizer(stop_words=stop_words)
# v_X_train = cv.fit_transform(X_train)
# v_X_test = cv.transform(X_test)
# X_df = pd.DataFrame(v_X_train.toarray(),columns=cv.get_feature_names())
# X_test_df = pd.DataFrame(v_X_test.toarray(),columns=cv.get_feature_names())

# think about output from function
# make a class?

# synsets?
