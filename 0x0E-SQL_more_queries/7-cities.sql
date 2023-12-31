-- a script that creates the db hbtn_0d_usa
-- table cities id INT unique, auto generated, cant be null, primary
-- varchar(256) cant be null
-- state_id INT can't be null, must be a FOREIGN KEY that reference id of the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) 
    REFERENCES states(id));