import os

s = 1
while s <= 1:

    nome1 = input("Informe seu nome Aluno 01")
    idade1 = input(f"Informe sua idade {nome1} ")

    nome2 = input("Informe seu nome Aluno 02")
    idade2 = input(f"Informe sua idade {nome2}")

    if idade1 > idade2:
        print(f"O aluno {nome1} tem {idade1} anos, e o aluno {nome2} tem {idade2} anos.{nome2} é mais velho")

    x = int(idade1) + int(idade2)
    print(f"a soma das idades do {nome1} e do {nome2} é igual a {x}")

y = 1
n = 0

if n == 0:
    s = 1

if y == 1:
    s = 0
    
while s <= 1:
    print("Deseja sair?")
    print("Sim - y")
    print("Não - n")
