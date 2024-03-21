travel_log = [
{
    "country" : "France",
    "visits" : 12,
    "cities" : ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#-------------------------------------------------------------------------------------------------#
# Do not change the code above
# TO DO: Write a function that will allow a new country to be added to the travel_log.
#-------------------------------------------------------------------------------------------------#
def add_new_country(country, visits, cities):
    travel_log.append({
        "country" : country,
        "visits" : visits,
        "cities" : cities
    })
#-------------------------------------------------------------------------------------------------#
# Do not change the code below
#-------------------------------------------------------------------------------------------------#
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
#-------------------------------------------------------------------------------------------------#

# DONE!!!! :))

# Another solution:

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country