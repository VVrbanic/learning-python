sandwich_order=["tuna", "salami", "cheese", "pastrami", "pastrami", "triple chesse", "vege", "pastrami"]
sandwich_finish=[]

print("Sorry no pastrami today!")

while "pastrami" in sandwich_order:
    sandwich_order.remove("pastrami")

print (sandwich_order)

while sandwich_order:
    sandwich=sandwich_order.pop()
    print("Making", sandwich)
    sandwich_finish.append(sandwich)

for sandwichs in sandwich_finish:
    print(sandwichs.title(), "is ready!")