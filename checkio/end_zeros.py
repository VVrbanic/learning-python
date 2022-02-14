def backward_string(val: str) -> str:
    a=""
    for i in range(0,len(val)):
        a=a+val[len(val)-1-i]
    return a
