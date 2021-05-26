from models.order import Order
from models.customer import Customer
from datetime import date

customer_1 = Customer("Harrison Booth", "hbooth@gmail.com")
customer_2 = Customer("Sandy McMillan", "smac@gmail.com")
customer_3 = Customer("Gaz Darnell", "gazzaDee@gmail.com")


order_001 = Order(customer_1.customer_name, date.today(), 1, "Pine Grove T-Shirt - Medium")
order_002 = Order(customer_2.customer_name, date.today(), 1, "AC/DC Jumper - Medium")
order_003 = Order(customer_3.customer_name, date.today(), 1, "Foo Fighters, Wasting Light - Vinyl")

orders = [order_001, order_002, order_003]