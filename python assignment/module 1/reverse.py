a = int(input("Enter a five digit number: "))
print(a)
rev=0

while(a!=0):
    i=a%10;
    rev=(rev*10)+i
    a=a//10;
print(rev)
        
