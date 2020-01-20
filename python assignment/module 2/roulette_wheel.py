n=int(input("enter the pocket number"))

if(n==0):
    print("pocket is green");
elif(n>=29):
    if(n%2==0):
         print("pocket is red")
    else:
         print("pocket is black")
elif(n>=19):
     if(n%2==0):
         print("pocket is black")
     else:
         print("pocket is red")
elif(n>=11):
     if(n%2==0):
         print("pocket is red")
     else:
         print("pocket is black")
elif(n>=1):
     if(n%2==0):
         print("pocket is black")
     else:
         print("pocket is red")
    
