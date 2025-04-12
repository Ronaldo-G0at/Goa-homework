def get_average(marks):
    return sum(marks) // len(marks)

def get_average(marks):
    raise NotImplementedError("TODO: get_average")
def get_average(marks):
    return int(sum(marks) / len(marks))
def hoop_count(n):
    if n < 10: return "Keep at it until you get it"
    return "Great, now move on to tricks"
def reverse_words(s):
    return " ".join(s.split(' ')[::-1])
def cockroach_speed(s):
    return int(s*27.777778)
def switch_it_up(number):
    res = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return res[number]
def square(n):
    return n*n
def twice_as_old(dad_years_old, son_years_old):
    res = (dad_years_old - 2 * son_years_old)
    
    if res < 0: return res*-1
    return res
def is_even(n): 
    return n % 2 == 0
def get_planet_name(id):
    """
    Returns the planet name based on the given ID (1-8).
    """
    planet_names = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    return planet_names.get(id, "Unknown")
def is_uppercase(inp):
    return inp == inp.upper()
def say_hello(name):
    return f"Hello, {name}"
def monkey_count(n):
    return list(range(1, n + 1))
def human_years_cat_years_dog_years(humanYears):
    if humanYears == 1:
        return [1, 15, 15]
    elif humanYears == 2:
        return [2, 24, 24]
    else:
        cat_years = 24 + (humanYears - 2) * 4
        dog_years = 24 + (humanYears - 2) * 5
        return [humanYears, cat_years, dog_years]