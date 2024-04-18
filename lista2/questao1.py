#%%

# Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10. 
# O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.

numero = float(input("Digite um número: "))

if numero > 10:
    print(f"{numero} é maior que 10.")
elif numero < 10:
    print(f"{numero} é menor que 10.")
else:
    print(f"{numero} é igual a 10.")

# %%