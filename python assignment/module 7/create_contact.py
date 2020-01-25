
class Info:
     def __init__(self,name,phone,email_address):
          self.name=name
          self.phone=phone
          self.email_address=email_address
     def s_name(self):
          name1=input("enter the name")
          self.name=name1
     def g_name(self):
          return self.name
     def s_phone(self):
          phone1=int(input('enter the contact number'))
          self.phone=phone1
     def g_phone(self):
          return self.phone
     def s_email_address(self):
          email_address1=input('enter your email address')
          self.email_address=email_address1
     def g_email_address(self):
          return self.email_address
     def __str__(self):
          return(self.name,self.phone,self.email_address)
def main():
     details=Info('viral','65456','wrtray')
     p={}
     details.s_name()
     details.s_phone()
     details.s_email_address()
     print("name=",details.g_name())
     print("number",details.g_phone())
     print("email=",details.g_email_address())
     d={'name':'name','number':'number','email':'email'}
     print(d)
     
main()
