def order():
    products = {}
    while True:
        product = input()
        if product == 'buy':
            break
        product = product.split(' ')
        product_name = product[0]
        product_price = float(product[1])
        product_quantity = int(product[2])
        if product_name not in products:
            products[product_name] = [product_price, product_quantity]
        else:
            products[product_name] = [product_price, (product_quantity + products[product_name][1])]
    print_order(products)


def print_order(products):
    for product, values in products.items():
        total_price = values[0] * values[1]
        print(f'{product} -> {total_price:.2f}')


order()
