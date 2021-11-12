/* Ex2_A
SELECT * FROM film inner join inventory on film.film_id=inventory.film_id 
inner join rental on inventory.inventory_id = rental.inventory_id
where rental.return_date is NULL

SELECT * FROM film inner join inventory on film.film_id=inventory.film_id 
inner join rental on inventory.inventory_id = rental.inventory_id
inner join customer on rental.customer_id = customer.customer_id
where rental.return_date is NULL 
order by customer.customer_id 

SELECT * FROM public.film_list where actors ilike '%Joe Swank%' and category ilike '%action%'


Ex2_B

select count(*), country.country, city.city from store 
inner join address on address.address_id = store.address_id
inner join city on address.city_id = city.city_id
inner join country on country.country_id = city.country_id
group by country, city


select sum(film.length), store.store_id from film
inner join inventory on inventory.film_id = film.film_id
inner join store on store.store_id = inventory.store_id
group by store.store_id

select sum(film.length), store.store_id from film
inner join inventory on inventory.film_id = film.film_id
inner join store on store.store_id = inventory.store_id
inner join rental on rental.inventory_id =  inventory.inventory_id
where rental.return_date is not NULL
group by store.store_id

select * from customer
left join address on customer.address_id=address.address_id
left join city on city.city_id=address.city_id
left join store on store.address_id = address.address_id


CREATE VIEW safe_list AS 
select film.title, film.description,film.length from film inner join film_category on film_category.film_id = film.film_id
inner join category on category.category_id=film_category.category_id
where category.name not ilike '%horror%' and film.title not ilike '%beast%' and film.title not ilike '%ghost%' 
and film.title not ilike '%dead%' and film.title not ilike '%zombie%' and film.title not ilike '%undead%';

select sum(length)/(60) from public.safe_list --hours
select sum(length)/(60*24) from public.safe_list --days

*/