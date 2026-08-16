# dict for toppings and their cost($)
toppings_cost = {
    "pepperoni":2,
    "pineapple":6,
    "cheese":1,
    "sausage":3,
    "olives":2,
    "anchovies":7,
    "mushrooms":2,
}

num_two_dollar_slices = list(toppings_cost.values()).count(2)
#print(num_two_dollar_slices)

num_pizzas = len(toppings_cost)
#print(num_pizzas)

print(f"We sell {num_pizzas} different kinds of pizza!")

pizza_list = [[v, k] for k, v in toppings_cost.items()]
#print(pizza_list)

pizza_list.sort()
cheapest_pizza = pizza_list[0]
#print(cheapest_pizza)

priciest_pizza = pizza_list[-1]
#print(priciest_pizza)

# ran out of "anchovies"
pizza_list.pop()

# new topping is added
# thus, pizza_list needs to be sorted again
toppings_cost["peppers"] = 2.5
pizza_list.append([2.5, "peppers"])
pizza_list.sort()

three_cheapest = pizza_list[:3]
print(three_cheapest)