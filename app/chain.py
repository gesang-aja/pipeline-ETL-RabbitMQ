from celery import chain, group
from app.tasks import preprocess_task, classify_task, cluster_task

def create_task_chain(raw_input):
    workflow = chain(
    preprocess_task.s(raw_input),
    group(
        classify_task.s(),
        cluster_task.s()
    )
)
    return workflow.apply_async(queue='antrian_preprocessing')

