USE lab4;

INSERT INTO hospitals (name, address, phone) VALUES
('Central Hospital', '123 Main St', '555-1234'),
('Westside Clinic', '456 West St', '555-5678'),
('Eastside Medical Center', '789 East Ave', '555-7890'),
('Northside Hospital', '321 North St', '555-1111'),
('Southside Clinic', '654 South St', '555-2222'),
('Lakeside Health', '987 Lake Ave', '555-3333'),
('Mountain Medical', '111 Mountain Rd', '555-4444'),
('Valley Clinic', '222 Valley Blvd', '555-5555'),
('City Hospital', '333 City Plz', '555-6666'),
('River Health Center', '444 River Rd', '555-7777');

INSERT INTO patients (hospital_id, name, date_of_birth, gender, contact_info) VALUES
(1, 'John Doe', '1985-05-20', 'Male', 'johndoe@example.com'),
(2, 'Jane Smith', '1990-08-15', 'Female', 'janesmith@example.com'),
(3, 'Alice Brown', '1975-09-30', 'Female', 'alicebrown@example.com'),
(4, 'Bob Johnson', '2000-12-10', 'Male', 'bobjohnson@example.com'),
(5, 'Charlie White', '1982-07-22', 'Other', 'charliewhite@example.com'),
(6, 'Diana Ross', '1988-03-15', 'Female', 'dianaross@example.com'),
(7, 'Frank Black', '1970-11-25', 'Male', 'frankblack@example.com'),
(8, 'Eve Green', '1995-06-07', 'Female', 'evegreen@example.com'),
(9, 'George Blue', '1968-10-14', 'Male', 'georgeblue@example.com'),
(10, 'Hannah Yellow', '1992-04-18', 'Female', 'hannahyellow@example.com');

INSERT INTO doctors (hospital_id, name, specialization, phone, email) VALUES
(1, 'Dr. Alan Brown', 'Pulmonology', '555-8765', 'alanbrown@example.com'),
(2, 'Dr. Sarah Green', 'Cardiology', '555-4321', 'sarahgreen@example.com'),
(3, 'Dr. Emily Clark', 'Neurology', '555-3456', 'emilyclark@example.com'),
(4, 'Dr. David Miller', 'Endocrinology', '555-6543', 'davidmiller@example.com'),
(5, 'Dr. Anna Taylor', 'Dermatology', '555-9876', 'annataylor@example.com'),
(6, 'Dr. Eric White', 'Orthopedics', '555-6789', 'ericwhite@example.com'),
(7, 'Dr. Laura Gray', 'Gastroenterology', '555-5432', 'lauragray@example.com'),
(8, 'Dr. Patrick Black', 'Oncology', '555-2345', 'patrickblack@example.com'),
(9, 'Dr. Carol Purple', 'Pediatrics', '555-8761', 'carolpurple@example.com'),
(10, 'Dr. Brian Red', 'Psychiatry', '555-4322', 'brianred@example.com');

INSERT INTO trackers (name, unit) VALUES
('Blood Pressure', 'mmHg'),
('Temperature', '°C'),
('Heart Rate', 'bpm'),
('Respiratory Rate', 'breaths/min'),
('Oxygen Saturation', '%'),
('Weight', 'kg'),
('Height', 'cm'),
('Blood Sugar', 'mg/dL'),
('Cholesterol', 'mg/dL'),
('BMI', 'kg/m²');

INSERT INTO patient_trackers (patient_id, tracker_id, measurement_value, measurement_date) VALUES
(1, 1, 120, '2024-11-12 10:00:00'),
(1, 2, 36.6, '2024-11-12 10:05:00'),
(2, 3, 75, '2024-11-13 09:30:00'),
(3, 4, 18, '2024-11-14 08:00:00'),
(4, 5, 95, '2024-11-15 11:00:00'),
(5, 6, 70, '2024-11-16 12:00:00'),
(6, 7, 170, '2024-11-17 13:00:00'),
(7, 8, 105, '2024-11-18 14:00:00'),
(8, 9, 200, '2024-11-19 15:00:00'),
(9, 10, 23.5, '2024-11-20 16:00:00');

