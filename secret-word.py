palavra_secreta = 'morango'
formatada = ''
palavra_formatada = ''
tentativas = 0


while palavra_secreta != palavra_formatada:
    if(tentativas == 10):
        print("Esgotou a tentativas")
        break
    letra_digitada = input("Digite uma letra: ")
    qtd_letra = len(letra_digitada)
    tentativas += 1

    while (qtd_letra > 1 or qtd_letra == 0):
        print("Digite apenas uma letra: ")
        letra_digitada = input("Digite uma letra: ")
        qtd_letra = len(letra_digitada)
        continue

    if letra_digitada in palavra_secreta:
        formatada += letra_digitada

    palavra_formatada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in formatada:
            palavra_formatada += letra_secreta
        else:
            palavra_formatada += '*'
    print(palavra_formatada)

if palavra_secreta == palavra_formatada:
    print(f"Parabéns, a palavra secreta é {palavra_secreta}. Você acertou!!")
else:
    print(f"Você errou, a palavra secreta era {palavra_secreta}")