--select * from customer
--select first_name ||' '|| last_name as full_name from customer
--select distinct create_date from customer
--select*from customer order by first_name desc
--select film_id, title, description, release_year, rental_rate from film order by rental_rate asc
--select address||' '||address2 , phone from address
--select*from film where film_id=15 or film_id=150
--select * from film where title='Alien Center'
--select * from film where title ilike '%al%'
--select*from film order by rental_rate asc limit 10
--select * from film order by rental_rate asc offset 10 fetch first 10 row only
/*
select customer.first_name ||' '|| customer.last_name as full_name, customer.customer_id, payment.amount, payment.payment_date
from customer
inner join payment
on customer.customer_id=payment.customer_id
order by customer_id asc 
*/

-- film not in inventory
/*
select film.title, film.description, film.film_id 
from film where film_id 
not in (select film_id from inventory)
*/
/*
select city.city, country.country from city
inner join country on city.country_id=country.country_id*/

select customer.first_name ||' '|| customer.last_name as full_name, customer.customer_id, payment.amount, payment.payment_date, payment.staff_id
from customer
inner join payment
on customer.customer_id=payment.customer_id
order by payment.staff_id asc 