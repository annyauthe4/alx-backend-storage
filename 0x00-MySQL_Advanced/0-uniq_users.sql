-- Write a SQL script that creates a table users following these
-- attributes: id, email, name.


-- Create users table if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
