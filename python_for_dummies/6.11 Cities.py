#The keys for each city’s dictionary should be something like country, population, and fact

cities={
        "zagreb" : {
                  "country":"croatia",
                  "population":"1000000",
                  "fact":"capital city",
                   },
        "paris": {
                  "country":"france",
                  "population":"2141000",
                  "fact":"capital city",
                  }
        }
        
for city, city_info in cities.items():
        country=city_info["country"]
        fact=city_info["fact"]
        print(city.title(), "is in", country.title(), "and has a population of around", city_info["population"]+". Fun fact is the", fact.upper()+".")
        
        
                