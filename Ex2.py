import random
class Exercicio():
    def __init__(self):
        self.moeda = ["Cara", "Coroa"]
        self.primos = [2, 3, 5, 7, 11, 13, 17, 19]

    def setMoeda(self, moeda):
        self.moeda = moeda

    def getMoeda(self):
        return self.moeda    
        
    def setPrimos(self, primos):
        self.primos = primos

    def getPrimos(self):
        return self.primos

    def ex2_q1(self):
        q1 = [random.randrange(6, 20, 6), random.randint(16, 20)]
        q1 = random.choice(q1)
        return q1
    """
    Em um dado de 20 lados, o resultado ser maior que 15 ou multiplo de 6
    = {6, 12, 16, 17, 18, 19, 20}
    """


    def ex2_q2(self):
        q2 = [random.randrange(2, 6, 2), random.randrange(3, 6, 3)]
        q2 = random.choice(q2)
        return q2
    '''    
    Em um dado de 6 lados, o resultado ser multiplo de 2 ou 3
    = {2, 3, 4, 6}
    '''


    def ex2_q3(self):
        q3 = random.sample(ex.getMoeda(), 2)  ##Espaço Amostral jogando 3 moedas = {(Cara, Cara, Cara), (Cara, Cara, Coroa), (Cara, Coroa, Cara), (Cara, Coroa, Coroa), 
        return q3 
    '''
    Jogar 2 moedas e o resultado ser diferente entre elas = {("Cara", "Coroa"), ("Coroa", "Cara")}
    '''


    def ex2_q4(self):
        q4 = random.randrange(1, 10, 2)
        for q4 in ex.getPrimos():
            return (q4)
        else:
            return None
    '''
    Em um dado de 6 lados, o resultado ser primo e par
    = {2}
    '''


    def ex2_q5(self):
        q5 = random.choice(ex.getMoeda())
        return q5

    '''
    Jogar uma moeda e o resultado ser Cara ou Coroa
    = {Cara, Coroa}
    '''


    def ex2_q6(self):
        q6 = random.randint(1, 6)
        return q6

    '''
    Jogar um dado de 6 faces e o resultado ser Par ou Impar
    = {1, 2, 3, 4, 5, 6}
    '''


    def ex2_q7(self):
        n = int(input("Quantas vezes vc quer que jogue o dado? "))
        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0
        n5 = 0
        n6 = 0
        i = 0
        while i < n:
            q7 = random.randint(1,6)
            print("Resultado:",q7)
            if q7 == 1:
                n1 += 1
            elif q7 == 2:
                n2 +=1
            elif q7 == 3:
                n3 +=1
            elif q7 == 4:
                n4 +=1
            elif q7 == 5:
                n5 +=1
            else:
                n6 +=1
            i+=1
        print ("Quantidade que a moeda foi jogada: ", n)
        print ("Quantidade de resultado 1: ", n1)
        print ("Quantidade de resultado 2: ", n2)
        print ("Quantidade de resultado 3: ", n3)
        print ("Quantidade de resultado 4: ", n4)
        print ("Quantidade de resultado 5: ", n5)
        print ("Quantidade de resultado 6: ", n6)

    '''
    Jogue um dado varias vezes e saiba quantas vezes saiu cada resultado
    '''


    def ex2_q8(self):
        n = int(input("Quantas vezes vc quer que jogue o dado? "))
        cara = 0
        coroa = 0
        i = 0
        while i < n:
            q8 = random.choice(ex.getMoeda())
            print("Resultado:",q8)
            if q8 == "Cara":
                cara += 1
            else:
                coroa +=1
            i+=1
        print ("Quantidade que a moeda foi jogada: ", n)
        print ("Quantidade de Cara: ", cara)
        print ("Quantidade de Coroa: ", coroa)

    '''
    Jogue um dado varias vezes e saiba quantas vezes saiu cada resultado
    '''


class Menu():
	
    def __init__(self):
        self._opcao = None

    def getOpcao(self): 
        return self._opcao

    def setOpcao(self, opcao): 
        self._opcao = opcao

    def painel(self):
        while self.getOpcao() != 9:
            print("Selecione uma opção abaixo:")
            print("##Interseção##")
            print("1 - Em um dado de 20 lados, o resultado ser maior que 15 ou multiplo de 6")
            print("2 - Em um dado de 6 lados, o resultado ser multiplo de 2 ou 3")
            print("##União##")
            print("3 - Jogar 2 moedas e o resultado ser diferente entre elas")
            print("4 - Em um dado de 6 lados, o resultado ser primo e par")
            print("##Igualdade##")
            print("5 - Jogar uma moeda e o resultado ser Cara ou Coroa")
            print("6 - Jogar um dado de 6 faces e o resultado ser Par ou Impar")
            print("##Extra##")
            print("7 - Jogue um dado varias vezes e saiba quantas vezes saiu cada resultado")
            print("8 - Jogue uma moeda varias vezes e saiba quantas vezes saiu cada resultado")
            print("9 - Sair do programa")
            self.setOpcao(int((input (">"))))
            if self.getOpcao() == 1:
                print(ex.ex2_q1())
            elif self.getOpcao() == 2:
                print(ex.ex2_q2())
            elif self.getOpcao() == 3:
                print(ex.ex2_q3())
            elif self.getOpcao() == 4:
                print(ex.ex2_q4())
            elif self.getOpcao() == 5:
                print(ex.ex2_q5())
            elif self.getOpcao() == 6:
                print(ex.ex2_q6())
            elif self.getOpcao() == 7:
                print(ex.ex2_q7())
            elif self.getOpcao() == 8:
                print(ex.ex2_q8())
            elif self.getOpcao() == 9:
                print("Tchau!! :)")
            else:
            	print("Opção invalida! Tente novamente")


##Execução
ex = Exercicio()
menuPainel = Menu()
menuPainel.painel()