<h1> MySQL Advance</h1>
 <ul>
    <li> Indexing</li>
    <li>Stored procedure and function</li>
    <li>Implementing views</li>
    <li> Implementing Triggers</li>
 </ul>

<h1> Index</h1>
An index is a data structure that makes data retrieval faster —like a book’s table
of contents. Without it, MySQL scans every row (full table scan).

Basic Index:
<code>CREATE INDEX index_name ON table_name (column_name);</code>

Example:
<code>CREATE INDEX idx_username ON users(username);</code>

<h1>Stored procedure and function</h1>
Both stored procedures and functions are reusable SQL code blocks stored in the
database and executed with a single call.

<b>How to Create a Stored Procedure:</b>
<code>
DELIMITER $$

CREATE PROCEDURE get_users_by_age(IN min_age INT)
BEGIN
    SELECT * FROM users WHERE age >= min_age;
END $$

DELIMITER ;
</code>

DELIMITER $$ is needed to avoid early termination by the semicolon (;).
IN min_age INT: input parameter
CALL get_users_by_age(25); will return users aged 25 and above.

<h1> How to Create Function</h1>
<code>
DELIMITER $$

CREATE FUNCTION get_user_age(email_param VARCHAR(100))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE user_age INT;
    SELECT age INTO user_age FROM users WHERE email = email_param LIMIT 1;
    RETURN user_age;
END $$

DELIMITER ;
</code>
<b>Called like this:</b>
<code>SELECT get_user_age('john@example.com');</code>
