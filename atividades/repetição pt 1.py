import os

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in num:
    print(n)

num[0] = 30

os.system("cls")

for n in num:
    print(n)

os.system("pause")