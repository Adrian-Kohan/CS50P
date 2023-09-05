-- Find out where and what time exactly the crime happened (bakery, 10:15am)
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';
-- Find out the name and id of origin and destination airport  (origin = 8, CSF)
SELECT * FROM airports;
-- Find out the destination of fiftville flights in 28 July after 10:15 (7, 5, 4 means Dubai, Dallas and New York City)
SELECT * FROM flights WHERE origin_airport_id = 8 AND day = 28 AND hour >= 10 AND minute > 15;
SELECT * FROM bakery_security_logs WHERE day = 28 AND hour = 10 AND minute <= 20;
SELECT * FROM interviews WHERE month = 7 AND day = 28 AND transcript LIKE %bakery%;