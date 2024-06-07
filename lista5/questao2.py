#%%

# Use um dicionário para armazenar os números favoritos de algumas pessoas.
# Escolha cinco colegas, e pergunte quais seus números favoritos.
# Use seus nomes para serem as chaves de cada número favorito. Ao final, exiba o nome de cada pessoa e seu número favorito.

numeros = {"Pedro Brito": 28, "Cinthia": 23, "Rodrigo": 25, "Cauã": 9, "Filipe": 7}

for nome, numero in numeros.items(): # pra acessar tanto as chaves quanto os valores, você usa items().
    print(f"{nome}: {numero}")

# %%