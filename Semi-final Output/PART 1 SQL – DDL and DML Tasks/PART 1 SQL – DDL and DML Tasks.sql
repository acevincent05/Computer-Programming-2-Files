CREATE DATABASE Pre_Enrollees;

USE Pre_Enrollees;

CREATE TABLE new_students (
	ID varchar(5) not null primary key,
	name varchar(100) not null,
	age int not null,
    shs_strand varchar(10) not null,
    chosen_program varchar (10) not null
    );
    
CREATE TABLE transfer_students (
	ID varchar(5) not null primary key,
	name varchar(100) not null,
	age int not null,
    prev_program varchar(10) not null,
    new_program varchar (10) not null
    );
    
INSERT INTO new_students (ID, name, age, shs_strand, chosen_program) VALUES
('N0001', 'Angela Reyes', 18, 'STEM', 'BSIT'),
('N0002', 'Mark Dela Cruz', 19, 'ABM', 'BSBA'),
('N0003', 'Janelle Santos', 18, 'HUMSS', 'BSED'),
('N0004', 'Kevin Ramirez', 20, 'TVL', 'BSHM'),
('N0005', 'Sofia Gonzales', 19, 'STEM', 'BSCS'),
('N0006', 'Liam Villanueva', 18, 'GAS', 'BSCRIM'),
('N0007', 'Bianca Mendoza', 19, 'HUMSS', 'BSPsych'),
('N0008', 'Joshua Tan', 18, 'STEM', 'BSCE'),
('N0009', 'Clarisse Lim', 20, 'ABM', 'BSBA'),
('N0010', 'Darren Cruz', 19, 'TVL', 'BSHM');

INSERT INTO transfer_students (ID, name, age, prev_program, new_program) VALUES
('T0001', 'Erika Flores', 20, 'BSBA', 'BSIT'),
('T0002', 'Miguel Santos', 21, 'BSCRIM', 'BSCS'),
('T0003', 'Rina Bautista', 22, 'BSHM', 'BSED'),
('T0004', 'Aaron Lopez', 20, 'BSCE', 'BSIT'),
('T0005', 'Faye Navarro', 19, 'BSPsych', 'BSN'),
('T0006', 'Jiro Pascual', 21, 'BSCS', 'BSBA'),
('T0007', 'Nicole Chua', 20, 'BSN', 'BSPsych'),
('T0008', 'Enzo Dizon', 22, 'BSIT', 'BSCRIM'),
('T0009', 'Lara Umali', 21, 'BSED', 'BSHM'),
('T0010', 'Troy Aguilar', 23, 'BSHM', 'BSCE');


SELECT * FROM new_students;

SELECT * FROM transfer_students;

# change 'Darren Cruz' name to 'Kyle Cruz'
UPDATE new_students SET name = 'Kyle Cruz' where id = 'N0010';

# delete a students based on the selected ID
DELETE FROM transfer_students where ID = 'T0004';

# view students with the STEM SHS strand
SELECT * FROM new_students
WHERE shs_strand = 'STEM';

# view students in alphabetical order 
SELECT * FROM new_students
ORDER BY name;

# view students by age in descending order
SELECT * FROM new_students
ORDER BY age DESC;

# view students' name and age arranged alphabetically with their age
SELECT * FROM new_students
ORDER BY name ASC, age DESC;

# view students limited to 5
SELECT * FROM new_students
ORDER BY ID
LIMIT 5;

# view students grouped by their SHS strands
SELECT shs_strand, COUNT(*) AS strand_num
FROM new_students
GROUP BY shs_strand
ORDER BY strand_num DESC;

