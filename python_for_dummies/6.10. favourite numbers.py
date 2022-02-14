favourite_numbers={
                    "LH":[44,1],
                    "VB":[77,2],
                    "MV":[33,3],
                    "CS":[55,6],
                    "SP":[11,10],
                    "AG":[99,17],
                    "RK":[88,12],
                    }
                
for name, numbers in favourite_numbers.items():
        print("\nHello, my name is", name, "and my favourite numbers are:")
        for number in numbers:
            print ("\t",number)