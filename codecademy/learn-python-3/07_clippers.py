hairstyles = [
    "bouffant", "pixie","dreadlocks",
    "crew", "bowl", "bob",
    "mohawk", "flattop"
]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = sum(prices)
average_price = total_price / len(prices)
print(f"Average Haircut Price: {average_price}")

new_prices = [price - 5 for price in prices]
print(new_prices)

price_last_week = zip(prices, last_week)
revenue_list = [pair[0] * pair[1] for pair in price_last_week]
total_revenue = sum(revenue_list)
print(f"Total Revenue: {total_revenue}")

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

hairstyle_price = zip(hairstyles, new_prices)
cuts_under_30 = [
    [hairstyle, price] for hairstyle, price in hairstyle_price if price < 30]
print(cuts_under_30)