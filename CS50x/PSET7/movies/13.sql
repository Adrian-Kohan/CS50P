SELECT name FROM people WHERE people.name != 'Kevin Bacon' AND id IN (SELECT DISTINCT person_id  FROM stars WHERE movie_id IN (SELECT movie_id ))