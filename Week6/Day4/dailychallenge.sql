/*
create table items(
item_id  serial primary key ,
	item_name varchar(20),
	price integer
);

create table orders(
order_id serial primary key ,
	item_id integer,
	qty integer,
	foreign key (item_id) references items(item_id)
);

insert into items (item_name,price) values ('Bag',10),('Soap',15),('Shampoo',5),('Watch',8),('Mobile',100),('Laptop',300);
insert into orders (item_id,qty) values (1,5),(2,3),(3,5),(4,6);

create or replace function returnTotal(itm integer, qty integer)
returns integer as $totalprice$
begin
return itm*qty;
end;
$totalprice$ language plpgsql;
select returnTotal(5,6);


create table users(
user_id serial primary key,
name varchar(20),
	order_id integer,
	foreign key (order_id) references orders (order_id)
);

insert into users (name,order_id) values ('ram',1),('mohan',2),('raja',4),('roy',3);

create or replace function totalvalue(ord integer)
returns integer as $total$
begin
return (select (orders.item_id * orders.qty) from users inner join orders on users.order_id = orders.order_id 
		where orders.order_id = ord);
end;
$total$ language plpgsql;
*/
select totalvalue(3)

