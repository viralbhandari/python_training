arr=list(input("enter the array").split(" "))
print(arr)
p=list(map(int,arr))
n= len(arr)
sum1=6
s=set()
for i in range(0,n):
    temp=sum1-p[i]
    if (temp in s):
         print("pairs with given sum are:"+str(sum1)+"is("+str(arr[i])+","+str(temp)+ s.add(arr[i]))
         
