from datetime import datetime, timedelta

# 1. Получение текущей даты и времени
now = datetime.now()
print(now)
print()

# 2. Установка разницы во времени (макс недели)
delta = timedelta(weeks=1, days=5)
print(delta)
past_date = now - delta
print(past_date)
print()

# 3. Форматирование даты и времени
formatted_date = now.strftime('%d-%m-%Y %H:%M:%S')
print(formatted_date)
print()

# %Y — год (четырёхзначный);
# %m — месяц (двухзначный);
# %d — день (двухзначный);
# %H — час (24-часовой формат);
# %M — минуты;
# %S — секунды.

# 4. Получение даты из текста
some_text = "14>05>2026 20ч.35м.38с."
datetime_obj = datetime.strptime(some_text, "%d>%m>%Y %Hч.%Mм.%Sс.")
print(datetime_obj, type(datetime_obj))
print()

# 5. Вычисление разницы между датами
date1 = datetime(2025, 1, 1)
date2 = datetime(2026, 5, 14)
dates_delta = date2 - date1
print(dates_delta)
print(dates_delta.days)
