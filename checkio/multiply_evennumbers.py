def checkio(array):
    a=0
    for i in range(0, len(array)):
        
        if i==0:
            a=a+array[i] 
        elif i % 2 == 0:
            a=a+array[i]
        else:
            next        
    if not array:
        return 0
        
    a=a*array[-1]
    return a