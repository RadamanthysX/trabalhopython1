# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
def mensagem(msg):
    print("-------------------------------------------------------------")
    print(msg)
    print("-------------------------------------------------------------")
mensagem("Bem vindo, informe o número abaixo para verificar se o mesmo é inteiro ou decimal")
num = float(input("Informe o número: "))
if num % 1 == 0:
    mensagem("O número escolhido é: %s\nÉ Inteiro" %(int(num)))
else:
    mensagem("O número escolhido é: %s\nÉ Decimal" %(num))