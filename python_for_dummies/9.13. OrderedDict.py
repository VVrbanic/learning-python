from collections import OrderedDict

chapter_five = OrderedDict()

chapter_five ["for"] = "it is a loop"
chapter_five ["if"] = "you begin an if statment with if"
chapter_five["elif"] = "the other conditions use elif"
chapter_five["else"] = "the final contidion"
            
for key,value in chapter_five.items():
    print(key, "-", value)
            
