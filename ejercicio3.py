
lista =[2,4,8,-4,22,3,2,5,8]
def modificar(lista):
    resultado=[]
    for i in lista:
        if i not in resultado:
            resultado.append(i)
            
    return (resultado)
print(modificar([2,4,8,-4,22,3,2,5,8]))
