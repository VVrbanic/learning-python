#If a person is under the age of 3, the ticket is free; 
#if they are between 3 and 12, the ticket is $10; 
#if they are over age 12, the ticket is $15.
prompt = "How old are you?"
prompt += "\nIf thats all write 0. "
count= 0
while True:
    age=input(prompt)
    age=int(age)
    if age == 0:
        print("That will be", str(count)+ "$. Thank you come again!")
        break
    if age < 3:
        print("You go free!")
    elif age < 12:
        count = count + 10
        print("That will be $10.")
    elif age > 11:
        count = count + 15
        print ("That will be $15")