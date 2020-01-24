import pickle
phonebook={'CHris':'8975454645','katie':'5553465764','joannie':'1324578968'}
output_file=open('phonebook.dat','wb')
pickle.dump(phonebook,output_file)
print(output_file)
output_file.close()
