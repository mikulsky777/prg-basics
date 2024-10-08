price = input('Enter price: ')
price = float(price)
discount = input('Enter discount %: ')
discount = float(discount)

discount_price = (100 - discount)/100 * price
reduction = price - discount_price

print(f'Price with discount: {round(discount_price, 2)}')
print(f'Reduction: {round(reduction, 2)}')
