matrix=[]
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)


matrix=[[j for j in range(5)]for i in range(5)]
print(matrix)
    
