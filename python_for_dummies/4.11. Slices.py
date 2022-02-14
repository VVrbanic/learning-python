guests= ["lars", "perl", "garneth","connie","sadie","steven","amethyst"]

print("the first three guests are:")
for guest in guests[0:3]:
    print(guest)

print("\n")

print("the middle three guests are:")
for guest in guests[5:8]:
    print(guest)
    
print("\n")

print("the last three guests are:")
for guest in guests[-3:]:
    print(guest)
    
print("\n")