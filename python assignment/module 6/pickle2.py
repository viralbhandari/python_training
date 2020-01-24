import pickle
in_file=open('phonebook.dat','rb')
pb=pickle.load(in_file)
in_file.close()
print(pb)
