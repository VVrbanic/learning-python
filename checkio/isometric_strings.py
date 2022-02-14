def isometric_strings(str1: str, str2: str) -> bool:
    popis={}
    a = True
    if str1=="":
        return a
    
    for i in range(0,len(str1)):
        if str1[i] in popis:
            if str2[i]!=popis[str1[i]]:
                a = False
                break
        else:
            popis[str1[i]]=str2[i]
    return a