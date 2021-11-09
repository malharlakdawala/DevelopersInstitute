--update students set birth_date = '02/11/1998' where last_name='Benichou'
--update students set last_name = 'Guez' where first_name='David'
--delete from students where first_name='Lea'
--select count(*) from students
--select count(*) from students where birth_date>'01/01/2000'
--ALter table customers ADD Column math_grade integer;

--ALTER TABLE students ADD COLUMN math_grade integer;
/*
update students set math_grade = 80 where id = 1;
update students set math_grade = 90 where id = 2 or id=4;
update students set math_grade = 40 where id = 6;
select*from students*/
--select count(*) from students where math_grade>83
--insert into students (last_name, first_name,birth_date,math_grade) values ('Simpson','Omer','2010-12-03',40)
--select*from students
--select first_name, count(*) from students group by first_name

--select sum(math_grade) from students