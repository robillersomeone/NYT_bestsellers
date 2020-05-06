import sys
import pickle
import numpy as np
import pandas as pd
import text_feature_engineering as te

new_description = ' '.join(sys.argv[1:])

# load in count vectorizer and model
cv_pickle = open("data/countvectorizer.pk","rb")
cv = pickle.load(cv_pickle)
# print(cv)
rf_text_model = pickle.load(open('models/rf_text_model.sav', 'rb'))

# target names for all the models
class_names = ['Not Bestseller', 'Bestseller']

def new_book_prediction(text):
    '''predict of bestseller or not based on text data

    Parameters
    -------
    text: description of book as a string

    Returns
    -------
    predict from RandomForestClassifier text based model
    '''
    # process text
    clean_text = te.nlp_processing(np.array([text]))
    # print(clean_text)
    # transform with count vectorizer (from a pickle)
    cv_transformed = cv.transform(clean_text)

    new_book_df = pd.DataFrame(cv_transformed.toarray(),columns=cv.get_feature_names())
    # predict with rf model (from a pickle)
    pred = rf_text_model.predict(new_book_df)
    # pred = model.predict(new_book_df)

    # return prediction
    if pred == 0:
        print('\n', class_names[0])
    else:
        print('\n', class_names[1])

    pass

def main():
    new_book_prediction(new_description)

if __name__ == '__main__':
    main()
