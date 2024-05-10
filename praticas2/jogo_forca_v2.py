#%%

# Import
import random
from os import system, name

import tkinter as tk
from tkinter import ttk

# Função para limpar a tela
def limpa_tela():

    #windows
    if name == 'nt':
        _ =  system('cls')
    #linux ou mac
    else:
        _ = system('clear')

# Função conteudo
def game():

    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra:\n')

    #lista palavras
    palavra = ['banana', 'maçã', 'creatina', 'amendoim', 'whey']

    #usando a func random
    palavra = random.choice(palavra)

    #list comprehension - contando as letras e para cada uma ele vai colocar um traço
    letras_descobertas = ['_' for letra in palavra]
    chances = 8
    letras_erradas = []

    while chances > 0:
        print(''.join(letras_descobertas))
        print('\nchances restantes:', chances)
        print('letras erradas:', ''.join(letras_erradas))

        tentativa = input('\nDigite uma letra: ').lower()
        
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)


if __name__ == "__main__":
    game()
    print("\nParabéns, você está aprendendo.\n")

# Cria a janela principal

root = tk.Tk()
root.geometry("300x400")
root.title("Forca")
root.configure(bg="gray")
fonte = ("Arial", 10)

# Inicia o loop principal da interface grafica

root.mainloop()

# %%
