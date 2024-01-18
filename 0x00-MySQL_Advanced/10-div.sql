-- A Script that creates a function SafeDiv
-- Divides and returns the first by the second number
-- or returns 0 if the second number is equal to 0
DELIMITER $$ ;
CREATE FUNCTION SafeDiv(
    a INTEGER,
    b INTEGER
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE res FLOAT;
    IF b = 0 THEN
        RETURN 0;
    END IF;
    SET res = (a * 1.0) / b;
    RETURN res;
END;$$
DELIMITER ;
