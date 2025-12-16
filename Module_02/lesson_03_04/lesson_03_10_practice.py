evaluation_map = {
    '*': 'Ужасно',
    '**': 'Очень плохо',
    '***': 'Средненько',
    '****': 'Все в порядке',
    '*****': 'Прекрасная поездка',
}

stars = input()
print(evaluation_map.get(stars, 'Ошибка ввода!'))
if stars in evaluation_map.keys():
    print(evaluation_map[stars])
else:
    print('Ошибка ввода!')
