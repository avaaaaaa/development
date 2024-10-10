import math


def steps_for_binary_search(x):
    # x adet elemandan olusan sıralı bir dizide 
    # aranmak istenen itemin binary search
    # ile bulmak icin gerekli
    # maksimum adım sayısını verir
    if x <= 0:
        return
    return int(math.log(x, 2)) + 1


def binary_search(sorted_iterable, item):
    # searches 'item' in 'sorted_iterable' with binary search
    # returns None if not found
    # returns its index if found

    if len(sorted_iterable) <= 0:
        return
    
    start_index = 0
    stop_index = len(sorted_iterable) - 1

    while start_index <= stop_index:
        check_index = (start_index + stop_index) // 2
        check_item = sorted_iterable[check_index]
        
        if check_item == item:
            return check_index
        
        elif check_item < item:
            start_index = check_index + 1
        
        else:
            stop_index = check_index - 1
    
    return

x = 5
sorted_list = list(range(x))  # [0, 1, 2, 3, 4]
for item in sorted_list:
    print(item, binary_search(sorted_list, item))
print("step count: ", steps_for_binary_search(x))