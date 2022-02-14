def call_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def great(magicians_names, great_magicians_names):
    while magicians_names:
        current_magician = "great " + magicians_names.pop()
        great_magicians_names.append(current_magician)
        
magic=["Houdini", "blaine", "Coppefield", "Angel", "dynamo"]
#copy_magic=magic.copy()
great_magic=[]


great(magic[:], great_magic)

call_magicians(magic)
call_magicians(great_magic)