from db import Db

class Logic:
    def __init__(self):
        self.db = Db()

    def insert_patient(self, first_name, last_name, dob, phone_number, email):
        self.db.insert_patient(first_name, last_name, dob, phone_number, email)

    def update_patient(self, patient_id, first_name=None, last_name=None, dob=None, phone_number=None, email=None):
        self.db.update_patient(patient_id, first_name, last_name, dob, phone_number, email)

    def select_patient_by_id(self, patient_id):
        self.db.select_patient_by_id(patient_id)

    def select_patient_by_phone(self, phone_number):
        self.db.select_patient_by_phone(phone_number)

    def close_db(self):
        self.db.close()
