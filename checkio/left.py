def left_join(phrases):
    l = ""
    for i in range (0, len(phrases)):
        if i == 0:
            l=phrases[i]
        else:
            l = l + "," + phrases[i]
        print(l)
        
    l = l.replace("right", "left")   
    return l