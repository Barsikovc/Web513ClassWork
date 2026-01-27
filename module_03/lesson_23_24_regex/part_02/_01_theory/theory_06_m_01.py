"""
Тип ошибки 1: Некорректное использование жадных квантификаторов

Возникает при некорректном использовании жадных квантификаторов,
в некотором случае они могут захватывать больше текста, чем нужно.
"""

import re

text = '<div>Первый</div><div>Второй</div>'
pattern = re.compile(r'<div>.*</div>')
matches = re.findall(pattern, text)
print(matches)  # ['<div>Первый</div><div>Второй</div>']

"""
Решение:
используем ленивый квантификатор, чтобы захватывать минимально возможное совпадение.
"""

text = '<div>Первый</div><div>Второй</div>'
pattern = re.compile(r'<div>.*?</div>')
matches = re.findall(pattern, text)
print(matches)