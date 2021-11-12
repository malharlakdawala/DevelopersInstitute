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



create table brand(
brand_id serial primary key,
	brand_name varchar(50)
);

create table colour(
colour_id serial primary key,
	colour_name varchar(50)
);

create table shoes(
brand_id integer,
	colour_id integer,
	foreign key (brand_id) references brand(brand_id) on delete cascade,
	foreign key (colour_id) references colour(colour_id) on delete cascade	
);

insert into brand (brand_name) values ('Nike'),('Reebok'),('Puma'),('Bata'),('Paragon'),('Woodland');
insert into colour (colour_name) values ('Red'),('Blue'),('Black'),('Green'),('Yellow'),('Violet');
insert into shoes (brand_id, colour_id) values (1,2),(2,2),(3,1),(5,1),(1,1);

select * from brand inner join shoes on brand.brand_id = shoes.brand_id 
inner join colour on colour.colour_id = shoes.colour_id


select * from brand left join shoes on brand.brand_id = shoes.brand_id 
left join colour on colour.colour_id = shoes.colour_id



select * from brand right join shoes on brand.brand_id = shoes.brand_id 
right join colour on colour.colour_id = shoes.colour_id

select * from brand right outer join shoes on brand.brand_id = shoes.brand_id 
right outer join colour on colour.colour_id = shoes.colour_id
*/

select * from brand full join shoes on brand.brand_id = shoes.brand_id 
full join colour on colour.colour_id = shoes.colour_id