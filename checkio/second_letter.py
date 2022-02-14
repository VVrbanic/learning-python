def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
        second_index("sims", "s") == 3
    """
    count = 1
    a = None
    for i in range(0,len(text)):
        if text[i] == symbol:
            if count == 2:
                a = i
                break
            else:
                count=count+1
    return a