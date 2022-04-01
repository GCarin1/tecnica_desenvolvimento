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
        b=float(input("Digite o valor de B\n:"))
        c=float(input("Digite o valor de C\n:"))
        
        if(a<=0):
            print("valor de A é invalido")
            time.sleep(1)
        elif(b<=0):
            print("valor de B é invalido")
            time.sleep(1)
        elif(c<=0):
            print("valor de B é invalido")
            time.sleep(1)
        else:
            r=float((a+b)**2)
            s=float((b+c)**2)
            d=float((r+s)/2)
            print(d)


start=init()
start.step()