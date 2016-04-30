CREATE TABLE students (
  name text,
  year text,
  id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE courses (
  name text,
--   teacher text,
  id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE participation (
  student_id int NOT NULL,
  course_id int NOT NULL,
  score int NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (course_id) REFERENCES courses(id)
);

insert into students(name, year) values
  ("Y. Barbitov", 2015),
  ("M. Parr", 2015),
  ("O. Shchepin", 2015),
  ("V. Kuzyk", 2015),
  ("A. Zaharova", 2015),
  ("E. Jivkoplyas", 2015),
  ("L. Savochkina", 2014),
  ("N. Shilyaev", 2014),
  ("I. Korvigo", 2014);

insert into courses(name) values
  ("Python"),
  ("Discrete Math"),
  ("R");

insert into participation values
  (1, 1, 3), (1, 2, 3), (1, 3, 4),
  (2, 1, 5), (2, 2, 3), (2, 3, 3),
  (3, 1, 5), (3, 2, 5), (3, 3, 5),
  (4, 1, 4), (4, 2, 5), (4, 3, 4),
  (5, 1, 4), (5, 2, 3), (5, 3, 5),
  (6, 1, 4), (6, 2, 4), (6, 3, 5),
  (7, 1, 4), (7, 2, 5), (7, 3, 5),
  (8, 1, 5), (8, 2, 4), (8, 3, 3),
  (9, 1, 5), (9, 2, 3), (9, 3, 3);