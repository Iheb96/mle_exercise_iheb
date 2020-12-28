import numpy as np
import csv
import pandas as pd
from joblib import dump, load
import warnings
warnings.filterwarnings("ignore")
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
#reading the data
x=pd.read_csv("C:\\Users\\Iheb96\\Downloads\\data\\data\\input_train.csv").drop(['ID'],axis=1) 
y=pd.read_csv("C:\\Users\\Iheb96\\Downloads\\data\\data\\output_train.csv").drop(['ID'],axis=1)
#encoding the data
vec = TfidfVectorizer()
vec = vec.fit(x['question'])
tfidf_train=vec.transform(x['question'])
#splitting the data nto train/val
num=tfidf_train.shape[0]
x_train=tfidf_train[:int(num*0.75)]
y_train=y[:int(num*0.75)]
x_val=tfidf_train[int(num*0.75):]
y_val=y[int(num*0.75):]
#training the model
svmm = svm.LinearSVC()
svmm.fit(x_train, y_train)
#Computing the model score
print("training score ",svmm.score(x_train, y_train))
print("validation score ",svmm.score(x_val, y_val))
#saving the encoder and decoder
dump(vec,"encoder.pkl")
dump(svmm,"decoder.pkl")

