def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m

def make_upper_case(s):
    return s.upper()


def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)


def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    

def abbrev_name(name):
    
    names = name.split()
    
    
    return f"{names[0][0].upper()}.{names[1][0].upper()}"