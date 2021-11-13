/* Exc2 A

ALTER TABLE employees ADD COLUMN commision_pct float;
update employees set email='not available', commision_pct = 0.10 where department_id =5;

UPDATE employees INNER JOIN departments ON employees.department_id=departments.department_id 
SET employees.email='available' WHERE departments.department_name = 'Accounting';

update employees set salary=8000 where salary =5000 and employee_id=105

Exc2 B

select  count(DISTinct job_id) from employees
select  count(job_id), job_id from employees group by job_id

select abs(max(salary)-min(salary)) as difference from employees
select min(salary),manager_id from employees group by manager_id

select avg(employees.salary), employees.job_id, jobs.job_title from employees inner join
jobs on employees.job_id=jobs.job_id
 where jobs.job_title != 'Programmer' group by employees.job_id,jobs.job_title
 
select avg(salary), job_id from employees group by job_id having count(*)>3

Exc2 C

alter table locations rename state_province to state;
select*from locations;

alter table locations
add primary key (location_id);

Exc2 D
create table new_countries(
country_id integer not null unique,
	country_name varchar(20),
	check(country_name IN ('India','Italy','China'))
);
insert into new_countries(country_id, country_name) values (1,'India'),(2,'India'),(3,'China'),(4,'Italy'),(5,'Italy');

select * into new_countries_copy from new_countries;
select*from new_countries_copy

create table new_jobs(
	job_id integer,
	job_title varchar(30) default '',
	min_salary integer default 8000,
	max_salary integer default NULL,
	check(max_salary<25000)
)
insert into new_jobs (job_id) values (1);
select*from new_jobs;

create table new_employees(
	employee_id integer unique, 
	first_name varchar(20), 
	last_name varchar(20), 
	email varchar(20), 
	phone_number integer,
	hire_date date, 
	job_id integer,
	salary integer,
	foreign key (job_id) references new_jobs (job_id)
);

Exc 2 E


insert into new_countries(country_id, country_name) values (7,'India'),(8, 'Italy');
select*from new_countries_copy;*/
