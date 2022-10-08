# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o 
# rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o 
# estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma 
# multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a 
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade 
# de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima 
# os dados do programa com as mensagens adequadas.

def mensagem(msg):
    print("-------------------------------------------------------------")
    print(msg)
    print("-------------------------------------------------------------")

mensagem("Bem Vindo Ao Sistema Peixe")
QuiloPeixeMaximo = 50.0
QuiloPeixe = float(input("Forneça o peso do peixe em KG: "))

if (QuiloPeixe > QuiloPeixeMaximo):
    QuiloExcedido = QuiloPeixe - QuiloPeixeMaximo
    Multa = QuiloExcedido * 4
    mensagem("Você utrapassou o peso máximo em %s quilos \ne portanto pagará uma multa de R$ %s" %(QuiloExcedido,Multa))
else:
    mensagem("Você não ultrapassou o peso máximo, Portanto não haverá multa.\nPeso atigindo foi de %s" %(QuiloPeixe))