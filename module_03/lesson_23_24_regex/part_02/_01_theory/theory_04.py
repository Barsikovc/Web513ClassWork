import re

my_str = 'А1 +375(29)6234567; МТС +375(33)3334455'
pattern = re.compile(r'А1 \+\d{3}\((\d{2})\)(\d{7})')
match_obj = pattern.match(my_str)
# match_obj = re.match(pattern, my_str)
print(match_obj)
print(match_obj.group())
print(match_obj.group(1))
print(match_obj.group(2))
