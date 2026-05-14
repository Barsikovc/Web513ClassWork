from datetime import datetime, timedelta


# Разница в 5 дней
delta = timedelta(days=5, hours=3)
print(delta)

# Арифметика с датами
today = datetime.today()
future_date = today + delta
print(future_date)