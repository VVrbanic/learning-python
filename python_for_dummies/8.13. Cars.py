def make_car(models, manifactures, **car_info):
    car = {}
    car["model"] = models
    car["manifacture"] = manifactures
    for key, value in car_info.items():
        car[key] = value
    return car
        

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)