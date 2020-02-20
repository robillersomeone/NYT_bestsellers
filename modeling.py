from sklearn.metrics import confusion_matrix, classification_report, plot_confusion_matrix
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import text_feature_engineering_helper as teh
import pandas as pd
import numpy as np
import pickle

# dataframes


# target names for all the models
class_names = ['Not Bestseller', 'Bestseller']
#

# X_data is the cleaned dataframe
def baseline_modeling(clf, X_data, y_data, confusion_title=None):

    # fit classifier
    clf.fit(X_data, y_data)

    # this is predcting on the training set
    clf_predictions = clf.predict(X_data)

    # takes y_train, model_predictions
    clf_confusion = confusion_matrix(y_data, clf_predictions)

    if confusion_title != None:
        clf_plot_confusion = plot_confusion_matrix(clf, X_data, y_data,
                    cmap='ocean', display_labels=class_names).ax_.set_title(confusion_title)
    else:
        clf_plot_confusion = plot_confusion_matrix(clf, X_data, y_data,
                    cmap='ocean', display_labels=class_names).ax_.set_title('Confusion Matrix for Classifier')
    clf_score = clf.score(X_data, y_data)

    clf_report = classification_report(y_data, clf_predictions, target_names=class_names)

    return {'clf score' :clf_score,
            'clf confusion': clf_confusion}

            # {'clf score' :clf_score,
            # 'clf confusion': clf_confusion,
            # 'clf report': clf_report}

# X_data is the cleaned dataframe
def modeling(clf, X_data, y_data):

    # fit classifier
    clf.fit(X_data, y_data)

    # this is predcting on the training set
    clf_predictions = clf.predict(X_data)

    # takes y_train, model_predictions
    clf_confusion = confusion_matrix(y_data, clf_predictions)

    # clf_plot_confusion = plot_confusion_matrix(clf, X_data, y_data, cmap='ocean', display_labels=class_names)

    clf_score = clf.score(X_data, y_data)

    clf_report = classification_report(y_data, clf_predictions, target_names=class_names)

    return {'clf score' :clf_score,
            'clf confusion': clf_confusion}


cv_pickle = open("csv_files/countvectorizer.pk","rb")
cv = pickle.load(cv_pickle)

def new_book_prediction(text):
    # process text
    clean_text = reh.nlp_processing(np.array([text]))

    # transform with count vectorizer (from a pickle)
    cv_transformed = cv.transform(clean_text)

    new_book_df = pd.DataFrame(cv_transformed.toarray(),columns=cv.get_feature_names())
    # predict with rf model (from a pickle)

    # pred = model.predict(new_book_df)

    if pred == 0:
        return class_names[0]
    else:
        return class_names[1]

    pass # return prediction


# TODO
# train and test data in function
