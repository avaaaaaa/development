import random


counter = 0  # how many times recursion occured
max_height = 0  # maximum height of the call stack
temp_height = 0


def quicksort(item_list: list) -> list:
    # sorting from the smallest to the biggest

    global counter, max_height, temp_height
    counter += 1
    temp_height += 1

    if temp_height > max_height:
        max_height = temp_height

    if len(item_list) <= 1: # base case
        temp_height -= 1
        return item_list
    elif len(item_list) == 2:  # base case
        if item_list[0] > item_list[1]:
            item_list[0], item_list[1] = item_list[1], item_list[0]
        temp_height -= 1
        return item_list
    
    pivot = item_list[0]
    left = [item for item in item_list[1:] if item <= pivot]
    right = [item for item in item_list[1:] if item > pivot]
    # pivot ile ayni deger varsa left ya da right kisminin
    # yalnizca birisine alinmali
    # right icin de >= yapilirsa pivot sayısı bir fazla olur 

    left = quicksort(left)
    right = quicksort(right)

    left.append(pivot)
    left.extend(right)

    return left


def quicksort2(item_list: list) -> list:
    # sorting from the smallest to the biggest

    global counter, max_height, temp_height
    counter += 1
    temp_height += 1

    if temp_height > max_height:
        max_height = temp_height

    if len(item_list) <= 1: # base case
        temp_height -= 1
        return item_list
    elif len(item_list) == 2:  # base case
        if item_list[0] > item_list[1]:
            item_list[0], item_list[1] = item_list[1], item_list[0]
        temp_height -= 1
        return item_list
    
    middle_index = len(item_list) // 2
    pivot = item_list[middle_index]
    left = []
    right = []

    for item in (item_list[0:middle_index] + item_list[middle_index + 1:]):
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)
    
    # pivot ile ayni deger varsa left ya da right kisminin
    # yalnizca birisine alinmali
    # right icin de >= yapilirsa pivot sayısı bir fazla olur 

    left = quicksort2(left)
    right = quicksort2(right)

    left.append(pivot)
    left.extend(right)

    return left

list_size = 1000
list_range = 10
number_list = []
for i in range(list_size):
    number_list.append(random.randint(-1 * list_range, list_range))
    # unsorted randomized array

#number_list = list(range(300))  # sorted array with no duplication
#number_list = [1, 2, 3, 4, 5, 6]  # sorted array with no duplication
number_list = [1,1, 2,2, 3,3, 4,4, 5,5, 6,6]  # sorted array with duplications

sorted_list = quicksort(number_list)
#print(sorted_list)
print("count of recursive calls:", counter)
print("max height of the call stack:", max_height)

counter, max_height, temp_height = 0, 0, 0
sorted_list = quicksort2(number_list)
#print(sorted_list)
print("count of recursive calls:", counter)
print("max height of the call stack:", max_height)

print("original list:", number_list)
