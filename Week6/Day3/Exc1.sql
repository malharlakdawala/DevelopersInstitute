/* EXC1_A

select film.title, language.name from film
inner join language
on film.language_id=language.language_id
select film.title, film.description, language.name from film
left join language
on film.language_id=language.language_id

select film.title, film.description, language.name from film
right join language
on film.language_id=language.language_id

select film.title, film.description, language.name from film
full join language
on film.language_id=language.language_id


CREATE TABLE new_film (
 id SERIAL PRIMARY KEY,
 name VARCHAR (50) NOT NULL
);

INSERT INTO new_film (name)
VALUES('Terminator'), ('Star Wars'),('Dunkirk');



CREATE TABLE customer_review (
	review_id  SERIAL PRIMARY KEY,
	film_id INTEGER,
	language_id INTEGER,
	title varchar(50),
	score INTEGER,
	review_text  varchar,
	last_update Date,	
	FOREIGN KEY (film_id)  REFERENCES new_film (id) ON DELETE CASCADE,
	FOREIGN KEY (language_id)  REFERENCES language (language_id)
);

INSERT INTO customer_review(film_id,language_id,title,score,review_text,last_update) VALUES 
(1,2,'Nice movie',8,'Very nice movie, must watch','20/01/2021'),
(2,1,'Bad movie',4,'Bad Moview, Dont watch','30/03/2021');


--select * from customer_review inner join language on language.language_id=customer_review.language_id
--select * from customer_review inner join new_film on new_film.id=customer_review.film_id

--DELETE FROM new_film WHERE id=1
 select * from customer_review
 
----------- EXC1_B ---------
 
 UPDATE film set language_id=2 where film_id = 3 or film_id = 5 or film_id = 7;
  UPDATE film set language_id=3 where film_id = 4 or film_id = 6 or film_id = 8; 
  
  by seeing the database diagram,
  customer table is linked to Rental and Payment
  

  drop table customer_review 
  
  select count(*) from rental where return_date is NULL 
  
  select film.title, film.rental_rate, rental.rental_date from film
  inner join inventory
  on  inventory.film_id=film.film_id
  inner join rental on rental.inventory_id=inventory.inventory_id
  where rental.return_date is NULL order by film.rental_rate desc limit 30
 
  select * from film inner join film_actor on film.film_id = film_actor.film_id
  inner join actor on actor.actor_id = film_actor.actor_id 
  where actor.first_name = 'Penelope' and actor.last_name = 'Monroe' and film.description ilike '%sumo%'

  select * from film inner join film_category on film_category.film_id = film.film_id
  inner join category on film_category.category_id = category.category_id 
  where category.name = 'Documentary' and film.rating='R' and film.length<60

  
  select * from film inner join inventory on film.film_id = inventory.film_id
  inner join rental on inventory.inventory_id = rental.inventory_id
  inner join customer on rental.customer_id = customer.customer_id
  where customer.first_name='Matthew' and customer.last_name = 'Mahan' and film.rental_rate>4 and 
  rental.return_date between '28/07/2005' and '01/08/2005'
  
	
  select * from film inner join inventory on film.film_id = inventory.film_id
  inner join rental on inventory.inventory_id = rental.inventory_id
  inner join customer on rental.customer_id = customer.customer_id
  where customer.first_name='Matthew' and customer.last_name = 'Mahan' and 
  (film.title ilike '%boat%' or film.description ilike '%boat%') order by  film.replacement_cost desc limit 1
      */
