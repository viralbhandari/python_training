from automobile import Automobile
class Suv(Automobile):
    def __init__(self,make,model,mileage,price,pass_cap):
        self.pass_cap=pass_cap
       
    def s_pass_cap(self):
          pass_cap1=int(input('enter the pass cap'))
          self.pass_cap=pass_cap1
    def g_pass_cap(self):
          return self.pass_cap

def main():
    details=Suv('xyz','65456','wrtray','6','9')
    
    details.s_make()
    details.s_model()
    details.s_mileage()
    details.s_price()
    details.s_pass_cap()
    print("make=",details.g_make())
    print("model=",details.g_model())
    print("mileage=",details.g_mileage())
    print("price",details.g_price())
    print("pass cap=",details.g_pass_cap()) 
main()

    
