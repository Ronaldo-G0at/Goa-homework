def greet(name, owner):
    if name == owner:
        return "Hello boss"
    return "Hello guest"



def rental_car_cost(d):
    # your code
    cost = d * 40
    if d >= 7:
        cost  -= 50
    elif d >= 3 and d < 7:
        cost -=20
    return cost