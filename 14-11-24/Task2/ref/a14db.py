import sqlite3
from sqlite3 import IntegrityError

# Connect to the SQLite database (it will create the database file if it doesn't exist)
connection = sqlite3.connect('medical_db.db')
cursor = connection.cursor()

# Create the patients table (if not already exists)
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob TEXT,
    phone_number TEXT,
    email TEXT
)
''')

# Function to insert a new patient
def insert_patient(first_name, last_name, dob, phone_number, email):
    try:
        # Insert a new patient record
        cursor.execute('''
        INSERT INTO patients (first_name, last_name, dob, phone_number, email)
        VALUES (?, ?, ?, ?, ?)
        ''', (first_name, last_name, dob, phone_number, email))
        connection.commit()
        print(f"Patient {first_name} {last_name} added successfully.")
    except IntegrityError as e:
        print(f"Error: {e}")

# Function to update an existing patient's details
def update_patient(patient_id, first_name=None, last_name=None, dob=None, phone_number=None, email=None):
    try:
        # Check if the patient exists
        cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
        patient = cursor.fetchone()
        
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
            
            cursor.execute(update_query, tuple(values))
            connection.commit()
            print(f"Patient ID {patient_id} updated successfully.")
        else:
            print(f"Error: Patient with ID {patient_id} not found.")
    except Exception as e:
        print(f"Error: {e}")

# Function to select patient(s) by primary key (patient_id)
def select_patient_by_id(patient_id):
    cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
    patient = cursor.fetchone()
    
    if patient:
        print("Patient Found: ", patient)
    else:
        print(f"Error: No patient found with ID {patient_id}.")

# Function to select patient(s) by non-primary key (e.g., phone number or email)
def select_patient_by_phone(phone_number):
    cursor.execute("SELECT * FROM patients WHERE phone_number = ?", (phone_number,))
    patients = cursor.fetchall()
    
    if patients:
        print("Patients Found: ")
        for patient in patients:
            print(patient)
    else:
        print(f"Error: No patient found with phone number {phone_number}.")

# Insert some test data
insert_patient('a', 'b', '1985-06-15', '123-456-7890', 'a@poc.com')
insert_patient('c', 'd', '1992-02-20', '987-654-3210', 'de@poc.com')
insert_patient('e', 'f', '1975-08-25', '555-444-3333', 're@poc.com')

# Try to insert a patient with a duplicate email (will violate primary key constraint)
insert_patient('abc', 'def', '1990-10-10', '123-123-1234', 'abcdef@poc.com')

# Update patient with ID 1 (John Doe)
update_patient(1, phone_number='111-222-3333', email='freak@poc.com')

# Try to update a non-existent patient
update_patient(999, phone_number='000-000-0000')

# Select patient by primary key (patient_id)
select_patient_by_id(1)  
select_patient_by_id(999)  # Should show "patient not found"

# Select patients by non-primary key (phone number)
select_patient_by_phone('987-654-3210')  # Should find
select_patient_by_phone('000-000-0000')  # Should show "no patient found"

# Close the connection
cursor.close()
connection.close()
