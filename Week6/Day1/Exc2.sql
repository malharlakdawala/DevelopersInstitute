--insert into students(last_name,first_name,birth_date) values ('Benichou','Marc','02/11/1989');
--insert into students(last_name,first_name,birth_date) values ('Cohen','Yoan','03/12/2010');
--insert into students(last_name,first_name,birth_date) values ('Benichou','Lea','27/07/1987');
--insert into students(last_name,first_name,birth_date) values ('Dux','Amelia','07/04/1996');
--insert into students(last_name,first_name,birth_date) values ('Grez','David','14/06/2003');
--insert into students(last_name,first_name,birth_date) values ('Simpson','Omer','03/10/1980');

--select*from students
--select first_name,last_name from students;
--select first_name,last_name from students where id=2
--select first_name,last_name from students where last_name='Benichou' AND first_name='Marc';
--select first_name,last_name from students where last_name='Benichou' or first_name='Marc';
--select first_name,last_name from students where first_name LIKE '%a%';
--select first_name,last_name from students where first_name LIKE 'a%';
--select first_name,last_name from students where first_name LIKE '%a';
--select first_name,last_name from students where id=3 or id=1
select * from students where birth_date>'01/01/2000';
