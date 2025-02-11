def remove_elements_by_indexes(main_list, indexes_list):
    for index in sorted(indexes_list, reverse=True):
        if 0 <= index < len(main_list):
            del main_list[index]
    return main_list

