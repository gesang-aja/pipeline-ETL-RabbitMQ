# Setup stemming dan stopwords
import re
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

stemmer = StemmerFactory().create_stemmer()
stop_words = set(StopWordRemoverFactory().get_stop_words())

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\x00-\x7f]', r' ', text)
    text = text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    text = re.sub(r'(.)\1+', r'\1\1', text)
    tokens = text.split()
    processed_tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(processed_tokens)
