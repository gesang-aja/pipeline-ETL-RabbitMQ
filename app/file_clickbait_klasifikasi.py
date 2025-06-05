import joblib


loaded_model = joblib.load(r"app\RF_clickbait_klasifikasi.joblib")
model = loaded_model['model']
tfidf = loaded_model['TFIDF']

def klasifikasi (cleaned_text) :
    vector = tfidf.transform([cleaned_text])
    prediction = model.predict(vector)
    label = 'clickbait' if prediction == 1 else 'non-clickbait'
    return label