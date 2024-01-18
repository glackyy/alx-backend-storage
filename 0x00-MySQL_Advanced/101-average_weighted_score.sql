-- A Script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users AS us, 
    (SELECT us.id, SUM(score * weight) / SUM(weight) AS w_avg 
    FROM users AS us
    JOIN corrections as c ON us.id=c.user_id 
    JOIN projects AS pr ON c.project_id=pr.id 
    GROUP BY us.id)
  AS WA
  SET us.average_score = WA.w_avg 
  WHERE us.id=WA.id;
END;
