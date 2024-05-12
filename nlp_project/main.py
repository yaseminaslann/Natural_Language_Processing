# -*- coding: utf-8 -*-

from data_preprocessing import document_processor
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier


if __name__ == '__main__':
    dataset = pd.read_excel("training_dataset.xlsx")
    x = dataset["Text"].values
    y = dataset["Label"].values
    x_processed = document_processor.process(x)
    
    vec = TfidfVectorizer()
    x_vectorized = vec.fit_transform(x_processed)
    
    clf = MultinomialNB().fit(x_vectorized, y)      # Multinomial Naive Bayes
    
    test_dataset = pd.read_excel("test_dataset.xlsx")
    x_test = test_dataset["Text"].values
    y_test = test_dataset["Label"].values
    x_test_processed = document_processor.process(x_test)
    x_test_vectorized = vec.transform(x_test_processed)
    
    y_predicted = clf.predict(x_test_vectorized)    

    print("Accuracy Naive Bayes : {}".format(accuracy_score(y_test,y_predicted)))

    svm = SGDClassifier(loss='hinge', max_iter=15, random_state=10)
    svm.fit(x_vectorized, y)
    y_predicted_svm = svm.predict(x_test_vectorized)
    
    print("Accuracy SVM: {}".format(accuracy_score(y_test,y_predicted_svm)))