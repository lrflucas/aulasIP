#%%

# Faça um programa que mostre as tabuadas dos números de 1 a 10.

for numero in range(1, 11):
  print(f"Essa é a tabuada do {numero}: ")

  for outronum in range(1, 11):
    tabuada = (numero * outronum)
    print(f"{numero} x {outronum} = {tabuada}")

# %%