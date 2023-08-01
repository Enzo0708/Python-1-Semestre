import os

p = int(input("Digite um número: "))
r = int(input("Digite a razão: "))
d = p + (11 - 1) * r
for c in range(p, d, r):
    print(f"{c}")

os.system("pause")

carro = int(
    input("Qual carro você deseja alugar? \n([1]economico, [2]sedan, [3]sv): "))
dia = int(input("Quantos dias você ficou com o carro?: "))
km = float(input("Quantos quilometros você rodou com o carro?: "))

if carro == 1:
    al1 = dia * 50
    al2 = km * 0.15
    alc = al1 + al2
    print(f"O valor total a ser pago no carro economico é R${alc}")

if carro == 2:
    al12 = dia * 100
    al22 = km * 0.15
    alc2 = al12 + al22
    print(f"O valor total a ser pago no carro economico é R${alc2}")

if carro == 3:
    al13 = dia * 150
    al23 = km * 0.15
    alc3 = al13 + al23
    print(f"O valor total a ser pago no carro economico é R${alc3}")

os.system("pause")