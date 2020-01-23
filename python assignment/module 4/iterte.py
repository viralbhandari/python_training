people = {1:{'name':'john','age':'28','sex':'male'},2:{'name':'Marie','age':'24','sex':'female'}}
for p_id,p_info in people.items():
    print("\nperson ID:",p_id)
    for key in p_info:
        print(key + ':',p_info[key])
