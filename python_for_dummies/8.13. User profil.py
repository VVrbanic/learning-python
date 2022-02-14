def building_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items(): 
        profile[key] = value 
    return profile
        
user_profile = building_profile('vera', 'vrbanic', location="zagreb", animal="cat", dream="happiness")

print(user_profile)
