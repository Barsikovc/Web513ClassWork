question_1 = 'My name __ Vova'
correct_1 = 'is'

print(question_1)
answer = input('Введите ваш ответ: ')
if answer == correct_1:
    print(f'Ответ верный')
else:
    print(f'Ответ неверный, верный ответ: {correct_1}')