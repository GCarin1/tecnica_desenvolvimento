import time

class init:
    def step(self):
        while True:
            self.algo()
            continua = str(input('Deseja continuar a calcular ? \ny-Sim n-Não\n:'))

            if(continua=='y'):
                print("Preparando para proxima execução")
                print("================================")
                time.sleep(1)
            else:
                
                print("Finalizando programa...")
                print("================================")
                time.sleep(1)
                break
       
    def algo(self):

        a=float(input("Digite o valor de A\n:"))
        while(a<=0):
            print("valor de A é invalido")
            a=float(input("Digite o valor de A\n:"))
            

        b=float(input("Digite o valor de B\n:"))
        while(b<=0):
            print("valor de B é invalido")
            b=float(input("Digite o valor de B\n:"))
            
            
        c=float(input("Digite o valor de C\n:"))
        while(c<=0):
            print("valor de B é invalido")
            c=float(input("Digite o valor de C\n:"))
            
        else:
            r=float((a+b)**2)
            s=float((b+c)**2)
            d=float((r+s)/2)
            print(f'O valor de D é :{d}')


start=init()
start.step()


#Projeto integrado 
#Duas opções do projeto  