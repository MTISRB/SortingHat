# Required packages for the database:
# pip install firebase
# pip install firebase_admin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import pandas as pd
import pprint


def parse(key):
    cred = credentials.Certificate(key)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://mtisrb-default-rtdb.europe-west1.firebasedatabase.app/'
    })


def load_data(xlsx_file, sheet_name) -> list:
    excel = pd.read_excel(xlsx_file, sheet_name=sheet_name)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    temp = excel.to_dict().copy()
    t = [value for value in temp.values()]

    for x in range(len(t)):
        t[x] = [i for i in t[x].values()]

    for x, _list in enumerate(t):
        t[x] = [item for item in _list if str(item) != 'nan']
    #print(t)

    return t


def fill_fb(t: list):
    data_id = t[0]
    vraag = t[1]
    antwoord = t[2]
    richting = t[3]
    punten = t[4]

    ref, handle = query()

    handle = db.reference("py/DATA_ID")
    for i, q in enumerate(data_id):
        vragen_ref = ref.child('DATA_ID')
        vragen_ref.update({
            f'ID {i}': {
                'ID': f'{q}',
            }
        })

    handle = db.reference("py/vragen")
    for i, q in enumerate(vraag):
        vragen_ref = ref.child('vragen')
        vragen_ref.update({
            f'vraag {i}': {
                'vraag_id': f'{i}',
               'vraag': f'{q}'
            }
        })

    handle = db.reference("py/antwoord")
    for i, q in enumerate(antwoord):
        vragen_ref = ref.child('antwoord')
        vragen_ref.update({
            f'antwoord {i}': {
                'antwoord_id': f'{i}',
                'antwoord': f'{q}'
            }
        })

    handle = db.reference("py/richting")
    for i, q in enumerate(richting):
        vragen_ref = ref.child('richting')
        vragen_ref.update({
            f'richting {i}': {
                'richting_id': f'{i}',
                'richting': f'{q}'
            }
        })

    handle = db.reference("py/punten")
    for i, q in enumerate(punten):
        vragen_ref = ref.child('punten')
        vragen_ref.update({
            f'punten {i}': {
                'punten_id': f'{i}',
                'punten': f'{q}'
            }
        })

# As an admin, the app has access to read and write all data, regradless of Security Rules
def query() -> tuple:
    ref = db.reference('py/')
    handle = db.reference('py/vragen/')
    return ref, handle


# users_ref = ref.child('users')
# users_ref.set({
#     'gebruiker_1': {
#         'user_id': '0',
#         'voornaam': 'John',
#         'achternaam': 'Doe'
#     }
# })

# vragen_ref = ref.child('vragen')
# vragen_ref.set({
#     'vraag_1': {
#         'vraag_id': '1',
#         'vraag': 'In welke richting heb je al interesse?'
#     }
# })

# antwoorden_ref = ref.child('antwoorden')
# antwoorden_ref.set({
#     'antwoord_1': {
#         'antwoorden_id': '1',
#         'antwoorden': 'Forensische ICT, Interactie-Technologie, Software Engineering, Data engineer, geen idee'
#     }
# })

# hopper_ref = users_ref.child('gebruiker')