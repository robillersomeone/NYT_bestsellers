from sklearn.metrics import confusion_matrix, classification_report, plot_confusion_matrix
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

# dataframes


# target names for all the models
class_names = ['Not Bestseller', 'Bestseller']

#
# clf =

def baseline_modeling(clf, X_data, y_data):

    # fit classifier
    clf.fit(X_data, y_data)

    # this is predcting on the training set
    clf_predictions = clf.predict(X_data)

    # takes y_train, model_predictions
    clf_confusion = confusion_matrix(y_data, clf_predictions)

    clf_plot_confusion = plot_confusion_matrix(clf, X_data, y_data, cmap='ocean', display_labels=class_names)

    clf_score = clf.score(X_data, y_data)

    clf_report = classification_report(y_data, clf_predictions, target_names=class_names)

    return clf_score #, clf_report


# TODO
# train and test data in function
# think about reading output
    # probably going the OOP route
# import data directly
    # most likely not
# think about tuning parameters
