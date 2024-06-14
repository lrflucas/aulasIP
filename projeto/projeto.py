#%%

#! Cadastro de Notas(Nome do aluno, Nota_1, Nota_2, Nota_3, Media, Resultado se aprovado ou reprovado);
#! CONCEITOS DE CRUD


import tkinter as tk        # importando a biblioteca tkinter pra criar interface gráfica, e chamando de tk
from tkinter import ttk     # importa especificamente o ttk da biblioteca tkinter, que fornece uma aparência melhor da interface



#* função pra calcular a média das 3 notas do aluno. aceita 3 parâmetros, que são as 3 notas

def calculo_media(nota1, nota2, nota3):

    notas = [float(nota1), float(nota2), float(nota3)]  # deixa as notas como float e armazena na lista           
    media = sum(notas) / len(notas)                     #! "sum" soma os valores da lista notas, "len" lê a quantidade de elementos na lista
    return media                                        # retorna o valor do cálculo da média  #! return pode ser usado para encerrar a execução da função ou para retornar um valor. nesse caso, retorna o valor da média para que ele possa ser utilizado em outras partes do código



#* função pra dizer se o aluno foi aprovado, reprovado ou se a média é inválida

def reprovado_ou_aprovado(media, aluno):  
                              
    if media >= 7.0 and media <= 10.0:                              
        return f"{aluno} está aprovado! A média foi {media}"        # se a média estiver entre 7 e 10, retorna dizendo que o aluno está aprovado
    elif media >= 0.0 and media < 7.0:                              
        return f"{aluno} está reprovado. Sua média foi {media}"     # se a média estiver entre 0 e 6.9, diz que o aluno está reprovado
    else:                                                           
        return f"Média inválida. Notas impossíveis."                # se a média não estiver entre 0 e 10, diz que a média é inválida
    


#* função pra coletar os dados do aluno a partir de campos de entrada e exibir essas informações na interface

def cadastrar_aluno():

    aluno = nome_entry.get()                                                                                    # coleta o nome do aluno e armazena na variável aluno
    nota1 = nota1_entry.get()                                                                             
    nota2 = nota2_entry.get()                                                                                   #! .get() é usado para recuperar o que foi inserido no Entry
    nota3 = nota3_entry.get()                                                                             

    media = calculo_media(nota1, nota2, nota3)                                                                  # chama a função "calculo_media" e armazena o resultado na variável media
    resultado = reprovado_ou_aprovado(media, aluno)                                                             # chama a função "reprovado_ou_aprovado" e armazena o resultado na variável resultado

    resultado_label.config(text=f" Nome do aluno: {aluno} \n Primeira nota: {nota1} \n Segunda nota: {nota2}"       
                                f"\n Terceira nota: {nota3} \n \n {resultado}")                                 # atualiza a configuração da label "resultado_label", definindo para mostrar o nome do aluno, as três notas, e o resultado se foi aprovado ou reprovado



#* função para criar o arquivo .txt

def criar_arquivo():

    with open("dados.txt", "w") as arquivo: #? cria um arquivo no modo de escrita
        arquivo.write("")                   #? cria um arquivo vazio chamado dados.txt, que vai ser usado pra armazenar os dados do projeto



#* função para adicionar um registro no arquivo .txt

def salvar_registro():

    aluno = nome_entry.get()
    nota1 = nota1_entry.get()
    nota2 = nota2_entry.get()
    nota3 = nota3_entry.get()

    media = calculo_media(nota1, nota2, nota3)     
    resultado = reprovado_ou_aprovado(media, aluno)
    dados = [aluno, nota1, nota2, nota3, media, resultado]

    with open("dados.txt", "a") as arquivo:                                     #? abre o arquivo dados.txt no modo de adição para adicionar novos dados ao final do arquivo                              
        arquivo.write("\n" + ",".join([str(elemento) for elemento in dados]))   #? escreve uma nova linha no arquivo contendo os dados do aluno e converte os elementos da lista em strings



#* função para ler o arquivo .txt

def ler_arquivo():

    with open("dados.txt", "r") as arquivo:     #? abre o arquivo em modo de leitura
        dados = arquivo.readlines()             #? lê todas as linhas do arquivo e armazena na lista dados
    return dados
    


#* função para procurar um registro no arquivo .txt

def procurar_registro():

    procurar_aluno = nome_entry.get().strip()                                               #! .strip() remove espaços em branco do início e do final de uma string
    dados = ler_arquivo()

    if not dados:                                                                           #? vê se dados está vazio
        resultado_label.config(text="Nenhum registro encontrado.")
    else:                                                                                   #? se dados não estiver vazio, inicializa a variável "encontrado" como false e a variável "texto" como uma string vazia
        encontrado = False
        texto = ""
        for linha in dados:
            elementos = linha.strip().split(",")                                            #? para cada linha, remove espaços em branco no início e no final e divide a linha em uma lista de elementos usando a vírgula como separador, armazenando essa lista na variável "elementos"
            if elementos[0] == procurar_aluno:                                              #? verifica se o nome do aluno é igual ao valor armazenado em "procurar_aluno"
                nota1_entry.delete(0, tk.END)
                nota1_entry.insert(0, elementos[1])
                nota2_entry.delete(0, tk.END)
                nota2_entry.insert(0, elementos[2])                                         #? se os nomes coincidirem, apaga qualquer texto existente nas entradas das notas e insere as respectivas notas do aluno
                nota3_entry.delete(0, tk.END)
                nota3_entry.insert(0, elementos[3])
                texto = (f" Nome do aluno: {elementos[0]} \n Primeira nota: {elementos[1]} \n Segunda nota: {elementos[2]}"
                         f"\n Terceira nota: {elementos[3]} \n \n {elementos[5]}")
                encontrado = True
                break
        if not encontrado:
            texto = "Aluno não encontrado."
        resultado_label.config(text=texto)                                                  # configura o texto do "resultado_label" para o valor de "texto"



