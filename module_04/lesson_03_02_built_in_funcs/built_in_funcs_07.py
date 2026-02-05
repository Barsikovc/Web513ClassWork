nums_list = [1, 2, 3, 4]
letters_list = ['a', 'b', 'c']

result = list(zip(nums_list, letters_list))
print(result)

for num, letter in zip(nums_list, letters_list):
    print(f'Число: {num}/Буква: {letter}')
