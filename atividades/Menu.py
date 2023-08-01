import os

print("MENU")
menu = int(input("-Nº Primo (1) \n-Nº decrescente (2) \n-Mediana de 3 Nº (3)\n"))

if menu == 1:
   a=int(input("insira um número: "))
   if a % 2 == 0:
       print(f"{a} não é primo")
   elif a / a and a / 1:
       print(f"{a} é primo")

if menu == 2:
    b = int(input("insira seu número: "))

    while b > 0:
        b -= 1
        print(f"{b}")

if menu == 3:
    c = int(input("insira o primeiro número: "))
    d = int(input("insira o segundo número: "))
    e = int(input("insira o terceiro número: "))
    if c > d and c > e:
        max1 = c
    elif d > e:
        print(f"A mediana é: {d}")
    else:
          

        if d > c and d > e:
            max1 = d
        elif c > e:
            print(f"A mediana é: {c}")
        else:
            if e > c and e > d:
                max1 = e
            elif c > d:
                print(f"A mediana é: {c}")
            else:
                print(f"A mediana é: {d}")

os.system("pause")

#########################################

def soma():
    x = int(input(""))
    y = int(input(""))
    z = x + y
    print(z)

soma()