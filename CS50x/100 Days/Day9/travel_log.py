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
def add_new_country(country, visits, cities):
    travel_log.append({
        "country" : country
        "visits" : visits
        "cities" : cities
    })
    
add_new_country("Russia, 2, ["Moscow", "Saint Peters"]")