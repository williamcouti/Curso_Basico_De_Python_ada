# > Listas

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas =  [7.9, 9.7, 8.2]

#Criando Listas
lista = []
list = list()
lista = [26, 'willian', 3.14159, False]
lista_de_listas = [10,[1,2,3]]

#Idexação e slices(fatiamento)

lista = [26, 'willian', 3.14159, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#slices

lista = [10, 50, 40, 25, 60, 5]
print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

#Ultilizando os proprios elementos da lista
for elemento in lista:
    print(elemento)   

# Ultilizando os indices qunatos elementos a lista tem
print('Comprimento da Lista', len(lista))

for i in range(len(lista)):
    print(lista[i])