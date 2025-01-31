def my_split(main_string, string_to_split):
    result = main_string.split(string_to_split)
    print(result)

main_string = input("enter main string: ")
string_to_split = input("enter string to split: ")

my_split(main_string, string_to_split)
