DAYS = {
    "Monday": "Monday",
    "Tuesday": "Tuesday",
    "Wednesday": "Wednesday",
    "Thursday": "Thursday",
    "Friday": "Friday",
    "Saturday": "Saturday",
    "Sunday": "Sunday",
}


def add_gamer(gamer, gamers_list):
    if "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)

def freq_day(gamers):
    freq = {k:0 for k in DAYS}
    for gamer in gamers:
        days_available = gamer["availability"]
        for day in days_available:
            freq[day] += 1
    return freq

def available_gamers(gamers, check_day):
    return [gamer["name"] for gamer in gamers if check_day in gamer["availability"]]


gamers = []

kimberly = {
    "name": "Kimberly Warner",
    "availability": [DAYS["Monday"], DAYS["Tuesday"], DAYS["Friday"]]
}

add_gamer(kimberly, gamers)
add_gamer({
    'name':'Thomas Nelson',
    'availability': [DAYS["Tuesday"], DAYS["Thursday"], DAYS["Saturday"]]},
    gamers)
add_gamer({
    'name':'Joyce Sellers',
    'availability': [DAYS["Monday"], DAYS["Wednesday"], DAYS["Friday"], DAYS["Saturday"]]},
    gamers)
add_gamer({
    'name':'Michelle Reyes',
    'availability': [DAYS["Wednesday"], DAYS["Thursday"], DAYS["Sunday"]]},
    gamers)
add_gamer({
    'name':'Stephen Adams',
    'availability': [DAYS["Thursday"], DAYS["Saturday"]]},
    gamers)
add_gamer({
    'name': 'Joanne Lynn',
    'availability': [DAYS["Monday"], DAYS["Thursday"]]},
    gamers)
add_gamer({
    'name':'Latasha Bryan',
    'availability': [DAYS["Monday"], DAYS["Sunday"]]},
    gamers)
add_gamer({
    'name':'Crystal Brewer',
    'availability': [DAYS["Thursday"], DAYS["Friday"], DAYS["Saturday"]]},
    gamers)
add_gamer({
    'name':'James Barnes Jr.',
    'availability': [DAYS["Tuesday"], DAYS["Wednesday"], DAYS["Thursday"], DAYS["Sunday"]]},
    gamers)
add_gamer({
    'name':'Michel Trujillo',
    'availability': [DAYS["Monday"], DAYS["Tuesday"], DAYS["Wednesday"]]},
    gamers)

list_of_freq = list(freq_day(gamers).items())
print(list_of_freq)

list_of_freq.sort(key=lambda x: x[1])
print(list_of_freq)

print("Count Of attending People (Descending order)")
for item in list_of_freq[::-1]:
    print(f"{item[0]}: {item[1]}", available_gamers(gamers, item[0]))

best_night = list_of_freq[-1]
print(best_night)