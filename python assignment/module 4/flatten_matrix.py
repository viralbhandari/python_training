mat=[[1,2,3],[4,5],[6,7,8,9]]
flatten_mat=[]
for sublist in mat:
    for val in sublist:
        flatten_mat.append(val)
print(flatten_mat)


flatten_mat= [val for sublist in mat for val in sublist]
print(flatten_mat)
