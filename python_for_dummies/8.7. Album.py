def make_album(artist, name, years=""):
    album={"artists":artist, "albums":name}
    if years:
        album["year"]=years
    return album
    
    
music=make_album("robyn","body talk","2013")
print(music)

music=make_album("beyonce","beyonce")
print(music)

music=make_album("frank ocean","blonde")
print(music)
    