#* função para atualizar um registro no arquivo .txt

def atualizar_registro():
    aluno = nome_entry.get()
    nota1 = nota1_entry.get()
    nota2 = nota2_entry.get()
    nota3 = nota3_entry.get()

    if not nota1 or not nota2 or not nota3:
        print("As notas devem ser inseridas.")
        return
    
    media = calculo_media(nota1, nota2, nota3)     
    resultado = reprovado_ou_aprovado(media, aluno)
    dados = ler_arquivo()

    for i in range(len(dados)):                                                     #? itera sobre os índices dos dados lidos do arquivo
        linha = dados[i].strip()
        if linha.startswith(aluno):                                                 #? verifica se a linha começa com o nome do aluno
            dados[i] = f"{aluno},{nota1},{nota2},{nota3},{media},{resultado}\n"
            break

    with open("dados.txt", "w") as arquivo:
        arquivo.writelines(dados)



#* função para excluir um registro no arquivo .txt

def excluir_registro():
    excluir_aluno = nome_entry.get()

    try:                                                #? bloco try-except, código dentro do bloco try é executado e erros são no bloco except
        with open("dados.txt", "r") as arquivo:
            dados = arquivo.readlines()

        with open("dados.txt", "w") as arquivo:
            for linha in dados:
                elementos = linha.strip().split(",")    #? remove espaços em branco no início e final da linha e então divide a linha em uma lista elementos usando a vírgula como delimitador
                if len(elementos) >= 4:                 # verifica se existem pelo menos 4 elementos
                    aluno = elementos[0].strip()        
                    if aluno != excluir_aluno:          #? verifica se o nome do aluno não é igual ao nome que se deseja excluir
                        arquivo.write(linha)            #? se o nome do aluno não corresponder ao "excluir_aluno", escreve a linha no arquivo, excluindo o registro do aluno cujo nome corresponde ao "excluir_aluno"

    except FileNotFoundError:                           #? se o arquivo não existir, uma mensagem de erro é impressa
        print("Nenhum registro encontrado.")



#* função para exibir os registros do arquivo .txt

def exibir_registros():
    dados = ler_arquivo()
    for linha in dados:
        linha = linha.strip()
        if linha:
            print(linha)



#todo - cria a janela principal da interface

criar_arquivo()                                 # cria o arquivo a cada vez que a janela é aberta
janela = tk.Tk()                                
janela.title("Cadastro de Notas dos Alunos")    # define o título da janela
janela.geometry("300x400")                      # define o tamanho da janela #! .geometry() é utilizado para especificar as dimensões da janela
janela.configure(bg="green")                    # define a cor de fundo como verde #! .configure() permite modificar várias propriedades da janela
fonte = ("Arial", 10)                           # tupla com dois elementos: o nome da fonte e o tamanho



#todo - cria as labels e entradas de texto

nome_label = ttk.Label(janela, text="Nome do aluno:")                                   # cria uma label na janela para o nome do aluno #! Label é usado para exibir textos ou imagens na interface, servem como elementos informativos e decorativos
nome_entry = ttk.Entry(janela)                                                          # entrada de texto na janela para inserir o nome #! Entry permite digitar informações

nota1_label = ttk.Label(janela, text="Primeira nota:")                                  
nota1_entry = ttk.Entry(janela)                                                         

nota2_label = ttk.Label(janela, text="Segunda nota:")                                   
nota2_entry = ttk.Entry(janela)                                                         

nota3_label = ttk.Label(janela, text="Terceira nota:")                                  
nota3_entry = ttk.Entry(janela)                                                         

calcular_botao = ttk.Button(janela, text="Calcular a média", command=cadastrar_aluno)   # cria um botão com o comando da função cadastrar_aluno

resultado_label = ttk.Label(janela, text="")                                            # cria uma label para exibir o resultado

salvar_botao = ttk.Button(janela, text="Salvar", command=salvar_registro)

ler_botao = ttk.Button(janela, text="Procurar", command=procurar_registro)

atualizar_botao = ttk.Button(janela, text="Atualizar", command=atualizar_registro)

excluir_botao = ttk.Button(janela, text="Excluir aluno", command=excluir_registro)



#todo - posiciona os widgets na janela

nome_label.grid(row=0, column=0, padx=5, pady=5)                        # posiciona a label do nome em uma grade
nome_entry.grid(row=0, column=1, padx=5, pady=5)                        # posiciona a entrada do nome, onde o usuário pode digitar

nota1_label.grid(row=1, column=0, padx=5, pady=5)                       
nota1_entry.grid(row=1, column=1, padx=5, pady=5)                       

nota2_label.grid(row=2, column=0, padx=5, pady=5)                       
nota2_entry.grid(row=2, column=1, padx=5, pady=5)                       

nota3_label.grid(row=3, column=0, padx=5, pady=5)                       
nota3_entry.grid(row=3, column=1, padx=5, pady=5)                       

calcular_botao.grid(row=6, column=0, columnspan=2, padx=5, pady=5)      # posiciona o botão para calcular a média, ocupando duas colunas (columnspan=2)

resultado_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)    

salvar_botao.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

ler_botao.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

atualizar_botao.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

excluir_botao.grid(row=12, column=0, columnspan=2, padx=5, pady=5) 



#todo - executa a interface gráfica

janela.mainloop()       # inicia o loop principal da interface gráfica, permitindo que a janela permaneça aberta e interativa enquanto o programa estiver em execução


# %%
