-- Convert the database character set and collation
-- Convert all tables and their respective fields to utf8mb4
-- Convert all VARCHAR/TEXT fields to utf8mb4
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SELECT CONCAT('ALTER TABLE `', table_name, '` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;') AS sql_statements
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0';
SELECT CONCAT('ALTER TABLE `', table_name, '` MODIFY `', column_name, '` ', data_type, '(',
    character_maximum_length, ') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;') AS sql_statements
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0' AND (data_type = 'varchar' OR data_type = 'text');
