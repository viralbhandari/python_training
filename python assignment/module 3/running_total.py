n=int(input("enter the number of trees"))
a=int(input("enter the total seconds"))
value = []
for i in range (0,n):
    x= input("enter the fruit values")
    value.append(x)
print(value)
k=max(value)
print("max value=",k)
x=value.index(k)
print(x)
sum1=value[x+1]+value[x+2]
sum2=value[x-1]+value[x-2]
sum3=value[x+1]+value[x-1]
if(sum1>sum2):
        if(sum1>sum3):
            print("total fruit value sum1 is",(sum1+k))
        else:
            print("total fruit value sum2 is",(sum2+k))
else:
    print("total fruit value is",(sum3+k))
    
