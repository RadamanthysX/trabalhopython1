# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
# peso ideal, utilizando as seguintes fórmulas:
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7

while True:
    print("-----------------------------------------------------")
    print("Selecione seu Gênero de Acordo com as Opções a Seguir")
    print("[1] Masculino")
    print("[2] Feminino")
    print("[3] Sair")

    resp = float(input("Digite sua Opção: "))

    if resp == 1:
        h=float(input("Agora, Insira Sua Altura: "))
        m=(72.7*h) - 58
        print("Seu Peso Ideal é: ", m)
    elif resp == 2:
        h=float(input("Agora, Insira Sua Altura: "))
        m=(62.1*h) - 44.7
        print("Seu Peso Ideal é: ", m)
    elif resp == 3:
        print("Você escolheu 'Sair', obrigado por usar!")
        exit()
    else:
        print("-----------------------------------------------------")
        print("Opção Selecionada é Inválida")
    

    