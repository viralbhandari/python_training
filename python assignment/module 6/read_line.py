def main():
    infile=open('viral.txt','r')
    line=infile.readline()
    while line!='':
        amount=line
        line=infile.readline()
        print(amount)
    infile.close()
main()
