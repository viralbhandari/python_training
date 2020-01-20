a=int(input("enter the number of packages"))
p=99;total=0;
if(a>=100):
    print("discount=",(p*a*40)/100)
    print("total=",(p*a)-(p*a*40)/100)
elif(a>=50):
    print("discount=",(p*a*30)/100)
    print("total=",(p*a)-(p*a*30)/100)
elif(a>=20):
    print("discount=",(p*a*20)/100)
    print("total=",(p*a)-(p*a*20)/100)
elif(a>=10):
    print("discount=",(p*a*10)/100)
    print("total=",(p*a)-(p*a*10)/100)
else:
    print("no discount")
    print("total=",(p*a))
