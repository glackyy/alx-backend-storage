-- A Script that creates a stored procedure
-- ComputeAverageScoreForUser, it computes
-- and store the avr score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INTEGER
)
BEGIN
    UPDATE users SET average_score=(Select AVG(score) FROM corrections
                                    WHERE corrections.user_id=user_id)
    WHERE id=user_id;
END;$$
DELIMITER ;
