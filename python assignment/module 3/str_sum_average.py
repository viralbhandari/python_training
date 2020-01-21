st=input("enter the subject and marks").split(' ')
l=[int(st[i]) for i in range(2,len(st),3)]
print("sum=",sum(l),"percentage=",round(sum(l)/len(l),2))

