## mysql

### basics

**to start, stop or restart, or check status of mysql service** 
```bash
sudo service mysql stop
sudo service mysql start
sudo service mysql restart
sudo service mysql status
```

**to log in to sql shell**
```bash
sudo mysql -u 'root' -p
```
then you will be asked to write your password "mostafa"\
or just use `sudo mysql` will also prompt for the password

**connecting to remoted db**
```bash
mysql -h hostAddress -P 3306 -u username -D dbname -p
```
then will prompt for user password

**to change prompt**
```bash
prompt @;
```
will change the prompt from mysql> to @

**to check you mySQl version**
```bash
SELECT VERSION();
```
sql key words can be written in upper or lower case and the code will work just fine,
but the best practice is to write key words in UPPERCASE so you can differentiate between
other words and mysql key words:

```sql
SELECT name, email FROM data_base_name WHERE id=73
```
another good syntax is to write the key word in one line and it's attributes in the next line:
```sql
SELECT
    name, email
FROM
	data_base_name
WHERE
	id=73
```

### database operations
```sql
CREATE database IF NOT EXISTS dbName;
SHOW databases;
DROP database IF EXISTS dbName;
USE dbName
SHOW tables FROM dbName;
```

### tables operations

```sql
CREATE TABLE IF NOT EXISTS table_name (
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256)
    country ENUM('EGYPT', 'SAUDI', 'US') DEFAULT 'EGYPT' 
    -- enum allow you to define a datatype that can only hold certian values
);

DESCRIBE table_name; --will show table rows and columns
EXPLAIN table_name --do the same as above
SHOW CREATE TABLE table_name --will show full description of the table
DELETE FROM table_name; -- delete the whole table
TRUNCATE TABLE table_name; --removes all rows from a table, but the table structure and its columns,
                            --constraints, indexes, and so on, remains
ALTER TABLE table_name RENAME TO new_name;
ALTER TABLE table_name RENAME COLUMN old_name To new_name;
ALTER TABLE table_name ADD column_name data_type;
ALTER TABLE table_name DROP COLUMN column_name;
ALTER TABLE table_name MODIFY column_name column_data_type;
ALTER TABLE users ALTER COLUMN status SET DEFAULT 'active';
```
The upcoming command is used to **alter a table** in MySQL and change its **character set** and **collation**. 

### Command:
```sql
ALTER TABLE `someTable` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### Explanation:

1. **`CONVERT TO CHARACTER SET utf8mb4`**: This converts the table to use the **UTF-8 MB4** character set, which is a superset of UTF-8 and allows for storing 4-byte characters like emojis or certain non-Latin scripts.

2. **`COLLATE utf8mb4_unicode_ci`**: This changes the table’s collation to **utf8mb4_unicode_ci**. 
   - **`utf8mb4_unicode_ci`**: This collation is case-insensitive (`ci` stands for "case-insensitive") and uses the Unicode sorting rules.

### Why Use `utf8mb4`?

- **UTF-8** (`utf8` in MySQL) can store characters using 1-3 bytes, which means it cannot store certain special characters like emojis or some less common Chinese characters.
- **UTF-8 MB4** (`utf8mb4`) extends this to 4 bytes per character, allowing for a wider range of characters, including emojis.

### When to Use This Command:

- When you need to ensure that your database can store a broader range of Unicode characters, such as emojis or symbols.
- When you want to update a table’s character set and collation to align with modern best practices (many applications now use `utf8mb4`).

### insertion
```sql
INSERT INTO
    personal_data (name, call_number)
VALUES
    ('mostafa', '01154199659'), ("name", "0123456789");
