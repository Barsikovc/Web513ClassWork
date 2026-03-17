from classes.ClassOrders import RestaurantOrder

if __name__ == '__main__':
    # Основная программа
    order1 = RestaurantOrder(1, "Салат Цезарь")
    order2 = RestaurantOrder(2, "Пицца Маргарита")
    order3 = RestaurantOrder(1, "Чай")

    # Проверяем доступность столов
    print(f"Стол 3 свободен? {'Да' if RestaurantOrder.is_table_available(3) else 'Нет'}")  # True
    print(f"Стол 1 свободен? {'Да' if RestaurantOrder.is_table_available(1) else 'Нет'}")  # False

    # Вывод общего количества заказов
    print(RestaurantOrder.get_total_orders())  # Вывод: Всего заказов: 3

    # Показываем заказы по столам
    RestaurantOrder.show_orders()
    print(RestaurantOrder.tables)
