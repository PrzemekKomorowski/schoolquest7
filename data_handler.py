import uuid
import csv
import os
DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'questions.csv'
DATA_HEADER = ['title', 'question']


def get_unique_id():
    id = uuid.uuid4()
    return id


def save_data(title, user_question):
    data_list = {'title': title,
                 'question': user_question}
    with open('questions.csv', "a") as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=DATA_HEADER)
        dict_object.writerow(data_list)


def get_all_questions():
    with open('questions.csv') as csv_file:
        reader = csv.reader(csv_file)
        return list(reader)
