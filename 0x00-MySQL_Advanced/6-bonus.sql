-- Create a stored procedure AddBonus that adds a new correction for a student.
-- Inputs: user_id(int), project_name (varchar), score (int).


-- Create stored procedure
DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;

    -- Check if the project already exists
    SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;

    -- If not found, insert it and get the new id
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
	SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END;
//

DELIMITER ;
