import joblib
# from bertopic import BERTopic


loaded_model = joblib.load(r"app\RF_topik_klasifikasi.joblib")
model = loaded_model['model']
tfidf = loaded_model['TFIDF']
encoder = loaded_model['encoder']

def klasifikasi_topik (cleaned_text) :
    vector = tfidf.transform([cleaned_text])
    prediction = model.predict(vector)
    label = encoder.inverse_transform(prediction)[0]
    return label