```
### reading
```sql
SELECT * FROM personal_data;
SELECT name, call_number, another_field FROM personl_data;
SELECT id, score FROM table_name order by score;
SELECT score, name FROM table_name ORDER BY score DESC;
--this will show from greatest to smallest, ,you can change DESC key word to ASC
SELECT score, name FROM table_name WHERE score >=10 ORDER BY score DESC;
```

### updatae
```sql
update personal_data set name = 'ahmed' where name = 'mostafa';
```

### delete
```sql
DELETE FROM personal_data where name = 'ahmed';
-- if you didn't specify where, then every row of the table will be delelted
```

### aggregate functions
In database management an aggregate function is a function where the values of multiple rows
are grouped together as input on certain criteria to form a single value of more significant meaning.
```sql
count(), sum(), avg(), min(), max()
SELECT avg(score) FROM second_table;
SELECT sum(sales) FROM table_name;
SELECT score AS nums FROM second_table; --nums will be the name of the results
SELECT MAX(score) AS winner FROM table_name;
SELECT SUM(distinct score) FROM table_name -- here replicated score values will not be summed up cause of the word "distinct"
SELECT score, count(score) AS number FROM second_table group by score ORDER BY score DESC;
SELECT score, name FROM second_table WHERE name!='' ORDER BY score DESC;
```
- to get the number of rows in your table:
```sql
SELECT COUNT(*) FROM personal_data;
```
- to get the number of some value in your table
```sql
SELECT COUNT(*) FROM personal_data where name = 'mostafa';
```
this would the number of user whose name is mostafa

### JOIN
read [this](https://www.geeksforgeeks.org/sql-join-set-1-inner-left-right-and-full-joins/)

- `JOIN` is used to combine data or rows from two tables or more based on common field between them.
- JOIN is a clause used in SQL to link data from one table to another table using one or more data column shared between two tables, In other words, we combine data of the two existing tables into one.

```sql
SELECT *
FROM table1
INNER JOIN table2
ON table1.col1 = table2.col2;
```



```sql
SELECT *
FROM martian
INNER JOIN base
ON martian.base_id = base.base_id;
```
```sql
SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id = tv_show_genres.show_id
where tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;

select s_name, score, status, address_city, email_id, accomplishments from students
inner join marks on s.s_id = m.s_id inner join details d on  d.school_id = m.school_id;
```
### create Users
```sql
CREATE USER 'user_account'@'hostname' IDENTIFIED BY 'password';
--to allow user account to connect to the database server from any host use '%'
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
DROP 'USER'@'host'; -- delete a user
-- -you can create multiple user with a single create user statement ,
-- and delete multiple users with one drop statement, just separate them with comma
-- user() function returns current user name with it's host name used to connect to the server
SELECT USER();
--to change user password
ALTER USER 'username'@'hostname' IDENTIFIED BY 'new_pass';
```
using the Create User Statement only creates a new user but does not grant any privileges to the user account.
Therefore to grant privileges to a user account, the GRANT statement is used.

### Grant permission
- to view permission of a user account
```sql
SHOW GRANTS FOR user_account@'hostname';
```
The `*.*` in the output denotes that the newly created user account can only login to
the database server and has no other privileges.

- **to grant privilege to a user**
```sql
GRANT privilege_name ON object FOR user;
--to grant all privileges to a user to all databases
GRANT ALL PRIVILEGES ON *.* To user_name@host
-- the syntax `GRANT PRIVILEGE_NAME ON databasename.tablename TO user@host`
-- if you want to grant privileges to all tables in that database:
GRANT ALL PRIVILEGES ON databasename.* To username@host
GRANT SELECT ON nursing.cardio TO user@localhost
--granting privilege to all users
GRANT SELECT ON users_table TO '*'@'local host';


