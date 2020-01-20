a = int(input("Enter a five edigit number: "))
print(a)
sum=0

while(a!=0):
    i=a%10;
    sum=sum+i;
    a=a//10;
print(sum)
        
