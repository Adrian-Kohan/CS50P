-- Find out where and what time exactly the crime happened (bakery, 10:15am)
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';
-- Find out the name and id of origin and destination airport  (8, CSF and )
SELECT * FROM airports;
SELECT * FROM flights WHERE origin_airport_id = 8 AND day = 28 AND hour >= 10 AND minute > 15;