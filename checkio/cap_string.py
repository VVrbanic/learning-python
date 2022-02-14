def correct_sentence(text: str) -> str:
    cap_string=text
    
    #if cap_string[0].isupper == False:
    cap_string=cap_string[0].upper() + cap_string[1:]
    
    if cap_string[-1] != ".":
        cap_string=cap_string + "."
        
    return cap_string