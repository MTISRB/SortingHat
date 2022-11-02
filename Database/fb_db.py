# ------ Required packages for the database: ----------
# pip install firebase
# pip install firebase_admin
# pip install pandas
# pip install openpyxl

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd
from pprint import pprint


MAIN_ROOT: str = "py"
DB_URL: str = 'https://mtisrb-default-rtdb.europe-west1.firebasedatabase.app/'


def parse(key: str):
    cred = credentials.Certificate(key)
    firebase_admin.initialize_app(cred, {
        'databaseURL': DB_URL
    })


def load_data(xlsx_file: str, sheet_name: str) -> list:
    excel = pd.read_excel(xlsx_file, sheet_name=sheet_name)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    temp = excel.to_dict().copy()
    t = [value for value in temp.values()]

    for x in range(len(t)):
        t[x] = [i for i in t[x].values()]

    for x, _list in enumerate(t):
        t[x] = [item for item in _list if str(item) != 'nan']

    return t


def reference(name: str):
    db.reference(name)


def query() -> tuple:
    ref = db.reference(f'{MAIN_ROOT}/')
    handle = db.reference('py/vragen/')
    return ref, handle


def upload(name, i, item):
    ref, _ = query()
    reference(f"{MAIN_ROOT}/{name}")
    t_ref = ref.child(f'{name}')
    t_ref.update({
        f'{name} {i}': {
            f'{name}_id': f'{i}',
            f'{name}': f'{item}'
        }
    })


def retrieve_data() -> list:
    raw_data = query()[0].get()
    new_data = []

    for x in raw_data:
        k = (x, raw_data[x])
        new_data.append(k)
    return new_data


def print_db():
    pprint(query()[0].get())


def fill_fb(t: list):
    data_id = t[0]
    question = t[1]
    answers = t[2]
    field_of_study = t[3]
    points = t[4]

    ref, _ = query()

    reference(f"{MAIN_ROOT}/DATA_ID")
    for i, q in enumerate(data_id):
        id_ref = ref.child('DATA_ID')
        id_ref.update({
            f'ID {i}': {
                'ID': f'{q}',
            }
        })

    reference(f"{MAIN_ROOT}/question")
    for i, q in enumerate(question):
        q_ref = ref.child('question')
        q_ref.update({
            f'question {i}': {
                'question_id': f'{i}',
                'question': f'{q}'
            }
        })

    reference(f"{MAIN_ROOT}/answers")
    for i, q in enumerate(answers):
        a_ref = ref.child('answers')
        a_ref.update({
            f'answers {i}': {
                'answers_id': f'{i}',
                'answers': f'{q}'
            }
        })

    reference(f"{MAIN_ROOT}/field_of_study")
    for i, q in enumerate(field_of_study):
        fos_ref = ref.child('field_of_study')
        fos_ref.update({
            f'field_of_study {i}': {
                'field_of_study_id': f'{i}',
                'field_of_study': f'{q}'
            }
        })

    reference(f"{MAIN_ROOT}/points")
    for i, q in enumerate(points):
        p_ref = ref.child('points')
        p_ref.update({
            f'points {i}': {
                'points_id': f'{i}',
                'points': f'{q}'
            }
        })
