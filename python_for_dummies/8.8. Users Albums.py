def make_album(artist, name, years=""):
    album={"artists":artist, "albums":name}
    if years:
        album["year"]=years
    return album
    
    
print("If you want to quit write 'q'")
while True:
    ar_name=input("Artist: ")
    if ar_name=="q":
        break
    
    al_name=input("Album: ")
    if al_name=="q":
        break
    
    year=input("If you know don't know the year press enter. Year: ")
    if year=="q":
        break
    
    music= make_album( ar_name, al_name, year)
    print(music)