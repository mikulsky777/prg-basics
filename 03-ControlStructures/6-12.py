products = 5
price = 40

if products > 2:
    total = 2*price + (0.75*((products-2)*price))
    print(f'Numbers of products purchased: {products}')
    print(f'Product price: {price}')
    print(f'Amount to pay: {total}')
elif products <= 2:
    total = price * products
    print(f'Numbers of products purchased: {products}')
    print(f'Product price: {price}')
    print(f'Amount to pay: {total}')