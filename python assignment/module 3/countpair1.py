l=list(map(int,input('Enter the elements of Array').split(' ')))
s=int(input('Enter the Sum'))
count=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==s:
            print(l[i],l[j])
            count+=1

         
