people = {1:{'name':'john','age':'28','sex':'male'},2:{'name':'Marie','age':'24','sex':'female'}}
people[3]={}
people[3]['name']='luna'
people[3]['age']='25'
people[3]['sex']='female'
people[3]['married']='No'
print(people)

del people[3]['married']
print(people[3])
