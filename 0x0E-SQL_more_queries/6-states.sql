-- a script that create the database hbtn_0d_usa
-- and the table states (id INT unique auto generated cant be null and unique), 
-- name (VARCHAR(256) cant be null)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);