INSERT INTO consultations (patient_id, doctor_id, consultation_date, diagnosis, notes) VALUES
(1, 1, '2024-11-12 15:00:00', 'Asthma', 'Patient has mild asthma symptoms.'),
(2, 2, '2024-11-13 10:00:00', 'Hypertension', 'Patient needs to monitor blood pressure regularly.'),
(3, 3, '2024-11-14 11:00:00', 'Migraine', 'Patient reports frequent headaches.'),
(4, 4, '2024-11-15 12:00:00', 'Diabetes', 'Patient shows signs of insulin resistance.'),
(5, 5, '2024-11-16 13:00:00', 'Skin Rash', 'Patient has mild skin irritation.'),
(6, 6, '2024-11-17 14:00:00', 'Fracture', 'Patient has a broken leg.'),
(7, 7, '2024-11-18 15:00:00', 'Stomach Ulcer', 'Patient reports stomach pain.'),
(8, 8, '2024-11-19 16:00:00', 'Cancer', 'Patient requires chemotherapy.'),
(9, 9, '2024-11-20 17:00:00', 'Allergy', 'Patient reports seasonal allergies.'),
(10, 10, '2024-11-21 18:00:00', 'Depression', 'Patient reports feeling down.');

INSERT INTO diagnoses (name, description) VALUES
('Asthma', 'Chronic lung disease that inflames and narrows the airways.'),
('Hypertension', 'Condition in which the blood pressure in the arteries is elevated.'),
('Migraine', 'Neurological condition characterized by intense headaches.'),
('Diabetes', 'Chronic condition that affects blood sugar regulation.'),
('Skin Rash', 'Visible changes in the texture or color of the skin.'),
('Fracture', 'A break in a bone.'),
('Stomach Ulcer', 'Sores that develop on the stomach lining.'),
('Cancer', 'Uncontrolled growth of abnormal cells.'),
('Allergy', 'An immune system response to a foreign substance.'),
('Depression', 'A mood disorder causing a persistent feeling of sadness.');

INSERT INTO patient_diagnoses (patient_id, diagnosis_id, diagnosis_date) VALUES
(1, 1, '2024-11-12 15:00:00'),
(2, 2, '2024-11-13 10:00:00'),
(3, 3, '2024-11-14 11:00:00'),
(4, 4, '2024-11-15 12:00:00'),
(5, 5, '2024-11-16 13:00:00'),
(6, 6, '2024-11-17 14:00:00'),
(7, 7, '2024-11-18 15:00:00'),
(8, 8, '2024-11-19 16:00:00'),
(9, 9, '2024-11-20 17:00:00'),
(10, 10, '2024-11-21 18:00:00');

INSERT INTO medications (name, description, dosage) VALUES
('Albuterol', 'Inhaler for asthma', '2 puffs every 4-6 hours'),
('Lisinopril', 'Medication for hypertension', '10 mg once daily'),
('Metformin', 'Medication for diabetes', '500 mg twice daily'),
('Sumatriptan', 'Medication for migraine', '50 mg as needed'),
('Hydrocortisone', 'Cream for skin irritation', 'Apply twice daily'),
('Ibuprofen', 'Pain reliever', '200 mg every 4-6 hours'),
('Omeprazole', 'Medication for stomach ulcer', '20 mg once daily'),
('Cisplatin', 'Chemotherapy drug', 'IV infusion'),
('Loratadine', 'Allergy medication', '10 mg once daily'),
('Sertraline', 'Antidepressant', '50 mg once daily');

INSERT INTO patient_medications (patient_id, medication_id, start_date, end_date, dosage) VALUES
(1, 1, '2024-11-12', '2024-11-19', '2 puffs every 4-6 hours'),
(2, 2, '2024-11-13', '2024-11-20', '10 mg once daily'),
(3, 3, '2024-11-14', '2024-11-21', '500 mg twice daily'),
(4, 4, '2024-11-15', '2024-11-22', '50 mg as needed'),
(5, 5, '2024-11-16', '2024-11-23', 'Apply twice daily'),
(6, 6, '2024-11-17', '2024-11-24', '200 mg every 4-6 hours'),
(7, 7, '2024-11-18', '2024-11-25', '20 mg once daily'),
(8, 8, '2024-11-19', '2024-11-26', 'IV infusion'),
(9, 9, '2024-11-20', '2024-11-27', '10 mg once daily'),
(10, 10, '2024-11-21', '2024-11-28', '50 mg once daily');

DROP PROCEDURE IF EXISTS get_patients_after_hospital;
DROP PROCEDURE IF EXISTS get_doctors_after_hospital;
DROP PROCEDURE IF EXISTS get_consultations_after_patient;
DROP PROCEDURE IF EXISTS get_consultations_after_doctor;
DROP PROCEDURE IF EXISTS get_patients_after_medication;
DROP PROCEDURE IF EXISTS get_medications_after_patient;
DROP PROCEDURE IF EXISTS get_patients_after_tracker;
DROP PROCEDURE IF EXISTS get_trackers_after_patient;
DROP PROCEDURE IF EXISTS get_patients_after_diagnosis;
DROP PROCEDURE IF EXISTS get_diagnosis_after_patient;

