
class init:
    def step(self):
        
        self.ex()
        
    def ex(self):
       
            custof=float(input("Digite o custo de fabrica do carro: R$ ")
            distr=float((custof*28)/100)
            imposto=float((custof*45)/100)

            custo=float(custof+distr+imposto)

            print(f"Valor do Carro é : R${custo:.2f}")  

            

           

   
start=init()
start.step()