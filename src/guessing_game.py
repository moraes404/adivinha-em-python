import random


try:
    def gameTitle():

        print("\n##############################################")
        print("###### Bem-vindo(a) ao jogo de adivinha!######")
        print("##############################################")

        global tryNum
        tryNum = None
        while tryNum == None:
            try:
                tryNum = int(input("\n###### Quantas tentativas você deseja?\n:"))
            except ValueError:
                print("###### digite um número inteiro!!")

        while True:
            if 1 > tryNum:
                print("###### Número de tentativas inválido!")
                tryNum = int(input("\n###### Quantas tentativas você deseja?\n:"))
                return tryNum
            else:
                print("###### Beleza. Vamos começar!")
                break
        gameStart()
        
    def gameStart():
        global tryNum
        while tryNum > 0:
            try:
                userNum = int(input("\n###### Escolha um número entre 1 e 10\n:"))
            except ValueError:
                print("###### digite um número inteiro entre 1 e 10!!")
                continue

            randomNum = random.randint(1,10)

            if userNum == randomNum:
                print("###### Temos o mesmo número!!!")
                tryNum -= 1

            if userNum != randomNum:
                print("###### O meu é diferente!!")
                tryNum -= 1

            if userNum < 1 or userNum > 10:
                print("###### Número inválido")
            else: 
                print("###### Meu número era:", randomNum)

            if tryNum == 0 or userNum == randomNum:
                print("\n##########################")
                print("###### Fim do jogo! ######")
                print("##########################\n")
                break
        gameRestart()

    def gameRestart():

        restart = None

        while True:
            restart = input("###### Quer tentar novamente? (S/N)\n:").upper()

            if restart == "S":
                print("###### Vamos lá!!")
                gameTitle()
            elif restart == "N":
                exit()
            else:
                print("###### Insira resposta válida")
                continue
    gameTitle()
except KeyboardInterrupt:
    print("\nFechando...")