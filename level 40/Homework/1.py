def count_sheeps(sheep):
    return sheep.count(True)

def no_space(x):
    return x.replace(" ","")

def double_integer(i):
    return i*2

def boolean_to_string(b):
    return str(b)
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2

def century(year): 
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
    


def digitize(n):
    starting_str = str(n)
    reversed_str = starting_str[::-1]
    
    res_list = []
    
    for i in reversed_str:
        res_list.append(int(i))
    
    return res_list