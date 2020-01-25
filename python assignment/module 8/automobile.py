class Automobile:
    def __init__(self,make,model,mileage,price):
        self.make=make
        self.model=model
        self.mileage=mileage
        self.price=price
    def s_make(self):
          make1=input("enter the make")
          self.make=make1
    def g_make(self):
          return self.make
    def s_model(self):
          model1=input('enter the model')
          self.model=model1
    def g_model(self):
          return self.model
    def s_mileage(self):
          mileage1=int(input('enter mileage'))
          self.mileage=mileage1
    def g_mileage(self):
          return self.mileage
    def s_price(self):
          price1=int(input('enter price'))
          self.price=price1
    def g_price(self):
          return self.price
    def __str__(self):
          return(self.name,self.phone,self.email_address)


