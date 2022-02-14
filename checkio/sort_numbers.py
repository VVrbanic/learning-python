def checkio(numbers_array: tuple) -> list:
    number= list(numbers_array)
    
    number=sorted(number, key=abs)
    return number