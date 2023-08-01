import os

x = int(input("informe um número: "))

y = x % 2

if y == 0:
    print("seu número é par")
else:
    print("seu número é ímpar")

os.system("pause")