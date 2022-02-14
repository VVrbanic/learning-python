favorite_languages = {
                    "jen" : "python",
                    "sarah": "c", 
                    "edward": "ruby", 
                    "phil": "python", }
                    
important_people = ["hans","mars", "anna", "sarah"]

for people in important_people:
    if people in favorite_languages.keys():
        print("Thank you for anwsering the poll.")
    else:
        print("Pleas anwser the poll.")