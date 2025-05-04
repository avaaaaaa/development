def ground_shipping(package_weight):
    total = 0
    flat_charge = 20
    if package_weight <= 2:
        total += package_weight * 1.5
    elif 2 < package_weight <= 6:
        total += package_weight * 3
    elif 6 < package_weight <= 10:
        total += package_weight * 4
    else:
        total += package_weight * 4.75
    return total + flat_charge

def ground_shipping_premium():
    flat_charge = 125
    return flat_charge

def drone_shipping(package_weight):
    total = 0
    if package_weight <= 2:
        total += package_weight * 4.5
    elif 2 < package_weight <= 6:
        total += package_weight * 9
    elif 6 < package_weight <= 10:
        total += package_weight * 12
    else:
        total += package_weight * 14.25
    return total

# each item of the result list has two values: lb and shopping way
# to sort the result list according to lb, we need a key function
# the function takes a single argument and returns a key to use for sorting purposes
#   list items will be sorted based on their return values
def _key_function(_list):
    return _list[0]
    

exit_loop = False
package_weight = 0

# ask for the package weight until correct value is given
while not exit_loop:
    package_weight = input("enter the package weight(lb): ")
    try:
        package_weight = float(package_weight)
        if package_weight <= 0:
            raise ValueError
        exit_loop = True
    except ValueError:
        print("Incorrect value, try again")

shipping_prices = [
    [ground_shipping(package_weight), "ground shipping"],
    [ground_shipping_premium(), "ground shipping premium"],
    [drone_shipping(package_weight), "drone shipping"]
]

# sort the prices in ascending order
# The value of the key parameter should be a function (or other callable) 
shipping_prices.sort(key=_key_function)

print(f"The cheapest price: {shipping_prices[0][0]} by '{shipping_prices[0][1]}'")
print("Other prices:")
for i in range(1, len(shipping_prices)):
    print(f"  The price: {shipping_prices[i][0]} by '{shipping_prices[i][1]}'")