def func_vogal():
    vetor_caracteres = []

    # Lê 10 caracteres
    for i in range(10):
        caractere = input(f"Digite o {i + 1}º caractere: ")
        vetor_caracteres.append(caractere)

    vogais = 'aeiouAEIOU'
    qtd_vogais = 0
    vogais_lidas = []

    # Conta as vogais e armazena as lidas
    for v in vetor_caracteres:
        if v in vogais:
            qtd_vogais += 1
            vogais_lidas.append(v)

    # Imprime o resultado
    print(f"Foram lidas {qtd_vogais} vogais. Vogais lidas: {', '.join(vogais_lidas)}")

if __name__ == "__main__":
    main()


