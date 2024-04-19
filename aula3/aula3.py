# Lista de convidados
convidados = ["Miguel", "João Augusto", "Manu"]

# Lista de frutas
cesta = ["Banana", "Melancia", "Amora"]

# Lista de valores em R$
precos = [3.90, 4.50, 2.89]

# Lista de idades
idades = [21, 35, 18, 24, 56]

#%%

# Lista de frutas
frutas = ["pêra", "uva", "maçã", "kiwi"]

# Alterando o elemento que está na posição 1
frutas[1] = "abacate"

frutas.insert(2, "morango")

del frutas[10]

indice_fruta = frutas.index("melancia")

del frutas[indice_fruta]

# %%

# Definição de uma tupla
dimensoes = (200, 50)
print("Dimensões originais")

for dimensao in dimensoes:
    print(dimensao)

# Alterando toda a tupla
dimensoes = (400 ,)

#%%

# Definição de um dicionário
professor = {"nome": "Wuldson", "idade": 23}

# Imprimindo os valores
print(professor["nome"])
print(professor["idade"])

# Acessando os valores
professor["nome"] = "Wuldson Rasta"
professor["idade"] = "33"

print(professor["nome"])
print(professor["idade"])

# Adicionando novos valores
professor["email"] = "wuldsonfranco.prof@gmail.com"
professor["cidade"] = "João Pessoa"
professor["cpf"] = "000.000.000-00"

# Removendo valores
del professor["cpf"]

# %%

linguagens_preferidas = {
    "Wuldson": "Python",
    "Arthur": "JavaScript",
    "Maria Laura": "Java",
    "Maria Eduarda": "Python",
    "Mario": "SQL"
}