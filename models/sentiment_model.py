import pickle

model = pickle.load(open("models/sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

def get_sentiment(text):
    text_vec = vectorizer.transform([text])
    pred = model.predict(text_vec)[0]

    return "Positive" if pred == 1 else "Negative"