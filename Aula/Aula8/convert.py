import math

class init:
    def step(self):
        
        self.convert()
        
    def convert(self):

        conv=int(input("Digite o valor a ser convertido\n:"))
        b = bin(conv).replace("0b", "")
        print(f"{b}")

        #print(f"valor em binario{binario}\nvalor em octal{octal}\nvalor em hexadecimal{hexa}")

       
           

            

           

   
start=init()
start.step()