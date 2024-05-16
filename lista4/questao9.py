#%%

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#   1. Para homens: (72.7*h) - 58
#   2. Para mulheres: (62.1*h) - 44.7

h = float(input("Digite a sua altura em metros: "))
formula_h = (72.7 * h) - 58
formula_m = (62.1 * h) - 44.7

print(f"Sua altura é: {h}")
print(f"Para homens, seu peso ideal é: {formula_h}")
print(f"Para mulheres, seu peso ideal é: {formula_m}")

# %%