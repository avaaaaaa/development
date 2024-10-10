import random


def countdown(x:int):
    if x < 0:
        return
    elif x == 0:
        print(f"{x}")
        return    
    print(f"{x}..", end="")
    countdown(x-1)


def factorial(x:int):
    if x < 0:
        return
    elif x == 0:
        return 1
    return x * factorial(x-1)


def sum_up(number_list:list):
    list_size = len(number_list)
    if list_size == 0:
        return
    elif list_size == 1:
        return number_list[0]
    return number_list[0] + sum_up(number_list[1:])


def count_items(a_list:list):
    list_size = len(a_list)
    if list_size == 0:
        return 0
    elif list_size == 1:
        return 1
    return 1 + count_items(a_list[1:])


def find_max_min(number_list:list, mode=1):
    # max -> mode=-1
    # min -> mode=1
    list_size = len(number_list)
    if list_size == 0:
        return
    elif list_size == 1:
        return number_list[0]
    rest_of_max_min = find_max_min(number_list[1:], mode)
    
    if number_list[0]*mode < rest_of_max_min*mode:
        return number_list[0]
    else:
        return rest_of_max_min


def binary_search(sorted_number_list:list, find_number):
    def __func(sorted_number_list, start, end):
        if start > end:
            return

        index = (start + end) // 2
        check_number = sorted_number_list[index]
        
        if check_number == find_number:
            return index
        elif check_number < find_number:
            start = index + 1
        else:
            end = index - 1
        
        __func(sorted_number_list, start, end)
    

    return __func(sorted_number_list, 0, len(sorted_number_list) - 1)


def quicksort(number_list, mode=1):
    """sorts 'number_list' by using quicksort algorithm\n
    it sorts the list in ascending order by default (mode=1)\n
    to sort in descending order, pass -1 as number to 'mode' parameter
    """
    list_size = len(number_list)
    if list_size == 0:
        return []
    elif list_size == 1:
        return [number_list[0]]
    elif list_size == 2:
        n0 = number_list[0]
        n1 = number_list[1]
        if n0*mode > n1*mode:
            n0, n1 = n1, n0
        return [n0, n1]
    
    pivot = 0
    left, right = [], []

    for number in number_list[1:]:
        if number*mode <= number_list[pivot]*mode:
            left.append(number)
        else:
            right.append(number)

    left = quicksort(left, mode)
    right = quicksort(right, mode)

    return [*left, number_list[pivot], *right]


x = 10
countdown(x)
print(factorial(x))

numbers = list(range(x))
print(sum_up(numbers))
print(count_items(numbers))
print(find_max_min(numbers, -1))

find_number = -11
print(binary_search(numbers, find_number))

list_size = 10
list_range = 100
numbers = []
for i in range(list_size):
    numbers.append(random.randint(-1*list_range, list_range))
#numbers = [71, 91, -55, 53, 23, 79, 39, -82, 23, 50]

print("original\n", end="     ")
print(numbers)

print("ascending order\n", end="     ")
print(quicksort(numbers))

print("descending order\n", end="     ")
print(quicksort(numbers, -1))
