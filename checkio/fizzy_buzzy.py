#"Fizz Buzz" if the number is divisible by 3 and by 5;
#"Fizz" if the number is divisible by 3;
#"Buzz" if the number is divisible by 5;
#The number as a string for other cases.

def checkio(number: int) -> str:
    a=""
    if number%5 == 0 and number%3 == 0:
        a = "Fizz Buzz"
    elif number%5 == 0:
        a = "Buzz"
    elif number%3 == 0:
        a = "Fizz"   
    else:
        a = str(number)
    return a