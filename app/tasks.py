from app.celery_config import app
import time
from app.file_prepocessing import clean_text
from app.file_clickbait_klasifikasi import klasifikasi
from app.file_topik_klasifikasi import klasifikasi_topik
from app.file_load import save_to_postgres

@app.task(name='app.tasks.preprocess_task', bind=True, queue='antrian_preprocessing')
def preprocess_task(self, berita):
    try:
        print(f"Preprocessing berita: {berita}")
        cleaned = clean_text(berita)
        processed_data = {
            'news': berita,
            'cleaned_news': cleaned,
            'processed_at': time.time(),
            'status': 'processed'
        }
        print(f"Preprocessing selesai: {processed_data}")
        return processed_data
    except Exception as exc:
        print(f"Error in preprocess_task: {exc}")
        self.retry(countdown=60, max_retries=3, exc=exc)

@app.task(name='app.tasks.classify_task', bind=True, queue='antrian_klasifikasi')
def classify_task(self, preprocessed_berita):
    try:
        cleaned = preprocessed_berita.get('cleaned_news', '')
        label_clickbait = klasifikasi(cleaned)

        result_clickbait =  {
            'news': preprocessed_berita.get('news', ''),
            'cleaned_news': cleaned,
            'label': label_clickbait,
        }
        save_to_postgres(berita=result_clickbait['news'], berita_clean= result_clickbait['cleaned_news'] , hasil= result_clickbait['label'], tabel= 'berita_clickbait')
        return result_clickbait
    except Exception as exc:
        print(f"Error in classify_task: {exc}")
        self.retry(countdown=60, max_retries=3, exc=exc)



@app.task(name='app.tasks.cluster_task', bind=True, queue='antrian_clustering')
def cluster_task(self, preprocessed_berita):
    try:
        
        cleaned = preprocessed_berita.get('cleaned_news', '')
        label_topik = klasifikasi_topik(cleaned)

        result_topik =  {
            'news': preprocessed_berita.get('news', ''),
            'cleaned_news': cleaned,
            'label': label_topik,
        }
        
        save_to_postgres(berita=result_topik['news'], berita_clean= result_topik['cleaned_news'] , hasil= result_topik['label'], tabel ='berita_topik' )
   
        return result_topik
    except Exception as exc:
        print(f"Error in cluster_task: {exc}")
        self.retry(countdown=60, max_retries=3, exc=exc)
