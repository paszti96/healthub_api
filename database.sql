CREATE DATABASE HealthHUB;

CREATE TABLE patient (
    name VARCHAR(255),
    social_security_num CHAR(11) UNIQUE,
    risk_level INT,
    birth_date DATE,
    address_id INT,
    FOREIGN KEY address_id REFERENCES address(id),
);

CREATE TABLE hospital(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    address_id INT,
    FOREIGN KEY (address_id) REFERENCES address(id),
    
);

CREATE TABLE address(
    id INT PRIMARY KEY,
    address_name VARCHAR(255),
    latitude DECIMAL,
    Longitude DECIMAL,
);

CREATE TABLE appointment(
    id INT PRIMARY KEY,
    patient_id INT,
    hospital_id INT,
    timeslot DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (hospital_id) REFERENCES hospital(id)
);