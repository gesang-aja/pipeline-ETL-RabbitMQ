from celery import Celery
from kombu import Queue ,Exchange

app = Celery('task_chain')

exchange_tugas = Exchange('tugas_utama', type='direct')
app.conf.update(
    broker_url='amqp://guest@localhost:5672//',
    result_backend='rpc://',
    task_routes = {
    'app.tasks.preprocess_task': {'queue': 'antrian_preprocessing', 'routing_key': 'antrian_preprocessing'},
    'app.tasks.classify_task': {'queue': 'antrian_klasifikasi', 'routing_key': 'antrian_klasifikasi'},
    'app.tasks.cluster_task': {'queue': 'antrian_clustering', 'routing_key': 'antrian_clustering'},
    },
    task_queues = (
        Queue('antrian_preprocessing', exchange=exchange_tugas, routing_key='antrian_preprocessing'),
        Queue('antrian_klasifikasi', exchange=exchange_tugas, routing_key='antrian_klasifikasi'),
        Queue('antrian_clustering', exchange=exchange_tugas, routing_key='antrian_clustering'),
    ),
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

app.autodiscover_tasks(['app'])
