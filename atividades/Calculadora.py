import os

print("escolha a operação e digite seus números para que a conta seja realizada.")

num1 = float(input("escolha o primeiro número "))
num2 = float(input("escolha o segundo número "))
c = input("selecione a operação desejada soma(+) subtração(-) multiplicação(*) divisão(/): ")

if c == "+":
    r = (num1 + num2)

elif c == "-":
    r = (num1 - num2)

elif c == "*":
    r = (num1 * num2)

elif c == "/":
    r = (num1 / num2)

else:
    print("Operação inválida")
    r = None

if r is not None:
    print(f"O resultado é {r}")
    
os.system("pause")