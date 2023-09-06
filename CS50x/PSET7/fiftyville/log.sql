-- Find out where and what time exactly the crime happened (bakery, 10:15am)
SELECT *
  FROM crime_scene_reports
 WHERE month = 7
   AND day = 28
   AND street = 'Humphrey Street';

-- Reading the transcript of each witnesses for gettinf more details
SELECT *
  FROM interviews
 WHERE month = 7
   AND day = 28
   AND transcript LIKE '%bakery%';

-- Finding bakery security logs based on first witness transcript
SELECT *
  FROM bakery_security_logs
 WHERE day = 28
   AND hour = 10
   AND minute <= 30
   AND activity = 'exit';

-- Finding bank accounts that withdrawing money from Leggett Street based on second witness transcript
SELECT *
  FROM atm_transactions
 WHERE month = 7
   AND day = 28
   AND atm_location = 'Leggett Street'
   And transaction_type = 'withdraw';

-- Finding accounts number based on bank accounts that withdrawing money from Leggett Street ATM
SELECT *
  FROM bank_accounts
 WHERE account_number = 28500762
   OR account_number = 28296815
   OR account_number = 76054385
   OR account_number = 49610011
   OR account_number = 16153065
   OR account_number = 25506511
   OR account_number = 81061156
   OR account_number = 26013199;

-- Finding phone numbers that thief calls after thieft based on third witness transcript
SELECT *
  FROM phone_calls
 WHERE day = 28
   AND duration < 60;

-- Find out the name and id of origin airport (origin = 8, CSF)
SELECT * FROM airports;

-- Find out the destination of earliest fiftville flight in 29 July based on third witness transcript(4 means New York City)
SELECT *
  FROM flights
 WHERE origin_airport_id = 8
   AND day = 29;

-- Limiting the list of passengers to flight id based on clues
SELECT *
  FROM passengers
 WHERE flight_id = 36;

-- Mixing all the clues to limit the names
SELECT DISTINCT name
  FROM people, passengers, phone_calls, bakery_security_logs, bank_accounts
 WHERE passengers.passport_number = people.passport_number
   AND passengers.flight_id = 36
   AND phone_calls.caller = people.phone_number
   AND phone_calls.duration< 60
   AND bakery_security_logs.license_plate = people.license_plate
   AND bakery_security_logs.day = 28
   AND bakery_security_logs.hour = 10
   AND bakery_security_logs.minute <= 30
   AND bakery_security_logs.activity = 'exit';

-- Getting all information about these 3 people
SELECT *
  FROM people
WHERE name = 'Sofia'
  OR name = 'Bruce'
  OR name = 'Kelsey';

--By comparing the resuls of person id from bank accounts (that was limited with some account number before) with these 3 person id we find out that Bruce is the thief
SELECT name
  FROM phone_calls, people
 WHERE phone_calls.caller = '(367) 555-5533';

-- Finding the receiver number of Bruce phone call
SELECT receiver
  FROM phone_calls
 WHERE caller = '(367) 555-5533'
   AND day = 28
   AND duration < 60;

-- Finding the name of receiver who is the accomplice
SELECT name
  FROM  people
 WHERE phone_number = '(375) 555-8161';

