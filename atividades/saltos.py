import os

saltos = []
soma = 0
r = 0
l = 0

s = 1
while s == 1:
    print("\nMenu Inicial\n")
    print("[1] - Registro \n[2] - Sair")
    x = int(input("Selecione: "))

    os.system("cls")

    while r == 0:
        if x == 1:
            
            print("Registro")
            
            nome1 = input("Nome do Atleta: ")
            a = float(input("Primeiro salto: "))
            b = float(input("Segundo salto: "))
            c = float(input("Terceiro salto: "))
            d = float(input("Quarto salto: "))
            e = float(input("Quinto salto: "))

            soma = a + b + c + d + e
            media = soma / 5

            os.system("cls")

            print()
            print(f"a média dos saltos de ({nome1}) é: {media}")

            nome2 = input("Nome do segundo Atleta: ")
            f = float(input("Primeiro salto: "))
            g = float(input("Segundo salto: "))
            h = float(input("Terceiro salto: "))
            i = float(input("Quarto salto: "))
            j = float(input("Quinto salto: "))

            soma2 = f + g + h + i + j
            media2 = soma2 / 5

            os.system("cls")

            print()
            print(f"a média dos saltos de ({nome2}) é: {media2}")

            print("listar")
            print("[0] - sim ou [1] - não")
            l = int(input(""))

            if l == 0:
                print(f"A média de distância dos saltos do atleta ({nome1}) é {media}")
                print(f"A média de distância dos saltos do atleta ({nome2}) é {media2}")

            print("\n[1] - sair \n[0] - alterar")
            r = int(input(""))

            os.system("cls")

    if x == 2:
        s = 0