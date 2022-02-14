import re
def popular_words(text: str, words: list) -> dict:

    text = text.lower()
    text = re.split(', | |\n',text)
    """a = {}
    for i in range (0, len(words)):
        a[words[i]] = 0
        print(a)
    
    for i in range (0, len(text)):
        print(text[i])
        if text[i] in words:
            a[text[i]] =  a[text[i]] + 1
            print(a)"""
            
    return text