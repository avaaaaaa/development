from collections import deque
import math


class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.neighbors = {}
        # node.neighbors:
        #   dictionary for the distance between node and its neighbors

class DijkstraNode(Node):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.closest = None
        self.distance = math.inf
        self.is_visited = False
        # node.closest:
        #   the node that should be visited to reach this node
        #   for the shortest path between this node and starting node
        # node.distance:
        #   the shortest path between this node and starting node,
        #   thus, this value must be 0 for starting node
        # node.is_visited:
        #   shows if the node is visited before,
        #   default is False, because every node is unprocessed at first


class Graph:
    def __init__(self, nodes:list) -> None:
        self.nodes = nodes
    
    def add_node(self, node:Node):
        self.nodes.append(node)
    
    def delete_node(self, node:Node):
        self.nodes.remove(node)
    
    def make_connection(self, node1:Node, node2:Node, distance):
        node1.neighbors[node2] = distance
        node2.neighbors[node1] = distance
        # node1 <--> node2


class DirectedGraph(Graph):
    def make_connection(self, node1:Node, node2:Node, distance):  # override
        node1.neighbors[node2] = distance
        # node1 --> node2

# graph connections can be found at "dijkstra_graphs.txt"

# creating nodes
s = DijkstraNode("s")
a = DijkstraNode("a")
b = DijkstraNode("b")
c = DijkstraNode("c")
d = DijkstraNode("d")
f = DijkstraNode("f")

# creating graph5
graph5 = Graph([s, a, b, c, d, f])
graph5.make_connection(s, a, 14)
graph5.make_connection(s, b, 9)
graph5.make_connection(s, c, 7)
graph5.make_connection(a, f, 9)
graph5.make_connection(a, b, 2)
graph5.make_connection(b, d, 11)
graph5.make_connection(b, c, 10)
graph5.make_connection(c, d, 15)
graph5.make_connection(d, f, 6)


# determining start_node and target_node
start_node = s
start_node.distance = 0  # distance of start_node must be 0
target_node = f
que = deque([start_node])

# implementing the dijkstra algorithm
while que:
    next = que.popleft()
    #print(next.name)
    
    if next.is_visited or next == target_node:
        continue
        # if it is visited before and not updated,
        #   then it has to be ignored to prevent infinite loop
        # we also don't need to process target_node
        #   processing a node means where we can reach
        #   going through this node
        #   since we just want to reach to the target
        #   and not go further, target node is not processed
    
    for neighbor in next.neighbors:
        #print(neighbor.name)
        length = next.distance + next.neighbors[neighbor]
        # (the shortest path to start_node) + (distance to neighbor)
        # this will determine possible neighbor.distance
        # and the neighbors whose distance is bigger than
        # target_node.distance cannot be a part of shorter path
        # so, these neighbors will be ignored
        if length > target_node.distance:
            continue
        elif length < neighbor.distance:  # found shorter path
            neighbor.distance = length
            neighbor.closest = next

            # now, neighbor node has to be processed again
            # because it is updated
            neighbor.is_visited = False
            que.append(neighbor)

    next.is_visited = True


# printing out the shortest path between start_node and target_node
path = target_node
total = target_node.distance
while path is not None:
    print(path.name, end=" ")
    path = path.closest
print("path:", total)
