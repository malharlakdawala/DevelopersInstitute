--Exc1
--select * from items order by item_price asc
--select * from items where item_price>=80 order by item_price desc
--select*from customers order by first_name asc 
--select last_name from customers order by last_name desc

--ALter table customers ADD Column cust_id SERIAL PRIMARY KEY;
--ALter table items ADD Column item_id SERIAL PRIMARY KEY;

--create table purchases(
--item_id integer,
--customer_id integer,
--Foreign key (customer_id) references customers(cust_id),
--Foreign key (item_id) references items(item_id)
--)

--insert into purchases(customer_id,item_id) values (1,1),(2,1),(1,3);
--ALTER TABLE purchases ALTER COLUMN item_id SET DEFAULT 1;
--delete from purchases where customer_id = 1
--insert into purchases(customer_id,item_id) values (1,1),(3,1),(1,3),(4,3),(5,2),(3,2);
/*
select * from items
inner join purchases
on items.item_id = purchases.item_id
*/
/*
select customers.first_name, customers.last_name, customers.cust_id, items.item_name, items.item_price
from customers
inner join purchases on purchases.customer_id = customers.cust_id
inner join items on purchases.item_id = items.item_id
*/

select customers.first_name, customers.last_name, items.item_name, items.item_price
from purchases
inner join customers on purchases.customer_id = customers.cust_id
inner join items on purchases.item_id = items.item_id
where customer_id = 4

/*
select customers.first_name, customers.last_name, items.item_name, items.item_price
from purchases
inner join customers on purchases.customer_id = customers.cust_id
inner join items on purchases.item_id = items.item_id
where items.item_name = 'Large Desk' or items.item_name = 'Small Desk'
*/

--insert into items (item_name,item_price) values ('Hard Disk',150)
--insert into purchases (item_id,customer_id) values (4,3)
/*
select customers.first_name, customers.last_name, items.item_name, items.item_price
from purchases
inner join customers on purchases.customer_id = customers.cust_id
inner join items on purchases.item_id = items.item_id
where first_name = 'Scott'
*/

--------------------------------
