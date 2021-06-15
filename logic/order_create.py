from payment import Blik, Card, Cash
from order import Order
from menu_item import MenuItem
import inquirer
import re

menu = [
    MenuItem('Pizza', 20),
    MenuItem('Burger', 12),
    MenuItem('Schabowy', 32),
    MenuItem('Spaghetti', 17),
    MenuItem('Sushi', 47),
    MenuItem('McChicken', 13)
]
payment_methods = {
    'card': Card,
    'blik': Blik,
    'cash': Cash
}

print('Todays menu:')
for i, m in enumerate(menu):
    print(i + 1, m.name, m.price)

order = Order()
while True:
    menu_add = input('Please enter the dish name number or enter E to end the order: ')
    regexp = re.compile('^[\d|E|e]{1}$')
    if regexp.match(menu_add):
        if menu_add.upper() != 'E':
            menu_item = menu[int(menu_add) - 1]
            order.add_item(menu_item)
            print('Added {} to your order. Current total: {} PLN'.format(menu_item.name, order.get_total()))
            continue
        else:
            break
    else:
        print('Didn\'t recognize the answer. Please try again.')

print('================== Your order =====================')
for item in order.items:
    print(item.name, item.price)
total = order.get_total()
print('Total: {} PLN'.format(total))

paymentMethods = [
    inquirer.List('payment',
                  message="How would you like to pay?",
                  choices=['cash', 'blik', 'card'],
                  ),
]
answers = inquirer.prompt(paymentMethods)
payment = payment_methods[answers['payment']]()
payment.pay(total)
