import sys
datastore={'office':{'medical':[
    {'room-number':'100','use':'reception','sq-ft':50,'price':75},
    {'room-number':'101','use':'waiting','sq-ft':250,'price':75},
    {'room-number':'102','use':'examination','sq-ft':125,'price':150},
    {'room-number':'103','use':'examination','sq-ft':125,'price':150},
    {'room-number':'104','use':'office','sq-ft':150,'price':100}],
    'parking':[{'location':'premium','style':'covered','price':750}]}}
print(datastore)
len1=len(datastore['office']['medical'])
len2=len(datastore['office']['parking'])
print(len1)
print(len2)

def add(arg):
    if(arg=='medical'):
        datastore['office']['medical'].append({'room_number':'105','use':'waiting','sq-ft':50,'price':125})
    print(datastore['office']['medical'])
    if(arg=='parking'):
        dict1={'parking':{'room_number':'105','use':'waiting','sq-ft':50,'price':125}}
        print(dict1.update(datastore['office']['parking']))

def update(arg,r):
    if(arg=='medical'):
        for i in range(0,len1):
            if(r>=0):
                key=int(input('what do you want to change 1.room number,2.use,3.area,4.price'))
                if(key==1):
                    new=(input('enter new room no'))
                    datastore['office']['medical'][r]['room-number']=new
                    print(datastore)
                    break
                if(key==2):
                    new=(input('enter new usability'))
                    datastore['office']['medical'][r]['use']=new
                    print(datastore)
                    break
                if(key==3):
                    new=(input('enter new area'))
                    datastore['office']['medical'][r]['sq-ft']=new
                    print(datastore)
                    break
                if(key==4):
                    new=(input('enter new price'))
                    datastore['office']['medical'][r]['price']=new
                    print(datastore)
                    break
    else:
        for i in range(0,len2):
            if(r>=0):
                key=int(input('what do you want to change 1.location,2.style,3.price'))
                if(key==1):
                    new=(input('enter new location'))
                    datastore['office']['parking'][r]['location']=new
                    print(datastore)
                    break
                if(key==2):
                    new=(input('enter new style'))
                    datastore['office']['parking'][r]['style']=new
                    print(datastore)
                    break
                if(key==3):
                    new=(input('enter new price'))
                    datastore['office']['parking'][r]['price']=new
                    print(datastore)
                    break

def delete(arg,r):
    if(arg=='medical'):
        datastore['office']['medical'][r]=("")
        print(datastore)
    else:
             datastore['office']['parking'][r]=("")
             print(datastore)

         
def exit():
    sys.exit()
    

def main():
    while(True):
        print("1.ADD")
        print("2.Update")
        print("3.DELETE a row")
        print("4.EXIT")
        
        ch=int(input("enter your choice"))
        if(ch==1):
            print("Medical or Parking")
            c=input("Where you want to add")
            add(c)
        if(ch==2):
            print("Medical or Parking")
            c=input("Where you want to update")
            r=int(input('in which row you want to change?'))
            update(c,r)
        if(ch==3):
            print("Medical or Parking")
            c=input("where do you want to delete")
            r=int(input('which row you want to delete?'))
            delete(c,r)
        if(ch==4):
            exit()
            
main()
