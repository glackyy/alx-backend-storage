-- A Script that creates a stored procedure
-- ComputerAverageWeightedScoreForUser wich takes in one parameter user_id
-- Computing the average weighted score for a user by summing up the product of scores
-- and weights of the user from the corrections table, summing up the total weight
-- and then dividing the total weighted score by the total weight, and then updating
-- the average score field of the user in the users table
DROP PROCEDURE IF EXISTS ComputerAverageWeightedScoreForUser;
DELIMITER $$ ;
CREATE PROCEDURE ComputerAverageWeightedScoreForUser (user_id INTEGER)
BEGIN
    DECLARE total_weighted_score INTEGER DEFAULT 0;
    DECLARE total_weight INTEGER DEFAULT 0;
    SELECT SUM(corrections.score * projects.weight)
        INTO total_weighted_score
        FROM corrections
        INNER JOIN projects
            ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;
    IF total_weight = 0 THEN
        UPDATE users SET users.average_score = 0
        WHERE user.id = user_id;
    ELSE
        UPDATE users
        SET users.average_score = total_weighted_score / total_weight
        WHERE users.id = user_id;
    END IF;
END;$$
DELIMITER ;
