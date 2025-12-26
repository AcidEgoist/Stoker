class Item:
    name: str
    amount: int
    sell_price: float
    buy_price: float
    revenue: float

    def __init__(self, name, amount=0, sell_price=None, buy_price=None):
        self.name = name
        self.amount = amount
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.revenue = 0

    def check_stock(self, treshold):
        if self.amount <= treshold:
            return False
        else:
            return True

    def buy_item(self, amount, buy_price):
        self.buy_price = ((self.buy_price * self.amount) + (buy_price * amount)) / (
            amount + self.amount
        )
        self.revenue -= amount * buy_price
        self.amount += amount

    def sell_item(self, amount):
        self.amount -= amount
        self.revenue += amount * self.sell_price
        return amount * self.sell_price

    def update_price(self, sell_price):
        self.sell_price = sell_price

    def get_revenue(self):
        return self.revenue


carrot = Item("carrot", 50, 40, 30)
potato = Item("potato", 100, 30, 15)

print("Carrot amount %i, avg. buy price: %f" % (carrot.amount, carrot.buy_price))
print("Potato amount %i, avg. buy price: %f" % (potato.amount, potato.buy_price))

if not carrot.check_stock(40):
    carrot.buy_item(100, 50)

if not potato.check_stock(200):
    potato.buy_item(100, 13)

print("Carrot amount %i, avg. buy price: %f" % (carrot.amount, carrot.buy_price))
print("Potato amount %i, avg. buy price: %f" % (potato.amount, potato.buy_price))
