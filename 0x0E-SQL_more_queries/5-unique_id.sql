-- a script that creates table unique_id 
-- id INT default 1 and must be unique, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));