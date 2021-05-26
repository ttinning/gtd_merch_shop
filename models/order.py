import random

class Order():

    def __init__(self, customer_name, order_date, basket):
        self.customer_name = customer_name
        self.order_date = order_date
        # self.quantity = quantity
        # self.merch_description = merch_description
        self.order_number = "GTD" + str(random.randint(1000, 10000))
        self.basket = basket
        self.basket_total = 0

        for item in basket:
            self.basket_total += item.price

        self.basket_total = round(self.basket_total, 2)