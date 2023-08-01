import os

print("MENU")
menu = int(input("Nº Primo (1) Nº decrescente (2) Mediana de 3 Nº (3): "))

if menu == 1:
   a=int(input("Digite um numero: "))
   if a / a and a / 1:
       print(f"{a} é primo")
   else:
       if a / 2:
        print(f"{a} não é primo")

if menu == 2:
    b = int(input("defina seu número "))

    while b > 0:
        b -= 1
        print(f"{b}")

if menu == 3:
    c = int(input("insira o primeiro número: "))
    d = int(input("insira o segundo número: "))
    e = int(input("insira o terceiro número: "))
    if c > d and c > e:
        max1 = c
    if d > e:
        print(f"A mediana é: {d}")
    else:
        if d > c and d > e:
            max1 = d
        if c > e:
            print(f"A mediana é: {c}")
        else:
            if e > c and e > d:
                max1 = e
                if c > d:
                    print(f"A mediana é: {c}")
                else:
                    print(f"A mediana é: {d}")

os.system("pause")