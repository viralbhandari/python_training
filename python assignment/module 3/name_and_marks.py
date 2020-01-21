st=list(input("enter the first name ,theory and practical marks of student").split(","))
n=list(map(int,st[1:]))
sum1=sum(n[2:5])
sum2=sum(n[6:8])
per=((sum1+sum2)/590)*100
print(sum1,'',sum2,'percentage is ',per)
print('',st[0],'obtained',sum1,'marks out of 500 in theory ',sum2,'marks out of 90 in practical and successfully passed the exam with ',per,'in aggregate.Many congratulations to ',st[0])
