class RestaurantOrder:
    total_orders = 0
    tables = {}

    def __init__(self, table_number, order_details):
        self.table_number = table_number
        self.order_details = order_details
        RestaurantOrder.total_orders += 1
        # setdefault устанавливает ключом номер столика и задает значение по умолчанию [],
        # при этом сразу возвращая [] к которому мы тут же .append(order_details)
        RestaurantOrder.tables.setdefault(table_number, []).append(order_details)

    @staticmethod
    def is_table_available(table_number):
        return len(RestaurantOrder.tables.get(table_number, [])) == 0

    @classmethod
    def get_total_orders(cls):
        return f'Всего заказов: {cls.total_orders}'

    @classmethod
    def show_orders(cls):
        for table, orders in cls.tables.items():
            print(f'Стол {table}: {', '.join(orders)}')


