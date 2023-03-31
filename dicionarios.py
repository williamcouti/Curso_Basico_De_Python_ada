# Dicionario

#Criando Dicionario

dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Willian', 'idade': 30, 'altura': 1.80 }

print(dicionario)
print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario['altura'])

# Adiciona elementos em um dicionario

dicionario['programador'] = True

print(dicionario)

#Sobrescreve o item do dicionario
dicionario['altura'] = 2

print(dicionario)

#Iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario)

#Testando a chave a existencia de uma chave

print('peso' in dicionario)
print('altura' in dicionario)