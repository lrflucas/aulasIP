#%%

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#   1. C = 5 * ((F-32) / 9).

temperatura = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = 5 * ((temperatura-32) / 9)

print(f"Temperatura em Fahrenheit é {temperatura}°F.\nTemperatura em Celsius é {celsius}°C.")

# %%