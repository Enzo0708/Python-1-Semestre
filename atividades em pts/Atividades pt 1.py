import os

x = float(input("informe um número: "))
if x < 0:
    print("o número é negativo")
elif x == 0:
    print("seu número é 0")
else:
    print("seu número é positivo")

os.system("pause")