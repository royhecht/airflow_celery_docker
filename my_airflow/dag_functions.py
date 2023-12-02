import logging


def extract_data(**kwargs):
    logging.info(f"Received kwargs: {kwargs}")
    data = kwargs.get('params', {}).get('data', {})
    return data


def transform_and_load(**kwargs):
    ti = kwargs['ti']
    extracted_data = ti.xcom_pull(task_ids='extract_task')

    transformed_data = {k.upper(): v.upper() for k, v in extracted_data.items()}
    print("Transformed and loaded data:", transformed_data)