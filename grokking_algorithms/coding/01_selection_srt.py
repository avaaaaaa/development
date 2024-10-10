def find_next(number_list, mode):
    """returns the index of the first occurence of 
    the smallest or the biggest number in number_list
    based on mode
    """

    if len(number_list) == 0:
        return
    
    smallest = number_list[0]
    return_index = 0
    mode = 1 if mode == 0 else mode  # prevent mode to be zero
    
    for i in range(1, len(number_list)):
        check_number = number_list[i]
        if check_number*mode < smallest*mode:
            smallest = check_number
            return_index = i
    
    return return_index


def selection_sort(number_list:list, mode=1):
    """returns sorted number_list in a new list using selection sort\n
    default sorting is in increasing order\n
    to sort in decreasing order, pass -1 as integer to 'mode' parameter
    """

    if len(number_list) <= 1:
        return number_list[:]
    # "return number_list" would return the original reference
    
    sorted_list = []
    copy_list = number_list[:]
    # we want to keep the original list unchanged
    # thus we use a copy list

    while len(copy_list) != 0:
        index = find_next(copy_list, mode)
        number = copy_list[index]
        
        sorted_list.append(number)
        copy_list.pop(index)
    
    return sorted_list


test_list = [5, 3, 6, 2, 10, 0 ,-3]
print("original id:", id(test_list))

sorted_list = selection_sort(test_list, -1)
print("sorted id:", id(sorted_list))
print("original:", test_list)
print("sorted: ", sorted_list)