numero_sorteado = 15

numero_escolhido = int(input('Informe um numero sorteado 1 e -20: '))

while numero_escolhido != numero_sorteado:
    print('Voce errou o numero tente novamente...')

    numero_escolhido = int(input('Informe um numero sorteado 1 e -20: '))
print('Parabens você acertou!')

#Exemplo doi estutura com contador

contador = 0 

while contador < 5:
    print(contador)

    contador = contador + 1