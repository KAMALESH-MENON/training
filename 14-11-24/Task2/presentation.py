from logic import Logic
from patient import Patient

def main():
    logic = Logic()

    # Insert some test data
    patient1 = Patient(None, 'a', 'b', '1985-06-15', '123-456-7890', 'a@poc.com')
    patient2 = Patient(None, 'c', 'd', '1992-02-20', '987-654-3210', 'de@poc.com')
    patient3 = Patient(None, 'e', 'f', '1975-08-25', '555-444-3333', 're@poc.com')
    patient4 = Patient(None, 'abc', 'def', '1990-10-10', '123-123-1234', 'abcdef@poc.com')

    logic.insert_patient(patient1)
    logic.insert_patient(patient2)
    logic.insert_patient(patient3)
    logic.insert_patient(patient4)

    # Update patient with ID 1
    logic.update_patient(1, phone_number='111-222-3333', email='freak@poc.com')

    # Try to update a non-existent patient
    logic.update_patient(999, phone_number='000-000-0000')

    # Select patient by primary key (patient_id)
    logic.select_patient_by_id(1)
    logic.select_patient_by_id(999)  # Should show "patient not found"

    # Select patients by non-primary key (phone number)
    logic.select_patient_by_phone('987-654-3210')  # Should find
    logic.select_patient_by_phone('000-000-0000')  # Should show "no patient found"

    # Close the connection
    logic