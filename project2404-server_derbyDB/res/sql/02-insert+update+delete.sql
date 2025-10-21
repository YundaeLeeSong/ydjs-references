-- Inserting staff data
INSERT INTO staff (staff_id, staff_firstname, staff_lastname, username, password)
VALUES 
    (1, 'John', 'Doe', 'john_doe', 'password123'),
    (2, 'Jane', 'Smith', 'jane_smith', 'letmein'),
    (3, 'Michael', 'Johnson', 'michael_j', 'securepass'),
    (4, 'Emily', 'Anderson', 'emily_a', 'password456'),
    (5, 'David', 'Brown', 'david_b', 'pass123'),
    (6, 'Sarah', 'Taylor', 'sarah_t', 'securepass456');

-- Inserting patient data
INSERT INTO patient (patient_id, patient_firstname, patient_lastname, mrn, dob)
VALUES 
    (1, 'Alice', 'Johnson', 'MRN123456', '1990-05-15'),
    (2, 'Bob', 'Williams', 'MRN789012', '1985-10-20'),
    (3, 'Eva', 'Brown', 'MRN345678', '1978-12-03'),
    (4, 'Chris', 'Miller', 'MRN654321', '1980-09-25'),
    (5, 'Olivia', 'Martinez', 'MRN098765', '1995-03-12'),
    (6, 'Sophia', 'Lee', 'MRN246801', '1972-07-18');

-- Inserting patient-staff relationships
INSERT INTO patient_staff (patient_cid, staff_cid)
VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 3),
    (4, 3),
    (5, 4),
    (6, 5),
    (6, 6);

-- Inserting daily report data
INSERT INTO daily_report_data (report_id, patient_id, weight, systolic, diastolic, is_abdomen, is_leg, report_date)
VALUES
    (1, 1, 70.5, 120.0, 80.0, 1, 0, '2024-03-31'),
    (2, 2, 85.2, 130.0, 85.0, 0, 1, '2024-03-31'),
    (3, 3, 65.7, 110.0, 70.0, 1, 1, '2024-03-30'),
    (4, 4, 72.3, 125.0, 78.0, 1, 0, '2024-03-29'),
    (5, 5, 78.9, 128.0, 82.0, 0, 1, '2024-03-30'),
    (6, 6, 67.4, 115.0, 72.0, 1, 1, '2024-03-29');

-- Inserting notification data
INSERT INTO notification (notification_id, patient_id, message)
VALUES
    (1, 1, 'Reminder: Please schedule your follow-up appointment.'),
    (2, 2, 'Medication refill request received.'),
    (3, 3, 'Lab results available. Please check your portal.'),
    (4, 4, 'Reminder: Your prescription needs to be renewed.'),
    (5, 5, 'Appointment scheduled for next week.'),
    (6, 6, 'New test results available. Please review.');
