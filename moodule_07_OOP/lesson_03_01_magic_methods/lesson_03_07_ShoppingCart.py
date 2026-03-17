class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def remove_item(self, name):
        for item in self.items[:]:
            if name in item.values():
                self.items.remove(item)

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        if isinstance(other, Cart):
            new_cart = Cart()
            new_cart.items = self.items + other.items
            return new_cart
        raise TypeError('Объекты относятся к разным классам!')

    def __repr__(self):
        return f'Cart()'

    def __str__(self):
        if not self.items:
            return f'Корзина пуста:('
        result = 'Корзина:\n'
        for item in self.items:
            result += f'{item['name']}: {item['quantity']} шт. по {item['price']} руб.\n'
        return result


if __name__ == '__main__':
    cart1 = Cart()
    cart1.add_item('Яблоки', 50, 2)
    cart1.add_item('Молоко', 80, 1)

    cart2 = Cart()
    cart2.add_item("Хлеб", 40, 1)
    print(cart1)
    print(cart2)
    combined_cart = cart1 + cart2
    print(combined_cart)
    combined_cart.remove_item('Молоко')
    print(combined_cart)