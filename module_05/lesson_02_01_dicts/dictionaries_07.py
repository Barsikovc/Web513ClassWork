def set_new_prices(fruits: dict[str, float], price_percent: int) -> dict[str, float]:
    for key, value in fruits.items():
        fruits[key] = round(value * (1 + price_percent / 100), 2)
    return fruits


if __name__ == '__main__':
    shop_fruits = {
        "яблоки": 100.59,
        "груши": 199.98,
        "персики": 400.05,
        "мандарины": 299.95,
        "апельсины": 349.50,
    }
    new_prices = set_new_prices(shop_fruits.copy(), 22)
    print(shop_fruits)
    print(new_prices)
