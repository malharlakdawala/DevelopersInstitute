--select first_name, last_name from customers order by first_name desc limit 2;

--delete from purchases where customer_id = 3
/*
select customers.first_name, customers.last_name, items.item_name, items.item_price
from customers
inner join purchases on customers.cust_id = purchases.customer_id
inner join items on items.item_id=purchases.item_id
*/
