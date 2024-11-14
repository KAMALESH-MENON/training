class Patient:
    def __init__(self, patient_id, first_name, last_name, dob, phone_number, email):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return (f"Patient ID: {self.patient_id}, Name: {self.first_name} {self.last_name}, "
                f"DOB: {self.dob}, Phone: {self.phone_number}, Email: {self.email}")
