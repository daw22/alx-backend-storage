-- A stored procedure that computes average score for a student
DELIMITER %%
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE total INT;
	DECLARE scores_count INT;
	SELECT SUM(score) INTO total FROM corrections AS C WHERE C.user_id = user_id;
	SELECT COUNT(*) INTO scores_count FROM corrections AS C WHERE C.user_id = user_id;
	UPDATE users SET average_score = total / scores_count WHERE id = user_id;
END
%%
DELIMITER ;
