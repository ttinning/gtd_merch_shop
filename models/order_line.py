class OrderLine:
    def __init__(self, item, qty):
        self.item = item
        self.qty = qty
        self.price = item.price * qty