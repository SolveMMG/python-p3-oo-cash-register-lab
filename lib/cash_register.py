class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.reset()

    def reset(self):
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity
        self.total += self.last_transaction

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total = round(self.total - discount_amount)
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
