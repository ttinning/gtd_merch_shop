from models.order import Order
from models.customer import Customer
from models.product import Product
from datetime import date

customer_1 = Customer("Harrison Booth", "hbooth@gmail.com")
customer_2 = Customer("Sandy McMillan", "smac@gmail.com")
customer_3 = Customer("Gaz Darnell", "gazzaDee@gmail.com")

product_1 = Product("Pine Grove T-Shirt - Medium")
product_2 = Product("AC/DC Jumper - Medium")
product_3 = Product("Foo Fighters, Wasting Light - Vinyl")


order_001 = Order(customer_1.customer_name, date.today(), 1, product_1.description)
order_002 = Order(customer_2.customer_name, date.today(), 1, product_2.description)
order_003 = Order(customer_3.customer_name, date.today(), 1, product_3.description)

orders = [order_001, order_002, order_003]