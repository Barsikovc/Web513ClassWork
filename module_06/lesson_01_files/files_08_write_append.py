def write_user_answers(filename, answers):
    with open(filename, 'wt', encoding='utf-8') as file:
        for answer in answers:
            file.write(f'{answer}\n')
    print(f'Ответы записаны!')

"""
Для работы с уже подготовленными данными
"""

def write_user_answers_wl(filename, answers):
    with open(filename, 'wt', encoding='utf-8') as file:
        file.writelines(answers)
    print(f'Ответы записаны!')


if __name__ == '__main__':
    user_name = input('Как вас зовут: ')
    user_language = input('Какой язык вы изучаете: ')
    user_time = input('Как долго: ')
    user_institution = input('Где: ')
    user_answers = [user_name, user_language, user_time, user_institution]
    user_filename = fr'data_files\{user_name}_data.txt'
    write_user_answers(user_filename, user_answers)
    print()

    user_filename_normalized = fr'data_files\{user_name}_data_wl.txt'
    user_answers_normalized = []
    for answer in user_answers:
        user_answers_normalized.append(answer + '\n')
    write_user_answers_wl(user_filename_normalized, user_answers_normalized)

