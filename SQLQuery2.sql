USE RobotKinematics;
GO

SELECT 
	Entry,
	Joint1_Angle,
	-- Converts the Timestamp into better format 
	FORMAT(Timestamp, 'hh:mm:ss tt') AS TimeSent
	FROM ArmMovementLog
	ORDER BY Entry DESC;