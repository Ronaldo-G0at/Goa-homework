def manual_list(start, end, step, user_num):
    return [x + user_num for x in range(start, end, step)]

print(manual_list(1, 10, 2, 5))
print(manual_list(0, 20, 4, 3))
print(manual_list(10, 30, 5, 10))
