import sqlite3
from sqlite3 import IntegrityError

class Db:
    def __init__(self):
        self.connection = sqlite3.connect('medical_db.db')
        self.cursor = self.connection.cursor()
        self._initialize_db()

    def _initialize_db(self):
        """Create the patients table if it doesn't exist"""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            dob TEXT,
            phone_number TEXT,
            email TEXT
        )
        ''')
        self.connection.commit()

    def insert_patient(self, first_name, last_name, dob, phone_number, email):
        try:
            self.cursor.execute('''
            INSERT INTO patients (first_name, last_name, dob, phone_number, email)
            VALUES (?, ?, ?, ?, ?)
            ''', (first_name, last_name, dob, phone_number, email))
            self.connection.commit()
            print(f"Patient {first_name} {last_name} added successfully.")
        except IntegrityError as e:
            print(f"Error: {e}")

    def update_patient(self, patient_id, first_name=None, last_name=None, dob=None, phone_number=None, email=None):
        try:
            self.cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
            patient = self.cursor.fetchone()

            if patient:
                update_query = "UPDATE patients SET"
                values = []
 
                if first_name:
                    update_query += " first_name = ?,"
                    values.append(first_name)
                if last_name:
                    update_query += " last_name = ?,"
                    values.append(last_name)
                if dob:
                    update_query += " dob = ?,"
                    values.append(dob)
                if phone_number:
                    update_query += " phone_number = ?,"
                    values.append(phone_number)
                if email:
                    update_query += " email = ?,"
                    values.append(email)

                update_query = update_query.rstrip(',')  # Remove the trailing comma
                update_query += " WHERE patient_id = ?"
                values.append(patient_id)

                self.cursor.execute(update_query, tuple(values))
                self.connection.commit()
                print(f"Patient ID {patient_id} updated successfully.")
            else:
                print(f"Error: Patient with ID {patient_id} not found.")
        except Exception as e:
            print(f"Error: {e}")

    def select_patient_by_id(self, patient_id):
        self.cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
        patient = self.cursor.fetchone()

        if patient:
            print("Patient Found: ", patient)
        else:
            print(f"Error: No patient found with ID {patient_id}.")

    def select_patient_by_phone(self, phone_number):
        self.cursor.execute("SELECT * FROM patients WHERE phone_number = ?", (phone_number,))
        patients = self.cursor.fetchall()

        if patients:
            print("Patients Found: ")
            for patient in patients:
                print(patient)
        else:
            print(f"Error: No patient found with phone number {phone_number}.")

    def close(self):
        self.cursor.close()
        self.connection.close()
