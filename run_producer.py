from app.chain import create_task_chain
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    # data = 'Aku adalah iku aja ajaiab yAAAA'
    # proses = create_task_chain(data)
    # hasil = proses.get()
    # print(hasil)


    df = pd.read_csv(r'app\data_coba.csv')
    # results = []

    for idx, row in df.iterrows():
        raw_input = row['title']
        print(f"\n=== Memproses baris {idx} ===")
        chain_result = create_task_chain(raw_input)
        result = chain_result.get()
        print(f"""
        Berita : {result[0]['news']},
        Berita_clean : {result[0]['cleaned_news']}
        Label_clickbait : {result[0]['label']}
        Label_topik : {result[1]['label']}
        """)
        # results.append({
        #     'Berita': raw_input,
        #     'Label_clickbait': result[0]['label'],
        #     'Label_topik': result[1]['label'],
        #     })

    print("======= SELESAI=======")


"""

rabbitmq-service start
rabbitmqctl status
rabbitmq-plugins enable rabbitmq_management


celery -A app.celery_config.app worker --loglevel=info --queues=antrian_preprocessing --pool=solo --hostname=worker_preprocessing@%h

celery -A app.celery_config.app worker --loglevel=info --queues=antrian_klasifikasi --pool=solo --hostname=worker_klasifikasi@%h

celery -A app.celery_config.app worker --loglevel=info --queues=antrian_clustering --pool=solo --hostname=worker_clustering@%h

celery -A app.celery_config flower
"""































    # result = chain_result  
    # print("Hasil klasifikasi:", result[0])
    # print("Hasil clustering:", result[1])
    

    # workflow = chain(
    #     preprocess_task.s(raw_input),
    #     group(
    #         classify_task.s(),
    #         cluster_task.s()
    #     )
    # )
    # result = workflow.apply_async(queue="antrian_preprocessing")
    # print("Workflow task sudah dikirim, id:", result.id)
    # # Tunggu sampai task selesai, lalu ambil hasilnya
    # final_result = result.get()  # timeout dalam detik, bisa disesuaikan

    # # Misalnya hasil dari classify_task dan cluster_task masing-masing mengembalikan dict
    # print("Hasil klasifikasi:", final_result[0])
    # print("Hasil clustering:", final_result[1])

