# Required packages for the database:
# pip install firebase
# pip install firebase_admin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import pandas as pd


def parse(key):
    cred = credentials.Certificate(key)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://mtisrb-default-rtdb.europe-west1.firebasedatabase.app/'
    })


def load_data(xlsx_file, sheet_name) -> dict:
    # Dictionary in list with lists as pairs and excel columns as keys
    data = {}

    excel = pd.read_excel(xlsx_file, sheet_name=sheet_name)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    data = excel.to_dict().copy()

    return data


def fill_fb(data: dict):
    pass


# As an admin, the app has access to read and write all data, regradless of Security Rules
def query() -> tuple:
    ref = db.reference('py/')
    handle = db.reference('py/users/')
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