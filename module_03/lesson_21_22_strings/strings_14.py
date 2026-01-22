from datetime import datetime

day = 13
month = 'июнь'
hour = 15

print("Сегодня пятница, %d.%s.%d" % (day, month, hour))

day = 'пятница'
month = 'июнь'
hour = 'утро'

print("Сегодня пятница, %s.%s.%s" % (day, month, hour))

date1 = datetime(year=2025, month=7, day=27, hour=15, minute=20, second=30)
print(date1)
print(type(date1))

formatted_date = date1.strftime('%d.%m.%Y время: %H:%M:%S')
print(formatted_date)
