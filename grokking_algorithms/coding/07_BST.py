from collections import deque


class BST_node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, root:BST_node=None) -> None:
        self.root = root
    
    def add_node(self, new_node:BST_node):
        if self.root is None:
            self.root = new_node
        else:
            # have to reach None value nodes (left or right)
            temp_node = self.root
            last_node = None  # the last visited node
            last_dir = 0
            while temp_node is not None:
                last_node = temp_node
                # save the last node before temp_node changes
                if new_node.value > temp_node.value:  # go right
                    temp_node = temp_node.right
                    last_dir = 0
                else:
                    temp_node = temp_node.left  # go left
                    last_dir = 1
            if last_dir == 1:  # new node is the left child of the last node
                last_node.left = new_node
            else:  # new node is the right child of the last node
                last_node.right = new_node


def traverse_dfs(root_node:BST_node):
    if root_node is None:
        return  # code reaches there, idk why it says code is unreachable
    print(root_node.value, end=" ")
    traverse_dfs(root_node.left)
    traverse_dfs(root_node.right)


def traverse_bfs(root_node:BST_node):
    que = deque([root_node])
    while que:
        get_node = que.popleft()
        if get_node is not None:
            que.append(get_node.left)
            que.append(get_node.right)
            print(get_node.value, end=" ")    


new_BST = BST()
list_values = [10, 5, 20, 2, 7, 25]
for value in list_values:
    node = BST_node(value)
    new_BST.add_node(node)

traverse_dfs(new_BST.root)
print()
traverse_bfs(new_BST.root)
