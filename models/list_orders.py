from order import Order
from datetime import date

order_001 = Order("Harrison Booth", date.today(), 1, "Pine Grove T-Shirt - Medium")
order_002 = Order("Sandy McMillan", date.today(), 1, "ACDC Jumper - Medium")
order_003 = Order("Gaz Darnell", date.today(), 1, "Foo Fighters, Wasting Light - Vinyl")

orders = [order_001, order_002, order_003]