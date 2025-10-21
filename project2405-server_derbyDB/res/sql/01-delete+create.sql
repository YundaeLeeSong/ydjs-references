CREATE TABLE staff (
    staff_id INT PRIMARY KEY,
    staff_firstname VARCHAR(80) NOT NULL,
    staff_lastname VARCHAR(80) NOT NULL,
    username VARCHAR(80) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL
);

CREATE TABLE patient (
    patient_id INT PRIMARY KEY,
    patient_firstname VARCHAR(80) NOT NULL,
    patient_lastname VARCHAR(80) NOT NULL,
    mrn VARCHAR(80) NOT NULL UNIQUE,
    dob DATE NOT NULL
);

CREATE TABLE patient_staff (
    patient_cid INT,
    staff_cid INT,

    PRIMARY KEY (patient_cid, staff_cid),
    FOREIGN KEY (patient_cid) REFERENCES patient(patient_id),
    FOREIGN KEY (staff_cid) REFERENCES staff(staff_id)
);

CREATE TABLE daily_report_data (
    report_id INT PRIMARY KEY,
    patient_id INT NOT NULL,
    weight DOUBLE,
    systolic DOUBLE,
    diastolic DOUBLE,
    is_abdomen INT,
    is_leg INT,
    report_date DATE,
    
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id)
);

CREATE TABLE notification (
    notification_id INT PRIMARY KEY,
    patient_id INT NOT NULL,
    message VARCHAR(256) NOT NULL,

    FOREIGN KEY (patient_id) REFERENCES patient(patient_id)
);