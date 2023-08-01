import os

mi = 0
s = 0
r = 0
a = 0
l = 0
r1 = 0
a1 = 0
l1 = 0
saltos = []


while s == 0:

    while s == 0:

        while mi == 0:
            os.system("cls")
            print("Escolha uma opção")
            print("[1] Registro")
            print("[2] Sair")
            x = int(input(" "))

            
            if x == 1:
                r1 = 1
                mi = 1
            elif x == 2:
                s = 1
                mi = 1
            else:
                print("Opção invalida")
                os.system("pause")

    #Registro

        nome = 1

        if r1 == 1:
            r = 1
            r1 = 0

        if x == 1:
            nome = int(input("Insira o nome do atleta: "))

        if nome == 1:
            for i in range(5):
                pulos = float(input("Isira a distância do salto: "))
                saltos.append(pulos)

        media = saltos / 5

        for pulos in saltos:
            if media:
                print(media)

os.system("pause")