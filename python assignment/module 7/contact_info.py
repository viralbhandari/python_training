class Contact:
    def __init__(self,name,number,email):
        self.name=name
        self.number=number
        self.email=email
    def __str__(self):
        return (self.name,self.number,self.email)


def main():
    my_contact=Contact('viral','6895412','viral@gmail.com')
    print(my_contact.__str__())
main()
