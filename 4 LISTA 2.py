# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo índice.
# Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []
for i in range(1, 6):
    print('%dº Pessoa' %i)
    idade = int(input('Informe a idade: '))
    altura = float(input('Digite a altura: '))
    idades.append(idade)
    alturas.append(altura)

print('-----------------------------------')
print('Ordem inversa')
print('Alturas')
print(alturas[::-1])
print('Idades')
print(idades[::-1])

print('-----------------------------------')
print('Ordem lida')
print('Alturas')
print(alturas)
print('Idades')
print(idades)
print('-----------------------------------')