CREATE DATABASE chirpdb;

USE DATABASE chirpdb;

CREATE TABLE Events
(
    event_id    int NOT NULL,
    headline    VARCHAR(255),
    description VARCHAR(255),
    timestamp        DATETIME,
    event_type  int,
    latitude    FLOAT,
    longitude   FLOAT
);
 
ALTER TABLE Events MODIFY COLUMN event_id int AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE Events AUTO_INCREMENT=2000000;

CREATE TABLE Users
(
    user_id           int NOT NULL,
    username          VARCHAR(255),
    phone_number      int NOT NULL,
    reliability_score FLOAT,
    base_latitude     FLOAT,
    base_longitude    FLOAT
);

ALTER TABLE Users MODIFY COLUMN user_id int AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE Users AUTO_INCREMENT=1000000;

CREATE TABLE Verifications
(
    verification_id int NOT NULL,
    event_id int NOT NULL,
    user_id int NOT NULL,
    verified bool NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Events(event_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

ALTER TABLE Verifications MODIFY COLUMN verification_id int AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE Verifications AUTO_INCREMENT=3000000;