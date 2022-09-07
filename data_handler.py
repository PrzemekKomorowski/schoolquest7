from datetime import datetime
import uuid
import csv
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
DATA_HEADER = ['id', 'date', 'title', 'question']
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
def get_unique_id():
    id = uuid.uuid4()
    return id


def save_data(id, title, user_question):
    data_list = {'id': id,
                 'date': dt_string,
                 'title': title,
                 'question': user_question}
    with open(f"{dir_path}/sample_data/question.csv", "a") as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=DATA_HEADER)
        dict_object.writerow(data_list)


def get_all_questions():
    with open(f"{dir_path}/sample_data/question.csv") as csv_file:
        reader = csv.reader(csv_file)
        return list(reader)
