from datetime import datetime as dt
from decimal import Decimal
from custom_module import generate_time_travel_message as msg
import random

now = dt.now()
print("Date:", now.date())
print("Time:", now.time())

target_date = dt(
    random.randint(now.year, now.year + 1000),
    random.randint(1, 12),
    random.randint(1, 7)
)
print(target_date)

base_cost = 1000
cost_multiplier = 2.71
final_cost = (target_date.year - now.year) * cost_multiplier + base_cost
final_cost = Decimal(final_cost).quantize(Decimal("1.00"))
print(final_cost)

destinations = [
    "planetA", "planetB",
    "planetC", "planetD",
    "planetE", "planetF",
]
destination = random.choice(destinations)
print(msg(target_date.year, destination, final_cost))
