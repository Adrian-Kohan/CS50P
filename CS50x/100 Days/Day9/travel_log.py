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
def add_new_country(count, visit, city):
    travel_log.append({
        "country" : count
        "visits": visit
        "cities" : city
    })

add_new_country("Russia, 2, ["Moscow", "Saint Peters"]")