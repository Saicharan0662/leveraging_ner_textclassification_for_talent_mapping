from flask import request, jsonify
import joblib
import spacy
import nltk
from sklearn.feature_extraction import _stop_words
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer 

nlp = spacy.load('en_core_web_sm')

class NLP():

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
        doc = " ".join([token for token in doc.split() if token not in stopwords])    
        doc = "".join([lemmatizer.lemmatize(word) for word in doc])
        return doc

    def preprocess_data(self, data):
        stopwords = _stop_words.ENGLISH_STOP_WORDS
        lemmatizer = WordNetLemmatizer()

        data = self.clean(data)
        tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform(docs)
        docs = tfidf_vectorizer_vectors.toarray()

        dense_tfidf_vectorizer_vectors = tfidf_vectorizer_vectors.toarray()

        # Create reshaped_data with the correct shape
        reshaped_data = np.zeros((dense_tfidf_vectorizer_vectors.shape[0], 2510))

        # Copy the values from tfidf_vectorizer_vectors to reshaped_data
        reshaped_data[:, :dense_tfidf_vectorizer_vectors.shape[1]] = dense_tfidf_vectorizer_vectors

        return reshaped_data


    def get_predictions(self, data):
        model = joblib.load('./NLP_Model/model111_796.sav')

        text = self.preprocess_data(data[5])

        predictions = model.predict(text)

        print(predictions)