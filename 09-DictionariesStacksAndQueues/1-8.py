price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print(f'Before discount:')
total = 0
for key, value in price_list.items():
    print(f"{key}: {value}")
    total += value
print(f'Total before discount: {round(total, 2)}')


print(f'After discount:')
total = 0
for key, value in price_list.items():
    print(f'{key}: {round(value*0.9, 2)}')
    total += round(value*0.9, 2)
print(f'Total value after discount: {round(total, 2)}')