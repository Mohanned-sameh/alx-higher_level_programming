-- This script creates a table second_table in the db hbtn_0c_0
-- adds id INT, name VARCHAR(256), score INT
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT second_table (id, name, score) VALUES (1, "John", 10);
INSERT second_table (id, name, score) VALUES (2, "Alex", 3);
INSERT second_table (id, name, score) VALUES (3, "Bob", 14);
INSERT second_table (id, name, score) VALUES (4, "George", 8);
