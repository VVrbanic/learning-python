def split_list(items: list) -> list:

    if len(items) % 2 == 0:
        num = int(len(items) / 2)
    else:
        num= int(len(items) / 2) + 1
    
    b= items[:num]
    c= items[num:]
 
    a= [b,c]
    
    return a