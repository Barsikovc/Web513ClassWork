# print(f'Число 123 в восьмеричной системе счисления равно {0o123} в десятичной')
# print(f'Число 123ab в шестнадцатеричной системе счисления равно {0x123ab} в десятичной')
#
# name = 'Коля'
# day = 13
# print(f'{name:10} запустил свой стартап!')
# print(f'Сегодня пятница: {day:5}')
#
# print(f'{name:3} запустил свой стартап!')
# print(f'Сегодня пятница: {day:1}')
#
# print(f'{name:10s} запустил свой стартап!')
# print(f'Сегодня пятница: {day:5d}')
# print(f'Сегодня пятница: {day:5n}')
# print()
#
# day_time = 13
# pi_num = 3.14159265
# print(f'Сегодня пятница: {day_time:.2f}')
# print(f'Число pi: {pi_num:.4f}')
#
# total_answers = 15
# correct_answers = 8
# percent = correct_answers / total_answers
# print(percent)
# print(f'Процент верных ответов: {percent:.3%}')
# print()

name = "Коля"
day = 13
star_name = "Солнце"

print(f'{name:>10} запустил свой стартап')
print(f'Сегодня пятница, {day:<10}!')
print(f'{star_name:^10} центр солнечной системы.')

print(f'{name:$>10} запустил свой стартап')
print(f'Сегодня пятница, {day:#<10}!')
print(f'{star_name:*^10} центр солнечной системы.')