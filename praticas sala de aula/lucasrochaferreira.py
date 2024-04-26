#%%

# Uma loja de frutas precisa armazenar informações sobre seus produtos. Para cada fruta, a loja deseja armazenar o nome, o preço e 
# a quantidade em estoque.

# ● a) Qual estrutura de dados em Python você usaria para armazenar essas informações? Explique sua escolha.
    
    #  Dicionário, pois ele guarda valores para cada chave, sendo mais fácil e organizado de armazenar as informações.

# ● b) Escreva um código Python que crie uma lista de frutas com pelo menos três itens, incluindo as informações de nome, preço e
# quantidade.

frutas = {
    "fruta1": ["Banana", "0.70", "20"],
    "fruta2": ["Maçã", "0.50", "30"],
    "fruta3": ["Tangerina", "0.80", "15"]
}

print(frutas)

#%%

# Uma empresa precisa calcular a média de notas de seus alunos em uma prova. As notas dos alunos estão armazenadas em uma lista.

# ● a) Escreva um código Python que utilize um laço for para calcular a média das notas dos alunos.

notas = [7.0, 6.0, 8.5, 3.5]

for media in notas:
    media = ((notas[0]+notas[1]+notas[2]+notas[3])/2)
    print(f"A média é: {media}.")
    break

# ● b) Explique como o laço for funciona neste código.

    # Ele percorre os dados da lista de notas, coloca a variável "media" para receber os dados da lista, calcula e printa o que a variável pede. 

# %%
