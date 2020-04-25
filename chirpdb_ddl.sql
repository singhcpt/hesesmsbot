CREATE DATABASE chirpdb;

USE DATABASE chirpdb;

create table Events
(
    event_id    int not null,
    headline    VARCHAR(255),
    description VARCHAR(255),
    timestamp        DATETIME,
    event_type  int,
    latitude    FLOAT,
    longitude   FLOAT
);
 
ALTER TABLE Events MODIFY COLUMN event_id int AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE Events AUTO_INCREMENT=2000000;

create table Users
(
    user_id           int not null,
    username          VARCHAR(255),
    reliability_score FLOAT,
    base_latitude     FLOAT,
    base_longitude    FLOAT,
    preferences       int
);

ALTER TABLE Users MODIFY COLUMN user_id int AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE Users AUTO_INCREMENT=1000000;
