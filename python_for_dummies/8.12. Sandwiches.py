def sendwiches(*toppings):
    print("This sandwich is made of:")
    for topping in toppings:
        print("-", topping)
    print("\n")

sendwiches("chesse")
sendwiches("chesse", "tomato", "salad", "onion" )
sendwiches("chesse", "tomato", "salad", "onion", "paprika", "sour cream")