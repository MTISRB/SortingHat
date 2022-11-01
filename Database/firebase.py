# Required packages for the database:
# pip install firebase
# pip install firebase_admin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("Project_week/mtisrb-firebase-adminsdk-u1zpn-c585cb5c8c.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mtisrb-default-rtdb.europe-west1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('py/')
users_ref = ref.child('users')
users_ref.set({
    'gebruiker_1': {
        'user_id': '0',
        'voornaam': 'John',
        'achternaam': 'Doe'
    }
})

vragen_ref = ref.child('vragen')
vragen_ref.set({
    'vraag_1': {
        'vraag_id': '1',
        'vraag': 'In welke richting heb je al interesse?'
    }
})

antwoorden_ref = ref.child('antwoorden')
antwoorden_ref.set({
    'antwoord_1': {
        'antwoorden_id': '1',
        'antwoorden': 'Forensische ICT, Interactie-Technologie, Software Engineering, Data engineer, geen idee'
    }
})

# hopper_ref = users_ref.child('gebruiker')

handle = db.reference('py/users/')

print(ref.get())