-- Granting Privileges on Functions/Procedures: While using functions and procedures, the Grant statement can be used to grant users the ability to execute the functions and procedures in MySQL.
-- Granting Execute Privilege: Execute privilege gives the ability to execute a function or procedure.
GRANT EXECUTE ON  PROCEDURE | FUNCTION  object TO user;
GRANT EXECUTE ON FUNCTION Calculatesalary TO 'Amit'@'localhost';
-- function named CalculateSalary to the user named Amit
```
### revoke
- The Revoke statement is used to revoke some or all of the privileges which have been granted to a user in the past.

```sql
REVOKE privileges ON object FROM user;
REVOKE SELECT, INSERT, DELETE, UPDATE ON Users FROM 'Amit'@'localhost';
REVOKE ALL ON Users FROM 'Amit'@'localhost';
REVOKE SELECT  ON Users FROM '*'@'localhost';
REVOKE EXECUTE ON PROCEDURE DBMSProcedure FROM '*'@'localhost';
```

### constraints
- Constraints are the rules that we can apply on the type of data in a table.

**some good ref**

[GFG](https://www.geeksforgeeks.org/sql-constraints/)

[FOREIGN KEY GOOD REF](https://www.cockroachlabs.com/blog/what-is-a-foreign-key/)

```sql
NOT NULL
UNIQUE
PRIMARY KEY
FOREIGN KEY
CHECK -- This constraint helps to validate the values of a column to meet a particular condition.
      -- That is, it helps to ensure that the value stored in a column meets a specific condition.
DEFAULT
AUTO_INCREMENT

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id),
    name VARCHAR(256) NOT NULL
);
CREATE TABLE orders (
  order _no INT PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
  product_sku INT NOT NULL REFERENCES books(product_sku)ON DELETE CASCADE ON UPDATE CASCADE,
); 
```
in the code above, ON DELETE CASCADE and ON UPDATE CASCADE specify that when
a row is deleted or a value is updated (respectively) in one table, the same
operation should be performed on the linked value or row in other tables.

### subquiry
```sql
Select NAME, LOCATION, PHONE_NUMBER from DATABASE 
WHERE ROLL_NO IN
(SELECT ROLL_NO from STUDENT where SECTION=’A’);
"""
    Explanation: First subquery executes “SELECT ROLL_NO from STUDENT where SECTION='A' returns ROLL_NO
    from STUDENT table whose SECTION is 'A'. Then outer-query executes it and return the NAME, LOCATION,
    PHONE_NUMBER from the DATABASE table of the student whose ROLL_NO is returned from inner subquery. 
"""
INSERT INTO table1  SELECT * FROM table2;
DELETE FROM Student2 WHERE ROLL_NO IN ( SELECT ROLL_NO FROM Student1 WHERE LOCATION = 'chennai');
SELECT cities.id, cities.name FROM cities WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California');
SELECT tv_shows.title, tv_show_genres.genre_id from tv_shows inner join tv_show_genres ON tv_shows.id = 
    (tv_show_genres.show_id) order by tv_shows.title, tv_show_genres.genre_id;
```
### importing sql dump 
- first insure the data base exist so create database first and use database
```bash
source path/to/sqlfile
```
if you want to import from the internet
```bash
echo "create database db_name" | sudo mysql -u 'root' -p
curl 'url_for_dbTable_file' -s | sudo mysql -u 'root' -p
# (-s) stands for silent which suppresses the progress meter and error messages from curl.
# another way
sudo mysql -u 'root' -p database name < sql_file_path
```
### truncate a table that have a reference to foreign key in it
```sql
SET FOREIGN_KEY_CHECKS = 0;
truncate table table_name;
SET FOREIGN_KEY_CHECKS = 1;
```

# connecting and disconnecting
```bash
mysql -h host -u user -p
```
host and user represent the host name where your MySQL server is running and the user name of your MySQL account

If you are logging in on the same machine that MySQL is running on, you can omit the host, and simply use the following
```bash
mysql -u user -p
```

### disconnecting
```mysql
/q
-- or
quit
```

### multiple lines queries
If you decide you do not want to execute a query that you are in the process of entering, cancel it by typing \c
```sql
mysql> SELECT
    -> USER()
    -> \c
mysql>
```
## queries
```sql
select version(), current_date; select now();
select SIN(PI()/4), (4+1)*5;
```
mysql [cheatsheet](https://devhints.io/mysql)
