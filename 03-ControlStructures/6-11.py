current_price = 190.00
previous_price = 200.00
sale =100-((current_price/previous_price)*100)
if sale >= 10:
    print(f'Current product price: {current_price}')
    print(f'Previous product price: {previous_price}')
    print(f'Buy the product!!')
    print(f'Product price reduced by {sale}%')
else:
    print(f'Sale is only {sale}%. Not worth to buy')