import math
from datetime import datetime

NOW = datetime.now()


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    def __repr__(self):
        return self.address
    def available_menus(self, time):
        menu_list = [menu for menu in self.menus
                     if menu.start_time <= time <= menu.end_time]
        return menu_list


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    def __repr__(self):
        message = f"The menu '{self.name}' is "
        message += (f"available between {self.start_time.time()}"
                    f" and {self.end_time.time()}")
        return message
    def calculate_bill(self, purchased_items):
        # -inf indicates that one or many purchased items
        #  are not on the menu
        price = [self.items.get(purchased_item, -math.inf)
                 for purchased_item in purchased_items]
        return sum(price)
        


brunch = Menu(
    "brunch",
    {"pancakes": 7.50, "waffles": 9.00, "burger": 11.00,
     "home fries": 4.50, "coffee": 1.50, "espresso": 3.00,
     "tea": 1.00, "mimosa": 10.50, "orange juice": 3.50},
    datetime(NOW.year, NOW.month, NOW.day, 11),
    datetime(NOW.year, NOW.month, NOW.day, 16),
    )

early_bird = Menu(
    "early bird",
    {"salumeria plate": 8.00, "duck ragu": 17.50, "espresso": 3.00,
     "salad and breadsticks (serves 2, no refills)": 14.00,
     "pizza with quattro formaggi": 9.00, "coffee": 1.50,
     "mushroom ravioli (vegan)": 13.50},
    datetime(NOW.year, NOW.month, NOW.day, 15),
    datetime(NOW.year, NOW.month, NOW.day, 18),
)

dinner = Menu(
    "dinner",
    {"crostini with eggplant caponata": 13.00, "caesar salad": 16.00,
     "pizza with quattro formaggi": 11.00, "duck ragu": 19.50,
     "mushroom ravioli (vegan)": 13.50, "coffee": 2.00, "espresso": 3.00},
    datetime(NOW.year, NOW.month, NOW.day, 17),
    datetime(NOW.year, NOW.month, NOW.day, 23),
)

kids = Menu(
    "kids",
    {"chicken nuggets": 6.50, "fusilli with wild mushrooms": 12.00,
     "apple juice": 3.00},
    datetime(NOW.year, NOW.month, NOW.day, 11),
    datetime(NOW.year, NOW.month, NOW.day, 21),
)

arepas_menu = Menu(
    "arepas",
    {"arepa pabellon": 7.00, "pernil arepa": 8.50,
     "guayanes arepa": 8.00, "jamon arepa": 7.50},
    datetime(NOW.year, NOW.month, NOW.day, 10),
    datetime(NOW.year, NOW.month, NOW.day, 20),
)


print(brunch)
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird.calculate_bill(["salumera plate", "mushroom ravioli (vegan)"]))
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))


flagship_store = Franchise("1232 West End Road",
                           [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street",
                           [brunch, early_bird, dinner, kids])

arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])


test_date = datetime(NOW.year, NOW.month, NOW.day, 12)
print(flagship_store.available_menus(test_date))

test_date = datetime(NOW.year, NOW.month, NOW.day, 17)
print(flagship_store.available_menus(test_date))


my_first_business = Business("Basta Fazoolin' with my Heart",
                       [flagship_store, new_installment])

my_second_business = Business("Take a' Arepa", [arepas_place])
