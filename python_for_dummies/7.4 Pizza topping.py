topping=""
prompt="What topping do you want to add to your pizza? "
prompt +="\n(If you are done adding please type in 'quit')"
while topping!="quit":
    topping=input(prompt)
    if topping == "quit":
        continue
    else:
        print("Adding", topping)