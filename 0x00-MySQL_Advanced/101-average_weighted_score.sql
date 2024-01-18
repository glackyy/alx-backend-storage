-- A Script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
        (SELECT users.id, SUM(score * weight) / SUM(weight) AS w_average
        FROM users JOIN corrections ON users.id = corrections.user_id
        JOIN projects ON corrections.project_id = projects.id
        GROUP BY users.id)
    AS w_a
    SET users.average_score = w_a.w_average
    WHERE users.id = w_a.id;
END;
