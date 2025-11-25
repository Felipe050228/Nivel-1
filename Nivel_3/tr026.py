# Função que recebe uma lista e separa os números pares
def receber_lista(lista):
    lista_secundaria = []   # Vai guardar todos os números recebidos
    lista_pares = []        # Vai guardar apenas os números pares
    
    # Percorre cada número da lista original
    for numero in lista:
        lista_secundaria.append(numero)  # Adiciona o número à lista secundária
        if numero % 2 == 0:              # Testa se o número é par
            lista_pares.append(numero)   # Se for par, adiciona à lista de pares

    # Exibe o resultado com cores
    print(f"Da lista \033[1;33m{lista_secundaria}\033[m, os números pares são \033[1;34m{lista_pares}\033[m")


lista_original = []  # Lista onde serão guardados todos os números informados

# Loop principal para continuar pedindo números ao usuário
while True:
    try:
        # Solicita 10 números por vez (de 1 até 10)
        for i in range(1, 11):
            diga_um_numero = int(input('digiti um numero: '))
            lista_original.append(diga_um_numero)  # Adiciona o número à lista
        
    except:
        # Caso o usuário digite algo que não seja número
        print('\033[1;31m|ERRO| DIGITI UM NUMERO VALIDO\033[m')

    else:
        # Pergunta se o usuário quer continuar
        while True:
            sim_ou_não = input('quer continuar [S/N]: ').upper().strip()[0]

            if sim_ou_não == "N":  # Se escolher "N", sai do loop interno
                break
            elif sim_ou_não == "S":  # Se escolher "S", continua o programa
                break
            else:
                # Caso digite uma opção inválida
                print('\033[1;31m|ERRO| DIGITI UMA OPIÇÃO VALIDA\033[m')
        
        # Se respondeu "N", para o programa principal também
        if sim_ou_não == "N":
            break

# Chama a função passando a lista com todos os números digitados
receber_lista(lista=lista_original)
