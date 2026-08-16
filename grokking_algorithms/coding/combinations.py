def find_comb(list_of_things, n, sort_the_list=1) -> list:
    if n <= 0 or n > len(list_of_things):
        return []
    
    sorted_list = sorted(list_of_things) if sort_the_list else list_of_things
    
    # when the list is sorted, it would be 
    # easier to detect duplication
    # for example, checking combinations of two
    # [1, 2, 1] -> [1, 2], [1, 1], [2, 1]
    # [1, 2] and [2, 1] is the same thing in terms of combination
    # if the list is ordered
    # [1, 1, 2] -> [1, 1], [1, 2], [1, 2]
    # it is easier to see that [1, 2] is duplicated
    
    # but for some cases like the longest common subsequence
    # the original character positions must stay the same
    # to find the correct answer 
    # so, sort_the_list paramater can be set 0 for that

    combs = {}
    break_loop = False
    indexes = [i for i in range(n)]
    # indexes for 'n' combination: 0, 1, 2, ..., n-2, n-1

    while not break_loop:
        comb = []
        for index in indexes:
            comb.append(sorted_list[index])

        # dictionary will not allow key duplications
        combs[tuple(comb)] = 1

        # update the indexes for the next combination
        update = []  # indexes that reached their limit
        for i in range(len(indexes))[::-1]:
            if indexes[i] + (n - i) < len(list_of_things):
                indexes[i] += 1
                break
            else:
                update.append(i)
        
        for i in update[::-1]:  # if '0' is in update, then terminate
            if i == 0:
                break_loop = True
                break
            indexes[i] = indexes[i-1] + 1
    
    return list(combs.keys())


def find_all_combs(list_of_things) -> list:
    combs = []
    for i in range(1, len(list_of_things) + 1):
        combs.append(find_comb(list_of_things, i))
        # combs[0]
        #   list of combinations where n = 1
        # combs[1]
        #   list of combinations where n = 2
        # combs[1][3]
        #   list of the elements of the fourth combination where n = 2
        # combs[1][3][0]
        #   the first element of the fourth combination where n = 2 
        
    return combs


"""
x = [1, 2, 3, 4, 5]
all_combs = find_all_combs(x)
print(all_combs, len(all_combs))
print(all_combs[0], len(all_combs[0]))
print(all_combs[1], len(all_combs[1]))
print(all_combs[1][0], len(all_combs[1][0]))
print(all_combs[1][0][1])
"""