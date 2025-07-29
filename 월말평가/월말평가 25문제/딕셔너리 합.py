mart_item = [
        {'price': 1000,
        'quantity': 30},
        {'price': 100,
        'quantity': 200},
        {'price': 500,
        'quantity': 10}
 ] # 값

def calc_product_price(mart) :
    total = 0
    for item in mart:
        price = item.get('price')
        quantity = item.get('quantity')
        total += price * quantity
    return total

print(calc_product_price(mart_item))