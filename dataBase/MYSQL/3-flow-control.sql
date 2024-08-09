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

-- case statement
CASE
WHEN (salary>10000) THEN
    (SELECT COUNT(job_id) INTO no_employees 
    FROM jobs 
    WHERE min_salary>10000);
WHEN (salary<10000) THEN
    (SELECT COUNT(job_id) INTO no_employees 
    FROM jobs 
    WHERE min_salary<10000);
ELSE
    (SELECT COUNT(job_id) INTO no_employees 
    FROM jobs WHERE min_salary=10000);
END CASE;

-- iterate statement
"""
    ITERATE means "start the loop again".
    ITERATE can appear only within LOOP, REPEAT,
    and WHILE statements.
"""
-- Here is the syntax:
ITERATE label

-- leave statement
"""
LEAVE statement is used to exit the flow control
construct that has the given label. If the label
is for the outermost stored program block, LEAVE
exits the program. LEAVE can be used within BEGIN
... END or loop constructs (LOOP, REPEAT, WHILE).
"""
-- Here is the syntax :
LEAVE label

