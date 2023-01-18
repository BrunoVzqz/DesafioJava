number = int(input('Qual posicao da sequencia voce quer encontrar? '))

class Fibonnaci():
    def __init__(self, number):
        self.__number = number

    def calcPosition(self):
        n1 = 1
        n2 = 1
        if self.__number == 1 or self.__number == 2 or self.__number == 0:
            print("fib("+str(self.__number)+") = "+'1')
        else:
            for i in range(2, self.__number):
                answer = n1 + n2
                n2 = n1
                n1 = answer
                i += 1
            print("fib("+str(self.__number)+") = "+str(answer))

f = Fibonnaci(number)
f.calcPosition()


        
