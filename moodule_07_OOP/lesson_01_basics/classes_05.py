class Cart:

    def __init__(self, goods_prices):
        self.goods_prices = goods_prices
        self.total_prices = self.calculate_total_price()

    def calculate_total_price(self):
        return sum(self.goods_prices)


if __name__ == '__main__':
    cart1 = Cart([1000, 2000, 3000])
    print(cart1.total_prices)
