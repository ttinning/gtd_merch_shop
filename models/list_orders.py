from models.order import Order
from models.customer import Customer
from models.product import Product
<<<<<<< HEAD

=======
from models.order_line import OrderLine
>>>>>>> 9e9bc177834b1be5e8ef9dcc2adb2347bcc187cb
from datetime import date

customer_1 = Customer("Harrison Booth", "hbooth@gmail.com")
customer_2 = Customer("Sandy McMillan", "smac@gmail.com")
customer_3 = Customer("Gaz Darnell", "gazzaDee@gmail.com")

product_1 = Product("Pine Grove T-Shirt - Medium", 21.99)
product_2 = Product("AC/DC Jumper - Medium", 34.99)
product_3 = Product("Foo Fighters, Wasting Light - Vinyl", 17.99)
product_4 = Product("DJ Shadow, Endtroducing - Digital Download", 6.99)

order1_line1 = OrderLine(product_1, 3)
order1_line2 = OrderLine(product_3, 2)

<<<<<<< HEAD

order_001 = Order(customer_1.customer_name, date.today(), 1, product_1.description)
order_002 = Order(customer_2.customer_name, date.today(), 1, product_2.description)
order_003 = Order(customer_3.customer_name, date.today(), 1, product_3.description)
=======
order2_line1 = OrderLine(product_1, 1)
order2_line2 = OrderLine(product_2, 5)

order3_line1 = OrderLine(product_1, 2)
order3_line2 = OrderLine(product_3, 3)
order3_line3 = OrderLine(product_2, 4)
order3_line4 = OrderLine(product_4, 1)

basket_1 = [order1_line1, order1_line2]
basket_2 = [order2_line1, order2_line2]
basket_3 = [order3_line1, order3_line2, order3_line3, order3_line4]


order_001 = Order(customer_1.customer_name, date.today(), basket_1)
order_002 = Order(customer_2.customer_name, date.today(), basket_2)
order_003 = Order(customer_3.customer_name, date.today(), basket_3)
>>>>>>> 9e9bc177834b1be5e8ef9dcc2adb2347bcc187cb

orders = [order_001, order_002, order_003]