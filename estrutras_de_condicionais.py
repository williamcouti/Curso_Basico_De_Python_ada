# > Estruturas condicionais

idade = 20

if idade >= 18:

    print('Você e maior de idade. ')
else: 

    print('Você e menor de idade.')

"""

Imagine que você queira imprimir "Aaprovada(o), caso o estudante
tenha uma media superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7

"""

media = float(input('Informe a média do estudante: '))

if media >= 7:
    print('Você foi aprovado(o)')
elif media >= 5:
    print('Recuperação')
else:
    print('Voce foi reprovado')

media2 = 10

presenca = 100

if media2 >= 7 and presenca >= 70:
    print('Você foi aprovado(o)')
else:
    print('Voce foi reprovado')

