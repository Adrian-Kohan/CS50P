travel_log = [
{
"country": "France",
"visits": 12,
"cities": ["Paris", "Lille","Di jon"]
},
{
"country": "Germany",
"visits": 5,
"cities": ["Berlin", "Hambura", "Stuttgart"]
},
]
def add_new_country(county_visited, times_visit, cities_visited):
    travel_log.append({
        "country": county_visited,
        "visits": times_visit,
        "cities": cities_visited
    },)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)