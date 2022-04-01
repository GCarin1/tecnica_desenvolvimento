#Aula5
import math

class init:
    def step(self):
        self.distancia()
    
    def distancia(self):
        x1=input("Digite x1\n:")
        x1=int(x1)
        x2=input("Digite x2\n:")
        x2=int(x2)
        y1=input("Digite y1\n:")
        y1=int(y1)
        y2=input("Digite y2\n:")
        y2=int(y2)

        d1=(x2*x2-x1*x1)+(y2*y2-y1*y1)
        d2=math.sqrt(d1)

        print(f'Distancia entre os dois pontos em m\n:{d2}')
  
    

start=init()
start.step()