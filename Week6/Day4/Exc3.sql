/*Exc3 A

select first_name, last_name from employees 
where salary > (select salary from employees where last_name = 'Kochhar')


select first_name, last_name from employees 
where manager_id in (select employees.manager_id from employees 
					inner join departments on employees.department_id=departments.department_id
				   inner join locations on locations.location_id = departments.location_id
					 inner join countries on countries.country_id=locations.country_id
					 where countries.country_name = 'United States of America')

select first_name, last_name from employees 
where department_id in (select employees.department_id from employees inner join departments on departments.department_id=employees.department_id
					  where departments.department_name = 'IT')
					 
select first_name, last_name from employees 
where salary > (select avg(salary) from employees)

 select first_name, last_name from employees 
where salary in (select min(salary) from employees group by department_id)

 select first_name, last_name from employees
 where department_id not in (select employees.department_id from employees inner join departments on departments.department_id=employees.department_id
					  where departments.department_name = 'IT')
					  

SELECT DISTINCT salary FROM employees as e1
where 5 = (select count(distinct salary) from employees as e2
		  where e1.salary<=e2.salary)
		 
SELECT DISTINCT salary FROM employees as e1
where 4 = (select count(distinct salary) from employees as e2
		  where e1.salary>=e2.salary)

 select departments.department_name from departments
 where department_id not in (select department_id from employees)
  
  done lots of eg on joins, so skipping it
  
  update employees set phone_number = '999' where phone_number ilike '%124%';
  select*from employees
  
 select first_name from employees where length(first_name)>8 
 
 update employees set email = upper(concat(left(first_name,1),(left(last_name,3)),'@example.com'));
  select*from employees;
										   */ 
 
 
 