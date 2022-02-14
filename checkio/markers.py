"""The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string. 
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.  +
If the final marker comes before the initial marker, then return an empty string.+"""

def between_markers(text: str, begin: str, end: str) -> str:
    a=""
    begin2=text.find(begin)
    end=text.find(end)
    print(begin, end)
    if begin2 == end:
        a = text
    elif begin2 == -1:
        a = text[:end]
    elif end == -1:
        a = text[begin2 + len(begin) :]
    elif begin2 > end:
        a = ""
    else:
        a=text[begin2 + len(begin) : end]
        
    return a