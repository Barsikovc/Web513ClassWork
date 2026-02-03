from random import random, seed

for i in range(5):
    print(random())
print()

seed()
for i in range(5):
    print(random())
print()

seed(0)
for i in range(5):
    print(random())
print()
