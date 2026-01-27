import re

text = 'Мой телеграм — @username. Но лучше свяжитесь со мной по email: user@example или support@domain.org.ru, mail01@yandex.ru'

pattern = re.compile(r'[\w.-]+@[\w.-]+\.\w+')
matches = re.findall(pattern, text)
print(matches)

pattern = re.compile(r'[A-Za-z0-9._-]+@yandex\.ru')
matches = re.findall(pattern, text)
print(matches)
email_input = input('Введите вашу почту: ').strip()
value = bool(re.match(pattern, email_input))
print(value)
