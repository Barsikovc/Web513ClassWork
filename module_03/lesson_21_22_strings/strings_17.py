import string

my_string = '   Мы рады\n встречать\n\n старых друзей.   '
print(my_string)
print()
print(string.capwords(my_string))

new_string = string.capwords(my_string)
print(string.capwords(new_string, sep="а"))
