def sum_numbers(text: str) -> int:
    a = 0
    res = [int(i) for i in text.split() if i.isdigit()]
           
    for i in range (0, len(res)):
        a = a + res[i]
    
    return a

