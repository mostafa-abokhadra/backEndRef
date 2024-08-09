-- if statement
IF condition THEN
    statement
ELSE IF condition THEN
    statement    
ELSE
    statement
END IF

IF user_id = "scott123" THEN
    SET user_name = "Scott";
ELSE IF user_id = "ferp6734" THEN
    SET user_name = "Palash";
END IF;