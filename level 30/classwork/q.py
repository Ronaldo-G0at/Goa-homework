def manual_find(main_string, str_to_find):

    index = main_string.find(str_to_find)

    if index != -1:
        return index
    else:
        return -1

main_string = "erm what the sigma"
str_to_find = "sigma"
print(manual_find(main_string, str_to_find))

str_to_find = "idek"
print(manual_find(main_string, str_to_find))