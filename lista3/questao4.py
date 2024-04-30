#%%

# Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

numero = int(input("Digite um número pra descobrir a tabuada: "))

print(f"Essa é a tabuada do {numero}: ")

for outronum in range(1, 11):
    tabuada = (numero * outronum)
    print(f"{numero} x {outronum} = {tabuada}")
    
# %%