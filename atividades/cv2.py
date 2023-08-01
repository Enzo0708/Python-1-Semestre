import os

vel = float(input("velocidade: "))

if vel > 80:
    print("multado")
    mult = (vel - 80) * 7
    print(f"R${mult} de multa")

os.system("pause")