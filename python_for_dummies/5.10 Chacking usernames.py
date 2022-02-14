current_list = ["hannah", "melania", "lucas", "Fred", "mihovil"]
new_list = ["fred", "nora", "danny", "sunny", "Melania"]

current_list_lower = [x.lower() for x in current_list]

for new in new_list:
    
    if new.lower() in current_list_lower:
        print("\n"+new+" has already been used, please try again")
    else:
        print("\n"+new+" welcome to the platform")
        