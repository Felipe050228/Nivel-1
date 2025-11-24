def contar_palavras(frase_dita):
    palavras_ditas = frase_dita.split() # fatia a frase por ispaço
    palavras_contadas = len(palavras_ditas) # conta quantas vezes a frase foi fatiada
    print(f"a frase \033[1;33m{frase_dita}\033[m tem um total de {palavras_contadas} palavras") # retona a frase e a quantidade de palavras


diga_uma_frase = input('diga um verso eu uma frase: ') # ler a frase dita
contar_palavras(frase_dita=diga_uma_frase) #coloca a frase na função "contar_palavras"