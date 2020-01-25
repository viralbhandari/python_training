from automobile import Automobile
class Truck(Automobile):
    def __init__(self,make,model,mileage,price,drive_type):
        self.drive_type=drive_type
       
    def s_drive_type(self):
          drive_type1=input('enter the drive type')
          self.drive_type=drive_type1
    def g_drive_type(self):
          return self.drive_type
def main():
    details=Truck('xyz','65456','wrtray','6','9')
    
    details.s_make()
    details.s_model()
    details.s_mileage()
    details.s_price()
    details.s_drive_type()
    print("make=",details.g_make())
    print("model=",details.g_model())
    print("mileage=",details.g_mileage())
    print("price",details.g_price())
    print("drive type=",details.g_drive_type()) 
main()

