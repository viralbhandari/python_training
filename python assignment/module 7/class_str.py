class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return (self.color,self.mileage)
def main():
    my_car=Car('red','18')
    print(my_car.__str__())
main()

