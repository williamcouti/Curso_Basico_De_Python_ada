
for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1, 12, 3):
    print(i)

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe s sua nota {i}: '))

    soma = soma + nota

print(soma / 3)
