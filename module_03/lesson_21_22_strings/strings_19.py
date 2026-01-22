from string import Template

# my_template = Template("$user_login имеет права: $user_access, в приложении $app_name")
#
# my_string1 = my_template.substitute(user_login="Admin",
#                                     user_access='superuser',
#                                     app_name='E-Shop')
# my_string2 = my_template.substitute(user_login="User1787",
#                                     user_access='guest',
#                                     app_name='E-Shop')
# print(my_string1)
# print(my_string2)

my_template = Template("$user_login имеет права: $user_access, в приложении $app_name")
users_list = [["Admin", 'superuser', 'E-Shop'],
              ["User1787", 'guest', 'E-Shop'],
              ["Moderator", 'is_staff', 'E-Shop']]
users_list_formed = []

for login, access, app in users_list:
    user_info = my_template.substitute(user_login=login,
                                       user_access=access,
                                       app_name=app)
    users_list_formed.append(user_info)

for user in users_list_formed:
    print(user)
