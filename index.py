import pandas as pd
import numpy as np

visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
visits_cart = pd.merge(visits, cart, how='left')
visits_cart_length = len(visits_cart)
null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])

added_into_cart_percentage = (float(null_cart_times) * 100) / float(visits_cart_length)

cart_checkout = pd.merge(cart, checkout, how='left')
null_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
no_checkout_percentage = (float(null_checkout) * 100) / float(len(cart_checkout))

all_data = visits \
    .merge(cart, how='left') \
    .merge(checkout, how='left') \
    .merge(purchase, how='left')

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

checkout_purchase = pd.merge(checkout, purchase, how='left')
null_purchase = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
null_purchase_percentage = (float(null_purchase) * 100) / float(len(checkout_purchase))

print(all_data.time_to_purchase.mean())

