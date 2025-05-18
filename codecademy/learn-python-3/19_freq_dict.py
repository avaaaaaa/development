# Write your frequency_dictionary function here:
def frequency_dictionary(elements):
    set_of_elements = set(elements)
    return {element:elements.count(element) for element in set_of_elements}
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0, 2, 21]))
# should print {0:5, 2: 1, 21: 1}