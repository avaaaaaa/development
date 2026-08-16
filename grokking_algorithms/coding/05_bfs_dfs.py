class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.friends = []
        self.is_mango_seller = False
    
    def add_friend(self, *new_friends):
        for friend in new_friends:
            self.friends.append(friend)
            friend.friends.append(self)
            # friendship is not directed connection
            # thus when A adding B as friend, B also should add A as friend 
    
    def print_friends(self):
        msg = f"friends of {self.name}: "
        for friend in self.friends[:len(self.friends)-1]:
            msg += friend.name + ", "
        msg += self.friends[-1].name
        print(msg)
    
    def set_mango_seller(self, is_seller: bool):
        self.is_mango_seller = is_seller
    
    def get_mango_seller(self):
        return self.is_mango_seller


def dfs_find_mango_seller(base_person: Person):
    # implements stack logic to traverse through network
    mango_sellers = []
    person_dict = {}
    # since friendship is not a directed connection, 
    # to prevent infinite recursion like processing
    # a node that is already processed, this dictionary
    # will be used to keep the track of processed nodes.
    
    def _find_mango_seller(base_person):
        person_dict[base_person] = 1
        # base node is now processed.
        for friend in base_person.friends:
            person_dict.setdefault(friend, 0)
            # 0 means this node is not processed yet
            if person_dict[friend] == 0:
                if friend.get_mango_seller() == True:
                    mango_sellers.append(friend)
                _find_mango_seller(friend)
            
    _find_mango_seller(base_person)
    
    return mango_sellers


def bfs_find_mango_seller(base_person: Person):
    # implements queue logic to traverse through network
    mango_sellers = []
    person_dict = {}
    search_queue = [base_person]
    # since friendship is not a directed connection, 
    # to prevent infinite recursion like processing
    # a node that is already processed, this dictionary
    # will be used to keep the track of processed nodes.

    def _find_mango_seller(base_person):
        person_dict[base_person] = 1
        # base node is now processed.
        for friend in base_person.friends:
            person_dict.setdefault(friend, 0)
            # 0 means this node is not processed yet
            if person_dict[friend] == 0:
                if friend.get_mango_seller() == True:
                    mango_sellers.append(friend)
                search_queue.append(friend)
          
    while len(search_queue) != 0:
        next_person = search_queue.pop(0)  # first in, first out
        _find_mango_seller(next_person)
    
    return mango_sellers


adit = Person("adit")
bob = Person("bob")
claire = Person("claire")
alice = Person("alice")
bobf1 = Person("bobf1")
clairef1 = Person("clairef1")
alicef1 = Person("alicef1")

adit.add_friend(bob, claire, alice)
bob.add_friend(bobf1)
claire.add_friend(clairef1)
alice.add_friend(alicef1)

"""
adit.print_friends()
bob.print_friends()
claire.print_friends()
alice.print_friends()
"""

bob.set_mango_seller(False)
claire.set_mango_seller(True)
alice.set_mango_seller(False)

bobf1.set_mango_seller(True)
clairef1.set_mango_seller(True)
alicef1.set_mango_seller(True)

mango_sellers = dfs_find_mango_seller(adit)
for person in mango_sellers:
    print(person.name, end=" ")
print()
mango_sellers = bfs_find_mango_seller(adit)
for person in mango_sellers:
    print(person.name, end=" ")
