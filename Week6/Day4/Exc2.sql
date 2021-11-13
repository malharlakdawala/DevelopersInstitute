/* Exc2 A

ALTER TABLE employees ADD COLUMN commision_pct float;
update employees set email='not available', commision_pct = 0.10 where department_id =5;

UPDATE employees INNER JOIN departments ON employees.department_id=departments.department_id 
SET employees.email='available' WHERE departments.department_name = 'Accounting';

update employees set salary=8000 where salary =5000 and employee_id=105

Exc2 B
*/
