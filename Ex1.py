import random

class Exercicio():
    def __init__(self):
        self.moeda = ["cara", "coroa"]
        self.primos = [2, 3, 5, 7, 11, 13, 17, 19]

    def setMoeda(self, moeda):
        self.moeda = moeda

    def getMoeda(self):
        return self.moeda    
        
    def setPrimos(self, primos):
        self.primos = primos

    def getPrimos(self):
        return self.primos

    def ex1_q1(self):
        return (random.randint(1, 10))   ##Eventos Aleatórios = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    def ex1_q2(self):
        q2 = random.randrange(2, 10, 2)  ##Números pares = {2, 4, 6, 8, 10}
        return q2

    def ex1_q3(self):
        q3 = random.randrange(1, 10, 2)  ##Números Impares = {1, 3, 5, 7, 9}
        return q3

    def ex1_q4(self):
        q4 = random.randrange(3, 10, 3)  ##Múltiplos de 3 = {3, 6, 9}
        return q4 

    def ex1_q5(self):
        q5 = random.choice(ex.getPrimos()) ##Números primos = {2, 3, 5, 7, 11, 13, 17, 19}
        return q5

    def ex1_q6(self):
        q6 = random.choices(ex.getMoeda(), k=3)  ##Espaço Amostral jogando 3 moedas = {(Cara, Cara, Cara), (Cara, Cara, Coroa), (Cara, Coroa, Cara), (Cara, Coroa, Coroa), 
        return q6                                ##(Coroa, Cara, Cara), (Coroa, Cara, Coroa), (Coroa, Coroa, Cara), (Coroa, Coroa, Coroa)}

class Menu():
	
    def __init__(self):
        self._opcao = None

    def getOpcao(self): 
        return self._opcao

    def setOpcao(self, opcao): 
        self._opcao = opcao

    def painel(self):
        while self.getOpcao() != 7:
            print("Selecione uma opção abaixo:")
            print("Dado de 10 lados")
            print("1 - Eventos Aleatórios")
            print("2 - Números pares")  
            print("3 - Números Impares")
            print("4 - Múltiplos de 3")
            print("Jogando um dado de 20 faces")
            print("5 - Números primos")  
            print("6 - Espaço Amostral jogando 3 moedas")
            print("7 - Sair do programa")
            self.setOpcao(int((input (">"))))
            if self.getOpcao() == 1:
                print(ex.ex1_q1())
            elif self.getOpcao() == 2:
                print(ex.ex1_q2())
            elif self.getOpcao() == 3:
                print(ex.ex1_q3())
            elif self.getOpcao() == 4:
                print(ex.ex1_q4())
            elif self.getOpcao() == 5:
                print(ex.ex1_q5())
            elif self.getOpcao() == 6:
                print(ex.ex1_q6())
            elif self.getOpcao() == 7:
                print("Tchau!! :)")
            else:
            	print("Opção invalida! Tente novamente")


##Execução
ex = Exercicio()
menuPainel = Menu()
menuPainel.painel()