import text_feature_engineering_helper as text_helper
import numpy as np
import pandas as pd
from nltk import pos_tag
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn import model_selection
from sklearn.feature_extraction import text as txt
from sklearn.feature_extraction.text import CountVectorizer

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
        tag = pos_tag([word])[0][1][0]
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

v_lemmtize_it =  np.vectorize(lemmtize_it)

# stop words
nyt_stop_words = ['new', 'york', 'bestseller', 'besteller', 'bestselling']

# add custom stop words to list of stop words, which is a frozen set
stop_words = txt.ENGLISH_STOP_WORDS.union(nyt_stop_words)

def nlp_processing(text):
    '''processes text for modeling

    Parameters
    -------
    text: a string of the description,
        with lemmas, no html, intergers, or punctuation

    Returns
    -------
    string of cleaned text
    '''
    preprocessed_text = text_helper.nlp_preprocessing(text)
    l_text = v_lemmtize_it(preprocessed_text)
    return l_text


# TODO


# fit the CountVectorizer?
# probs in a different notebook

# this notebook will just be to clean the text
# make another file for  fiting a count vectorizer

# X_test = nlp_processing(X_test)
#
# cv = CountVectorizer(stop_words=stop_words)
# v_X_train = cv.fit_transform(X_train)
# v_X_test = cv.transform(X_test)
# X_df = pd.DataFrame(v_X_train.toarray(),columns=cv.get_feature_names())
# X_test_df = pd.DataFrame(v_X_test.toarray(),columns=cv.get_feature_names())

# think about output from function
# make a class?

# synsets?
