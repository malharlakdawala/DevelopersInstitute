/*Exc1

create table customer_profile_dc(
id serial primary key,
job varchar (50)
);

create table customer_dc(
id serial primary key,
name varchar (50),
job_id integer,
foreign key (job_id) references customer_profile_dc (id) On Delete Cascade
);

insert into customer_profile_dc (job) values ('developer'),('designer'),('manager'),('Exectuive Officer');
insert into customer_dc (name, job_id) values ('mohan',2),('rohan',1),('lohan',2),('chauhan',3);


select * from customer_dc inner join customer_profile_dc on 
customer_dc.job_id = customer_profile_dc.id

select * from customer_dc right join customer_profile_dc on 
customer_dc.job_id = customer_profile_dc.id

select * from customer_dc full join customer_profile_dc on 
customer_dc.job_id = customer_profile_dc.id

select * from customer_dc left outer  customer_profile_dc on 
customer_dc.job_id = customer_profile_dc.id

delete from customer_dc where name= 'rohan';
delete from customer_profile_dc where job= 'manager';

select * from customer_dc
*/
