from datetime import datetime, timedelta

# получение текущей даты и времени
now = datetime.now()
# задать свою дату и время
date1 = datetime(2025, 7, 27, 15, 20, 30)
date2 = datetime(year=2025, month=7, day=27, hour=15, minute=20, second=30)
# форматирование даты и времени
formatted_data1 = date1.strftime('%d.%m.%Y время: %H*%M*%S')
formatted_data2 = date2.strftime('%d.%m.%Y время: %H*%M*%S')

# задать временной промежуток
delta = timedelta(days=5, hours=12, minutes=30, seconds=45)
print(delta)

today = datetime.today()
print(today)

# вычисление будущей даты
future_date = today + delta
print(future_date)

# вычисление разницы между датами
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 8, 7)

delta = date2 - date1
print(delta)

# получение объекта даты из строк разного вида
str_date1 = '10.05.2025'
str_date2 = '26-June-2025'
str_date3 = '5 Jan, 11'

first_date = datetime.strptime(str_date1, '%d.%m.%Y')
second_date = datetime.strptime(str_date2, '%d-%B-%Y')
third_date = datetime.strptime(str_date3, '%d %b, %y')

print(first_date)
print(second_date)
print(third_date)

delta1 = second_date - first_date
print(delta1)
print(sorted([first_date, second_date, third_date]))