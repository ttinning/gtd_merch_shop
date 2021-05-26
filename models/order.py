import random

class Order():

    def __init__(self, customer_name, order_date, quantity, merch_description):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.merch_description = merch_description
        self.order_number = "GTD" + str(random.randint(1000, 10000))