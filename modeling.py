import sys
import pickle
import numpy as np
import pandas as pd
import text_feature_engineering as te
from sklearn.metrics import confusion_matrix, classification_report, plot_confusion_matrix
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# dataframes


# target names for all the models
class_names = ['Not Bestseller', 'Bestseller']


# X_data is the cleaned dataframe
def baseline_modeling(clf, X_data, y_data, confusion_title=None):
    '''map part of speech to use in WordNetLemmatizer

    Parameters
    -------
    clf: sklearn classifier, ie RandomForestClassifier, LogisticRegression, or DummyClassifier

    X_data: cleaned training data features

    y_data: classification of example (besteller or not)

    confusion_title: optional title for classifer in confusion matrix

    Returns
    -------
    score for model
    confusion matrix
    '''
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
