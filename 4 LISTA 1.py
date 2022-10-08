# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros 
# quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário 
# a quantidades de latas de tinta a serem compradas e o preço total.

import math
def mensagem(msg):
    print("-------------------------------------------------------------")
    print(msg)
    print("-------------------------------------------------------------")

mensagem("Bem Vindo ao Sistema Infertintas!")
metrosQuadrados = int(input("Informe a quantidade de metros quadrados a serem pintados: "))
custoTinta = 80.0
litrosTotal = 18
litrosNecessarios = metrosQuadrados / 3
totalLatas =  math.ceil(litrosNecessarios / litrosTotal)
custoTotal = totalLatas * custoTinta
mensagem("O Terreno tem %s metros quadrados\nE será necessário %s latas de tinta\nCom o custo total de R$ %s" %(metrosQuadrados,totalLatas,custoTotal))
