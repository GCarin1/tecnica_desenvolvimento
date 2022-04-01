#Aula5
import math

class init:
    def step(self):
        self.idades()
    
    def idades(self):
        idade=int(input("Digite a idade"))

        match idade:
            case 5 | 6 | 7:
                print("infantilA")
            case 8 | 9 | 10:
                print("infantilB")
            case 11 | 12 | 13:
                print("juvenilA")
            case 14 | 15 | 16 | 17:
                print("juvenilB")
            case 18:
                print("adulto")

         
start=init()
start.step()