import os

y = 1
while y == 1:

    x = int(input("defina seu número "))

    while x > 0:
        x -= 1
        print(f"{x}")
    
print("Deseja sair?")
print("SIM - y")
print("NÃO - n")
y - input("")

y = y.upper()

if y == "Y":
    y = 0
else:
    y >= y

os.system("pause")