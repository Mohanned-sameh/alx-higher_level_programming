-- creates db hbtn_0d_2 and user user_0d_2
-- user have SELECT only
CREATE DATABASE IF NOT EXISTS hbtn_0d_0;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_0.* TO 'user_0d_2'@'localhost';