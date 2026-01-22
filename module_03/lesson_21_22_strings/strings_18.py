from string import Formatter

formatter = Formatter()

print(formatter.format('{user_login}', user_login='Admin'))
print(formatter.format("{} {user_login}", "Welcome", user_login='Admin'))

print("{} {user_login}".format('Welcome', user_login='Admin'))