CREATE TABLE Student (
	student_id SERIAL,
	first_name varchar(255),
	last_name varchar(255),
	address varchar(255),
	email varchar(255),
	primary key(student_id)

);

CREATE TABLE Course ( 
	course_id Integer,
        name varchar(255),
	primary key (course_id)
);

CREATE TABLE Takes (
	student_id Integer,
	course_id Integer,
	grade float,
	primary key (student_id, course_id),
	foreign key (student_id) references Student ON DELETE CASCADE,
	foreign key (course_id) references Course ON DELETE CASCADE 
);
