# Write your frequency_dictionary function here:
def frequency_dictionary(elements):
    item_sentence = "'" + "''".join([str(item) for item in elements]) + "'"
    print(item_sentence)
    return {item:item_sentence.count(f"'{str(item)}'") for item in elements}
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0, 2, 21]))
# should print {0:5}