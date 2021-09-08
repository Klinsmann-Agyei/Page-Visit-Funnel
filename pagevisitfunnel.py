import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())
visits_cart = pd.merge(visits, cart, how ='left')
print(len(visits_cart))
print(len(visits_cart[visits_cart.cart_time.isnull()]))
print(float(len(visits_cart[visits_cart.cart_time.isnull()]))/len(visits_cart))

cart_checkout = pd.merge(cart, checkout, how ='left')
print(len(cart_checkout))
print(len(cart_checkout[cart_checkout.checkout_time.isnull()]))
print(float(len(cart_checkout[cart_checkout.checkout_time.isnull()]))/len(cart_checkout))

checkout_purchase = pd.merge(checkout, purchase, how ='left')
print(len(checkout_purchase))
print(len(checkout_purchase[checkout_purchase.purchase_time.isnull()]))
print(float(len(checkout_purchase[checkout_purchase.purchase_time.isnull()]))/len(checkout_purchase))

all_data = visits.merge(cart, how = 'left').merge(checkout, how = 'left').merge(purchase, how = 'left')
print(all_data.head())

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
