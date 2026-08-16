import json

my_variable = {
    "name": "gg",
    "age": 18
}

# python --> json

with open("data.json", "w") as f:
    json.dump(my_variable, f)


# json --> python

with open("data.json") as f:
    get_variable = json.load(f)
print(get_variable)