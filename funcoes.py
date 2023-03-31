# > Funções

#1. O que são funções e por que ultilizá-las?

#Funções ultilizadas anteriormente

#print() # - Imprime uma menssagem (int, float, str) no console (terminal, cmd)
#input() # - Retorna um dado informado pelo usuario (entrada padrão) e pode receber um string
#len() # - Recebe uma lista e retorna o tamanho dessa lista
#max() # - Retorna o maio valor de uma lista

# 2 Criação de funções
def saudacao():
    
    print('Seja bem vindo')
    print('Olá e um prazer ter você fazendo parte desse curso!')

saudacao()

#passando parametro para uma função
def saudacao(nome, curso):
    
    print(f'Seja bem vindo {nome}!')
    print(f'E um prazer ter você fazendo parte do curso de {curso}!')

saudacao('willian coutinho', 'Python')

#Função com parametro default
def saudacao(nome='Willian', curso='Python'):
    
    print(f'Seja bem vindo {nome}!')
    print(f'E um prazer ter você fazendo parte do curso de {curso}!')

saudacao()

#Funções com retorno
def soma(num1, num2):
   # print(f'Soma =' , num1 + num2)
   return num1 + num2

resultado = soma(5, 7)
print(f'O resultado da soma é', resultado)

#Funções com retorno
def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    
resultado = calculadora(10, 20, '-')

print(resultado)