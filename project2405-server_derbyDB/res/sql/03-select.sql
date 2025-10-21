-- DQL to get all the patient data
SELECT * FROM patient;

-- DQL to get the maximum patient ID for incrementing IDs
SELECT MAX(patient_id)
FROM patient;

-- DQL to get current patients associated with a staff member
SELECT patient.patient_firstname, patient.patient_lastname, patient.mrn
FROM patient 
JOIN patient_staff ON patient.patient_id = patient_staff.patient_cid
WHERE patient_staff.staff_cid = 1;

-- DQL to get new patients not associated with any staff member
SELECT patient_firstname, patient_lastname, mrn
FROM patient
WHERE patient_id NOT IN (SELECT patient_cid FROM patient_staff);

-- DQL to get patient ID from MRN
SELECT patient_id
FROM patient
WHERE mrn = 'MRN123456';

-- DQL to get daily report data list for a patient
SELECT *
FROM daily_report_data
WHERE patient_id = 1
ORDER BY report_date;

-- DQL to get daily report data for a patient
SELECT report_date, weight
FROM daily_report_data
WHERE patient_id = 1;

-- DQL to get detail of a patient
SELECT patient_firstname, patient_lastname, mrn
FROM patient
WHERE patient_id = 1;
