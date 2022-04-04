
import time

class main:
    def init(self):
        
        while True:

            choice=int(input("Escolha qual função deseja executar\n\n1-Converter int para Binario\n2-Soma\n3-Subtração\n4-Multiplicação\n5-Divisão\n6-Todas as opções\n:"))

            if(choice==1):self.converter()
            elif(choice==2):self.sumbin()
            elif(choice==3):self.subbin()
            elif(choice==4):self.multbin()
            elif(choice==5):self.divbin()
            elif(choice==6):self.todasbin()
            
            continua = str(input('Deseja continuar utilizando a calculadora/conversor de binario ? \ny-Sim n-Não\n:'))
            if(continua=='y'):
                print(f"Preparando para proxima execução")
                print(f"================================")
                
            else:
                time.sleep(1)
                print(f"Saindo da calculadora ")
                break

    def converter(self):

        a=bin(int(input("Digite um numero\n:")))

        print(a)
        while True:
            continua = str(input('Deseja converter um número inteiro para  binario ? \ny-Sim n-Não\n:'))
            if(continua=='y'):
                print(f"Preparando para proxima execução")
                print(f"================================")
                
            else:
                time.sleep(1)
                print(f"finalizando função de conversão para número binario")
                break       
    def sumbin(self):
        a=bin(int(input("Digite um numero\n:")))
        b=bin(int(input("Digite um numero\n:")))
        n = bin(int(a, 2) + int(b, 2))
        print(f'A soma entre os números convertidos para o binario \n{n}\n')
        while True:
            continua = str(input('Deseja fazer a soma entre dois números binarios ? \ny-Sim n-Não\n:'))
            if(continua=='y'):
                print(f"Preparando para proxima execução")
                print(f"================================")
                
            else:
                time.sleep(1)
                print(f"finalizando função de soma entre números binarios")
                break
    def multbin(self):
        a=bin(int(input("Digite um numero\n:")))
        b=bin(int(input("Digite um numero\n:")))
        n = bin(int(a, 2) * int(b, 2))
        print(f'A soma entre os números convertidos para o binario \n{n}\n')
        while True:
            continua = str(input('Deseja fazer a multiplicação entre dois números binarios ? \ny-Sim n-Não\n:'))
            if(continua=='y'):
                print(f"Preparando para proxima execução")
                print(f"================================")
                
            else:
                time.sleep(1)
                print(f"finalizando função de multiplicação entre números binarios")
                break
    def subbin(self):
        a=bin(int(input("Digite um numero\n:")))
        b=bin(int(input("Digite um numero\n:")))
        n = bin(int(a, 2) - int(b, 2))
        print(f'A soma entre os números convertidos para o binario \n{n}\n')
        while True:
            continua = str(input('Deseja fazer a subtração entre dois números binarios ? \ny-Sim n-Não\n:'))
            if(continua=='y'):
                print(f"Preparando para proxima execução")
                print(f"================================")
                
            else:
                time.sleep(1)
                print(f"finalizando função de subtração entre números binarios")
                break
    def divbin(self):
        a=bin(float(input("Digite um numero\n:")))
        b=bin(float(input("Digite um numero\n:")))
        n = bin(float(a, 2) / int(b, 2))
        print(f'A soma entre os números convertidos para o binario \n{n}\n')
        while True:
            continua = str(input('Deseja fazer a divisão entre dois números binarios ? \ny-Sim n-Não\n:'))
            if(continua=='y'):
                print(f"Preparando para proxima execução")
                print(f"================================")
                
            else:
                time.sleep(1)
                print(f"finalizando função de divisão entre números binarios")
                break
    def todasbin(self):

        a=bin(int(input("Digite um numero\n:")))
        b=bin(int(input("Digite um numero\n:")))
        soma = bin(int(a, 2) + int(b, 2))
        subt= bin(int(a, 2) - int(b, 2))
        mult = bin(int(a, 2) * int(b, 2))
        div = bin(int(a, 2) / int(b, 2))

        print(f'A soma entre os números convertidos para o binario \n{soma}\n')
        print(f'A subtração entre os números convertidos para o binario \n{subt}\n')
        print(f'A multiplicação entre os números convertidos para o binario \n{mult}\n')
        print(f'A divisão entre os números convertidos para o binario \n{div}\n')

        while True:
            continua = str(input('Deseja fazer os calculos novamente ? \ny-Sim n-Não\n:'))
            if(continua=='y'):
                print(f"Preparando para proxima execução")
                print(f"================================")
                
            else:
                time.sleep(1)
                print(f"finalizando função de calculadora entre números binarios")
                break
     
          

start=main()
start.init()