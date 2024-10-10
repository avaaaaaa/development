import math
from combinations import find_all_combs


class State:
    def __init__(self, name) -> None:
        self.name = name


class Radio:
    def __init__(self, name, states_covered:set, price) -> None:
        self.name = name
        self.states_covered = states_covered
        self.price = price
    
    def __lt__(self, radio):
        return self.price < radio.price

    def __str__(self) -> str:
        return self.name
    
    def add_state(self, state:State):
        self.states_covered.add(state)
    
    def remove_state(self, state:State):
            self.states_covered.discard(state)


def exact_solution(radios:list, states_must_covered:set):
    all_radio_combs = find_all_combs(radios)
    lowest_price = math.inf
    lowest_comb = None

    current_state_set = set()
    current_price = 0
    
    for i in range(len(all_radio_combs)):
        for j in range(len(all_radio_combs[i])):
            current_price = 0
            current_state_set.clear()

            for single_radio in all_radio_combs[i][j]:
                current_state_set.update(single_radio.states_covered)
                current_price += single_radio.price
            
            if (current_state_set.issuperset(states_must_covered)
                and current_price < lowest_price):
                lowest_price = current_price
                lowest_comb = all_radio_combs[i][j]

    return (lowest_comb, lowest_price)


def greedy_approach(radios:list, states_must_covered:set):
    # local optimal is the lowest price per uncovered state
    # at every step, we should find the local optimal
    # similar to selection sort:
    #   finding smallest or highest element at a time
    #   until no element is left in the list
    # but what if there is more than one local optimal?
    # in this case, every local optimal must be tested
    lowest_price = math.inf
    lowest_comb = []
    set_covered = set()
    current_price = 0

    while states_must_covered.difference(set_covered):
        local_optimal = None
        lowest_price = math.inf

        for radio in radios:
            number_of_uncovered = len(radio.states_covered.difference(set_covered))
            if number_of_uncovered == 0:
                continue
            
            lowest_per_uncovered = radio.price / number_of_uncovered
            
            if lowest_per_uncovered < lowest_price:
                local_optimal = radio
                lowest_price = lowest_per_uncovered

            elif lowest_per_uncovered == lowest_price:
                pass
        
        lowest_comb.append(local_optimal)
        set_covered.update(local_optimal.states_covered)
        current_price += local_optimal.price
    
    return (lowest_comb, current_price)


states = [
    State("mt"), State("id"), # 0, 1
    State("or"), State("ca"), # 2, 3
    State("nv"), State("az"), # 4, 5
    State("ut"), State("wa")  # 6, 7
    ]

radio_list = [
    Radio("r_one",set([states[1], states[4], states[6]]), 3),
    Radio("r_two",set([states[0], states[1], states[7]]), 4),
    Radio("r_three",set([states[2], states[3], states[4]]), 3),
    Radio("r_four",set([states[4], states[6]]), 3),
    Radio("r_five",set([states[3], states[5]]), 2),
    Radio("r_six", set([states[0], states[1], states[2], states[3],
                       states[4], states[5], states[6]]), 7)
    ]

radios, cost = exact_solution(radio_list, set(states))
print("**exact**")
print("comb:" , *radios, "\ncost: ", cost)

radios, cost = greedy_approach(radio_list, set(states))
print("**greedy**")
print("comb:" , *radios, "\ncost: ", cost)

print("**ascending price order**")
for radio in sorted(radio_list):
    print(radio.name, radio.price)
