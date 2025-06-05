📰 Pipeline ETL Terdistribusi untuk Klasifikasi Berita Clickbait dan Topik
Sistem otomatis berbasis Celery dan RabbitMQ untuk klasifikasi berita clickbait dan topik populer


## 📌 Deskripsi Proyek

- 🔍 **Tujuan**: Membuat sistem otomatis yang dapat mengekstraksi, membersihkan, dan mengklasifikasikan berita clickbait dan topic berita secara efisien.
- 🛠️ **Manfaat**: Cocok untuk platform kurasi berita atau pemantauan media yang ingin menyaring konten clickbait dan menganalisis topik populer.
- ⚙️ **Arsitektur**: Menggunakan pendekatan terdistribusi dengan **Celery Workers** dan **RabbitMQ** sebagai message broker.


## 🚀 Cara Instalasi dan Menjalankan Proyek

###  1. Instalasi  RabbitMQ  

Menginstall Erlang dan RabbitMQ.

Erlang: https://www.erlang.org/downloads

RabbitMQ: https://www.rabbitmq.com/download.html

### 2.Menjalankan RabbitMQ

Buka **CMD sebagai Administrator**, lalu jalankan:

-----cmd-----

rabbitmq-service start

rabbitmq-plugins enable rabbitmq_management

akses dashboard UI-nya di browser:

http://localhost:15672

### 3. Clone Repository

bash
git clone https://github.com/username/pipeline-clickbait.git
cd pipeline-clickbait

### 3. membuat dan mengaktifkan  virtual enviroment

python -m venv venv # membuat venv

venv\Scripts\activate  # mengaktifkan venv

pip install -r requirements.txt # install dependensi


### 4. jalankan worker setiap queue + flower

Buka ti4ga terminal lalu jalankan masing masing script dibawah  : 

celery -A app.celery_config.app worker --loglevel=info --queues=antrian_preprocessing --pool=solo --hostname=worker_preprocessing@%h

celery -A app.celery_config.app worker --loglevel=info --queues=antrian_klasifikasi --pool=solo --hostname=worker_klasifikasi@%h

celery -A app.celery_config.app worker --loglevel=info --queues=antrian_clustering --pool=solo --hostname=worker_clustering@%h

celery -A app.celery_config flower

### 5. jalankan producer

Buka terminal dan jalankan : 

python run_producer.py

### 6. contoh output 

{
  "judul": "Gak Nyangka! 7 Artis Ini Pindah Profesi",
  "preprocessing": "gak nyangka artis pindah profesi",
  "clickbait": 1,
  "topik": "Hiburan"
}

## 📂 struktur folder
project/

├── app/

│   ├── celery_config.py             # Konfigurasi Celery & Queue
 
│   ├── chain.py                     # Definisi chain task ETL
 
│   ├── file_prepocessing.py         # Fungsi pembersihan dan preprocessing

│   ├── file_clickbait_klasifikasi.py  # Model klasifikasi clickbait

│   ├── file_topik_klasifikasi.py    # Model klasifikasi topik berita
 
│   ├── file_load.py                 # Fungsi penyimpanan/visualisasi hasil
 
│   ├── RF_clickbait_klasifikasi.joblib  # Model clickbait (joblib)

│   ├── RF_topik_klasifikasi.joblib      # Model topik berita (joblib)

│   ├── data_scrap.csv               # Dataset simulasi berita

├── run_producer.py        # Producer / main.py

├── requirements.txt       # Daftar dependensi

├── README.md              # Dokumentasi


** berikut link gdrive  model  RF_clickbait_klasifikasi.joblib da  RF_topik_klasifikasi.joblib :

https://drive.google.com/drive/folders/1Zagkjh0MLCtjFRPFCV_J-I34zP2NNmaj?usp=sharing
