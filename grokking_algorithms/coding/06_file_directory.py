import os
from os import listdir
from os.path import join, isfile
from collections import deque


def print_directory_bfs(start_dir="."):
    que = deque([start_dir])
    # que = deque(start_dir) would be incorrect. why?
    while que:
        get_path = que.popleft()
        
        split_str = get_path.split(os.sep)
        space = ["  " for item in split_str]
        space = "".join(space)

        print(get_path, sep="")
        # printing the directory

        for element in listdir(get_path):
            element_path = join(get_path, element)
            if isfile(element_path):
                print(space, element, sep="")
                # printing the file
            else:    
                que.append(element_path)


def print_directory_dfs(start_dir="."):
    print(start_dir)
    
    def _print_directory(start_dir, space):
        for item in listdir(start_dir):
            item_path = join(start_dir, item)
            # item has only the file or the directory name.
            # to get the actual path, it's needed to join
            # item name with 'start_dir'.
            if isfile(item_path):
                print(space, item, sep="")
            else:
                print(space, os.sep, item, sep="")
                _print_directory(item_path, space + " ")
                # if item is not a file, then it's the new 'start_dir'
    
    _print_directory(start_dir, "  ")


#dir = join(".", "pics", "2001")
dir = join(".", "pics")
dir = join(".", "sub_folder3")
dir = "."
print_directory_bfs(dir)
print_directory_dfs(dir)