def append_lists(list1, list2):
    list1.extend(list2)
    return list1

# Example usage:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = append_lists(list1, list2)
print(result)
