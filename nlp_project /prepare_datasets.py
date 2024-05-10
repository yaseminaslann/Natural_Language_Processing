# -*- coding: utf-8 -*-

from tika import parser 
import os


contents = []

classes = os.listdir('train_dataset')
for i in range(len(classes)):
    path = os.path.join('train_dataset', classes[i])
    content = os.listdir(path)
    for doc in content:
        document_path = os.path.join(path,doc)
        raw = parser.from_file(document_path)
        contents.append([raw['content'], i])

import numpy as np
import pandas as pd

contents = np.array(contents)

dataset = pd.DataFrame()

dataset["Text"] = contents[:,0]
dataset["Label"] = contents[:,1]

dataset.to_excel("training_dataset.xlsx")

test_dataset = pd.DataFrame()

contents = []
classes = os.listdir('test_dataset')
for i in range(len(classes)):
    path = os.path.join('test_dataset', classes[i])
    content = os.listdir(path)
    for doc in content:
        document_path = os.path.join(path,doc)
        raw = parser.from_file(document_path)
        contents.append([raw['content'], i])
        
contents = np.array(contents)
test_dataset["Text"] = contents[:,0]
test_dataset["Label"] = contents[:,1]

test_dataset.to_excel("test_dataset.xlsx")