#Make a dictionary called favorite_places. 
#Think of three names to use as keys in the dictionary, and store one to three favorite places for each person
 
favourite_places={
                  "tim":["sad","argentina", "peru"],
                  "stanislav":["srbia","bih","croatia"],
                  "lisa":["japan"]
                  }
for name,countries in favourite_places.items():
    if len(countries)==1:
        for country in countries:
            print(name,"favourite country is:\n\t", country)
    else: 
        print(name, "favourite countires are:")
        for country in countries:
            print("\t",country)