import os

x = int(input("informe um número: "))

y = x % 4
w = x % 100

if y == 0 and w > 0:
    print("o ano é bissexto")
else:
    print("o ano não é bissexto")

os.system("pause")