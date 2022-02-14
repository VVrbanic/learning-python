def between_markers(text: str, begin: str, end: str) -> str:
    a=""
    count=0
    for i in range(0, len(text)):
         
        if count == 1:
            if text[i] == end:
                count = count+1
            else:
                a=a+text[i]
        if text[i] == begin:
            count = 1 
    # your code here
    return a