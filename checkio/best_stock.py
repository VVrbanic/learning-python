def best_stock(a):
    best = 0
    stock = ""
    for x, y in a.items():
        if y > best:
            stock = x
    return stock