DELIMITER //

CREATE PROCEDURE get_patients_after_hospital(
	IN hospital_id INT
    )
BEGIN
	SELECT h.id AS hospitals_id, p.id AS patients_id, p.name as patient_name, p.date_of_birth as patient_date_of_birth,
    p.gender as patient_gender, p.contact_info as patient_contact_info
    FROM hospitals h
    JOIN patients p ON p.hospital_id = h.id
    WHERE p.hospital_id = hospital_id;
END //

CREATE PROCEDURE get_doctors_after_hospital(
	IN hospital_id INT
    )
BEGIN
	SELECT h.id AS hospitals_id, d.id AS doctors_id, d.name as doctor_name, d.phone as doctor_phone,
    d.specialization as doctor_specialization, d.email as doctor_email
    FROM hospitals h
    JOIN doctors d ON d.hospital_id = h.id
    WHERE d.hospital_id = hospital_id;
END //

CREATE PROCEDURE get_consultations_after_patient(
	IN patient_id INT
    )
BEGIN
	SELECT p.id AS patients_id, c.id AS consultations_id, c.consultation_date as consultation_date,
    c.diagnosis as consultation_diagnosis, c.notes as consultation_notes
    FROM patients p
    JOIN consultations c ON c.patient_id = p.id
    WHERE c.patient_id = patient_id;
END //

CREATE PROCEDURE get_consultations_after_doctor(
	IN doctor_id INT
    )
BEGIN
	SELECT d.id AS doctors_id, c.id AS consultations_id, c.consultation_date as consultation_date,
    c.diagnosis as consultation_diagnosis, c.notes as consultation_notes
    FROM doctors d
    JOIN consultations c ON c.doctor_id = d.id
    WHERE c.doctor_id = doctor_id;
END //

CREATE PROCEDURE get_patients_after_medication(
	IN medication_id INT
    )
BEGIN
	SELECT pm.id, pm.patient_id, pm.medication_id, p.name as patient_name, p.date_of_birth as patient_date_of_birth,
    p.gender as patient_gender, p.contact_info as patient_contact_info
    FROM patients p
    JOIN patient_medications pm ON p.id = pm.patient_id
    WHERE pm.medication_id = medication_id;
END //

CREATE PROCEDURE get_medications_after_patient(
	IN patient_id INT
    )
BEGIN
	SELECT pm.id, pm.medication_id, pm.patient_id, m.name as medication_name, m.description as medication_description,
    m.dosage as medication_dosage
    FROM medications m
    JOIN patient_medications pm ON m.id = pm.medication_id
    WHERE pm.patient_id = patient_id;
END //

CREATE PROCEDURE get_patients_after_tracker(
	IN tracker_id INT
    )
BEGIN
	SELECT pt.id, pt.patient_id, pt.tracker_id, p.name as patient_name, p.date_of_birth as patient_date_of_birth,
    p.gender as patient_gender, p.contact_info as patient_contact_info
    FROM patients p
    JOIN patient_trackers pt ON p.id = pt.patient_id
    WHERE pt.tracker_id = tracker_id;
END //

CREATE PROCEDURE get_trackers_after_patient(
	IN patient_id INT
    )
BEGIN
	SELECT pt.id, pt.tracker_id, pt.patient_id, t.name as tracker_name, t.unit as tracker_unit
    FROM trackers t
    JOIN patient_trackers pt ON t.id = pt.tracker_id
    WHERE pt.patient_id = patient_id;
END //

CREATE PROCEDURE get_patients_after_diagnosis(
	IN diagnosis_id INT
    )
BEGIN
	SELECT pd.id, pd.patient_id, pd.diagnosis_id,  p.name as patient_name, p.date_of_birth as patient_date_of_birth,
    p.gender as patient_gender, p.contact_info as patient_contact_info
    FROM patients p
    JOIN patient_diagnoses pd ON p.id = pd.patient_id
    WHERE pd.diagnosis_id = diagnosis_id;
END //

CREATE PROCEDURE get_diagnosis_after_patient(
	IN patient_id INT
    )
BEGIN
	SELECT pd.id, pd.diagnosis_id, pd.patient_id, d.name as diagnoses_name, d.description as diagnoses_description
    FROM diagnoses d
    JOIN patient_diagnoses pd ON d.id = pd.diagnosis_id
    WHERE pd.patient_id = patient_id;
END //

DELIMITER //