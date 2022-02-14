def safe_pawns(pawns: set) -> int:
    pawns=list(pawns)
    counter=0
    
    #postupak rada matrice 
    alfa=["a","b","c","d","e","f","g","h"]
    broj=["8","7","6","5","4","3","2","1"]
    rows =8
    columns= 8
    mylist = [[0 for x in range(columns)] for x in range(rows)]
    for i in range(rows):
        for j in range(columns):
            mylist[i][j]=alfa[j]+broj[i]
    
    #provjera sigurnosti
    for k in range(0, len(pawns)):
        for i in range(rows-1):
            for j in range(columns):
                if pawns[k]==mylist[i][j]:      
                        if j==0:
                           if mylist[i+1][j+1] in pawns:
                            counter=counter + 1
                        elif j==7:
                           if mylist[i+1][j-1] in pawns:
                            counter=counter + 1
                        elif mylist[i+1][j+1] in pawns:
                            counter=counter + 1
                        elif mylist[i+1][j-1] in pawns:
                            counter=counter + 1 
    return(counter)
                        
        
        