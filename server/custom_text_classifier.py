from flask import request, jsonify
import joblib
import spacy
import nltk
from sklearn.feature_extraction import _stop_words
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer 
import numpy as np 
import pandas as pd
import os 
import tensorflow as tf
import string
from time import time 

tf.keras.backend.clear_session()

nlp = spacy.load('en_core_web_sm')

class NLP():
    def __init__(self):
        self.model_path = r'G:\\project 3\\product\server\\NLP_Model\\model350_786.sav' #78.6%
        self.stopwords = _stop_words.ENGLISH_STOP_WORDS
        self.lemmatizer = WordNetLemmatizer()
        self.tfidf_vectorizer = TfidfVectorizer(use_idf=True, max_features = 20000) 
        self.predictions = []
        self.formated_output = []
        self.title_list = ['backend development', 'cloud engineer', 'cyber security', 'frontend development', 'machine learning']
        self.color_list = ['purple', 'red', 'cyan', 'orange', 'green']

    def clean(self, doc):
        text_no_namedentities = []
        document = nlp(doc)
        ents = [e.text for e in document.ents]
        for item in document:
            if item.text in ents:
                pass
            else:
                text_no_namedentities.append(item.text)
        doc = (" ".join(text_no_namedentities))

        doc = doc.lower().strip()
        doc = doc.replace("</br>", " ") 
        doc = doc.replace("-", " ") 
        doc = "".join([char for char in doc if char not in string.punctuation and not char.isdigit()])
        doc = " ".join([token for token in doc.split() if token not in self.stopwords])    
        doc = "".join([self.lemmatizer.lemmatize(word) for word in doc])
        return doc

    def preprocess_data(self, data):

        data = self.clean(data)
        docs = [data]
        tfidf_vectorizer_vectors = self.tfidf_vectorizer.fit_transform(docs)
        docs = tfidf_vectorizer_vectors.toarray()

        dense_tfidf_vectorizer_vectors = tfidf_vectorizer_vectors.toarray()
        reshaped_data = np.zeros((dense_tfidf_vectorizer_vectors.shape[0], 2224))
        reshaped_data[:, :dense_tfidf_vectorizer_vectors.shape[1]] = dense_tfidf_vectorizer_vectors

        return reshaped_data

    def get_formated_output(self, data):

        output = []
        for index, item in enumerate(data):
            output.append({
                "title": self.title_list[index],
                "value": item,
                "color": self.color_list[index]
            })
        return output
    
    def normalize_objects(self, data, new_min, new_max):
        values = [obj['value'] for obj in data]
        min_val = min(values)
        max_val = max(values)

        for obj in data:
            obj['value'] = ((obj['value'] - min_val) / (max_val - min_val)) * (new_max - new_min) + new_min

    def get_top_values(self, data, attribute_name):
        sorted_data = sorted(data, key=lambda x: x[attribute_name], reverse=True)
        top_values = sorted_data[:4]

        return top_values

    def get_predictions(self, data_list):

        if not os.path.exists(self.model_path):
            print("Model file does not exist.")
            return "NO RESULT"

        print("Model file exists.")

        try:
            print(self.model_path)
            model = joblib.load(self.model_path, mmap_mode=None)
            print("Model loaded successfully.")
        except Exception as e:
            print("Error loading model:", str(e))
            return "NO RESULT"

        try:
            
            res = [0]*5
            count = 0
            for data in data_list:
                if not data:
                    continue

                data = data.strip()
                if len(data) < 20: 
                    continue

                text = self.preprocess_data(data)
                pred = model.predict(text)
                pred = pred[0]
                print("Predictions: ", pred)
                
                for i in range(5):
                    res[i] += pred[i]
                    # res[i] = res[i]/2

                count += 1


            print("res: ", res)
            # print(sum(res))
            # print(count)
            for i in range(5):
                res[i] = res[i]/count 

            self.predictions = res
            self.formated_output = self.get_formated_output(self.predictions)

            # print(self.formated_output)
            # print(sum(self.formated_output))
            # self.formated_output = self.get_top_values(self.formated_output, 'value')
            # self.normalize_objects(self.formated_output, 0, 100)

            # sum_acc = 0
            # for val in self.formated_output:
            #     sum_acc += val['value']

            # print(sum_acc)

            return self.formated_output

        except Exception as e:
            print("Error predicting:", str(e))
            return "NO RESULT"