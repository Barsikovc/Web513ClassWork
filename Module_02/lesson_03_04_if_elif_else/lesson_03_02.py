# # num1 = 1
# # num2 = 2
# # num3 = 3
# #
# # print(num2 > num1 and num3 > num2)
# # print(num3 > num2 > num1)
# # print(num1 < num2 < num3)
# # print(num3 < num3 < num3)
#
# competent = True
# responsible = True
# careful = True
# print(competent and responsible and careful)
# print()
#
# competent = True
# responsible = False
# careful = True
# print(competent and responsible and careful)
# print()
#
# competent = True
# responsible = False
# careful = False
# print(competent or responsible or careful)
# #        1       +     0        +     0  == 1
# print()
#
# competent = False
# responsible = False
# careful = False
# print(competent or responsible or careful)
# print()
#
# competent = True
# responsible = True
# careful = False
#
# print(competent or responsible and careful)
# print()
#
# previously_fired = True
# print(not previously_fired)
# print()
#
#
# previously_fired = False
# print(not previously_fired)
# print()
#
# previously_fired = False
# competent = False
# responsible = True
# careful = True
# print(competent or responsible and careful and not previously_fired)
# #       False                  True                     True
# #        0      +                            1


time = int(input("Введите время в часах: ")) % 24

large_luggage = False
ticket = False
money = True

print(money or ticket and not large_luggage and time > 6)  # ошибка логики
print((money or ticket) and not large_luggage and time > 6)
