from automobile import Automobile
class Car(Automobile):
    def __init__(self,make,model,mileage,price,doors):
        self.doors=doors
    def s_doors(self):
          doors1=int(input('enter the number of doors'))
          self.doors=doors1
    def g_doors(self):
          return self.doors
def main():
    details=Car('xyz','65456','wrtray','6','9')
    
    details.s_make()
    details.s_model()
    details.s_mileage()
    details.s_price()
    details.s_doors()
    print("make=",details.g_make())
    print("model=",details.g_model())
    print("mileage=",details.g_mileage())
    print("price",details.g_price())
    print("doors=",details.g_doors()) 
main()

    

