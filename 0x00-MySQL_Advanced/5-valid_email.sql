-- Task: Create a trigger that resets the 'valid_email' attribute when 'email' is changed
-- Context: Ensures email validity is reevaluated automatically after a user changes their email address

DELIMITER //

CREATE TRIGGER reset_valid_email_on_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = FALSE;
    END IF;
END;
//

DELIMITER ;
