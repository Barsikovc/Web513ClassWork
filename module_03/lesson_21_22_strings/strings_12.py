day = 13
print('Сегодня пятница, {:10d}'.format(day))
print('Сегодня пятница, {:<10d}'.format(day))
print('Сегодня пятница, {:*<10d}'.format(day))
print('Сегодня пятница, {:*^10d}'.format(day))
print('Сегодня пятница, {:*>10d}'.format(day))

day = 13
month = 10
hour = 15
print('Сегодня пятница: {1:10d}.{0:d} - {2:d} часов'.format(month, day, hour))

day = 'пятница'
month = 'июнь'
daytime = 'morning'

print("Сегодня пятница: {1:*>10}.{0}.{2:*<10}".format(month, day, daytime))
print("Сегодня пятница: {day:*>10}.{month}.{daytime:*<10}".format(month='июнь', day='пятница', daytime='утро'))

day_time = 13.00
pi_num = 3.14159265

print('Сегодня пятница, {0:*>10.2f}'.format(day_time))
print('Число pi, {0:*>10.4f}'.format(pi_num))
