def checkio(*args):

    if len(args) == 0:
        a= None
    elif len(args) == 1:
        a= args[0]
    else:
     a= max(args)-min(args)
     
    return a