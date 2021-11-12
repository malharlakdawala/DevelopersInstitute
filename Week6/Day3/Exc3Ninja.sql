/*
select * from film inner join inventory on film.film_id=inventory.film_id
inner join rental on rental.inventory_id=inventory.inventory_id
where (film.rating = 'G' or film.rating= 'PG') and rental.return_date is not NULL 

*/

create table waitlist_children(
waitlist_id serial primary key,
	child_name varchar(50),
	movie_title varchar (255),
	
)
