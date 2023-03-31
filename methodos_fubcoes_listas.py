
# > Methodo d elistas

lista = [1, 3, 12, 8, 2]

# append: Adicionar um elemento no final da lista

print('Antes do append', lista)
lista.append(3)
print('Depois do append', lista)


# insert ecolhe a posição onde adicionar na lista i quel objeto vc quer

lista.insert(2, 10)
print('Depois do insert', lista)

#extend pega os elementos da lista e colocar no final da lista
lista2 = [1, 2, 3]

lista.extend(lista2)
print('Depois do extend', lista)

#pop remover o elemento que vc expecificar ou remove oultimo elemento 
lista.pop()
print('Depois do pop', lista)

lista.pop(0)
print('Depois do pop', lista)

#remove remove o elemento que vc quer remover
lista.remove(3)
print('Depois do remove', lista)

#caunt contar os elementos na lista
print('Quantidade de 2 na lista', lista.count(2))

#index diz o idice de um elemento na lista
print('Indice do elemento 12:', lista.index(12))

#sort ordena uma lista
lista.sort()
print(lista)

#reverso
lista.sort(reverse=True)
print(lista)

#len quantos elementos tem na lista
print(len(lista))

#sum soma todos os elementos da lista
print(sum(lista))

#Max retorna o maior valos da lista
print('Maior valor da lista', max(lista))

#Min menor valos da lista
print('Menor elemento da lista', min(lista))


