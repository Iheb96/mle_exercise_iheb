
from joblib import dump, load
import warnings
warnings.filterwarnings("ignore")
from typing import Optional
from fastapi import FastAPI
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
#load the model
vec = TfidfVectorizer()
vec= load("encoder.pkl")
estim= svm.LinearSVC()
estim= load("decoder.pkl")


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def predict(question: str):
    tfidf = vec.transform([question])
    res=estim.predict(tfidf)

    return {"Prediction class": str(res[0])}
