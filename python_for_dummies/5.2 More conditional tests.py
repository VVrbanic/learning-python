#Tests for equality and inequality with string
#Tests using the lower() function
hand_cream = "Afrodita"
if hand_cream != "afrodita":
    print ("nope, try again")
    
if hand_cream.lower() == "afrodita":
    print("I told you not to use capital letters!")

#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
#Tests using the and keyword and the or keyword
grade = 2.67

if grade < 1.5:
    print("\nYou fail!")
elif grade >= 1.5 and grade < 2.5:
    print("\nThis result is really bad but you pass")
elif grade >= 2.5 and grade < 3.5:
    print("\nYou pass")
elif grade >= 3.5 and grade < 4.5:
    print("\nyou are above average!")
elif grade >= 4.5 and grade <= 5:
    print("\nwell done!")
else:
    print("\nError the trade must be higer or equal than 1 and loweror equal to 5")
    
 
#Test whether an item is in a list 
#Test whether an item is not in a lis
microsoft_office=["word","excel","powerpoint"]
find="python"
if find in microsoft_office:
    print("\nYes it is incuded")
if find not in microsoft_office:
    print("\nSorry you have to instal it yourself")

