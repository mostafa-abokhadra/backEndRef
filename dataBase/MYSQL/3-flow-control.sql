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

-- loop statment
"""
    used to create repeated execution of the statement list
    statement_list consists one or more statements, each statement
    terminated by a semicolon (;). the statements within the loop
    are repeated until the loop is terminated. Usually, LEAVE statement
    is used to exit the loop construct. Within a stored function,
    RETURN can also be used, which exits the function entirely.
    A LOOP statement can be labeled.      
"""
LOOP       
    statement_list  
END LOOP

DELIMITER $$
CREATE PROCEDURE `my_proc_LOOP` (IN num INT)
BEGIN
    DECLARE x INT;
    SET x = 0;
    loop_label: LOOP
        INSERT INTO number VALUES (rand());
        SET x = x + 1;
        IF x >= num THEN
            LEAVE loop_label;
        END IF;
    END LOOP;
END$$

-- repeat statement
"""
    The REPEAT statement executes the statement(s)
    repeatedly as long as the condition is true.
    The condition is checked every time at the end 
"""

[begin_label:] 
REPEAT     
statement_list 
UNTIL search_condition 
END 
REPEAT 
[end_label]

DELIMITER $$
CREATE PROCEDURE my_proc_REPEAT (IN n INT)
BEGIN
SET @sum = 0;
SET @x = 1;  
REPEAT   
    IF mod(@x, 2) = 0 THEN
        SET @sum = @sum + @x;
    END IF;
    SET @x = @x + 1;
    UNTIL @x > n 
END REPEAT;
END $$
