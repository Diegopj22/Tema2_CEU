
lista =[2,4,8,-4,22,3,2,5,8]
def modificar(lista):
    resultado=[]
    for i in lista:
        if i not in resultado and i % 2 == 0:
            resultado.append(i)
    resultado.sort(reverse=True)       
    
    
    
        

    
    return (resultado)

print(modificar([2,4,8,-4,22,3,2,5,8]))

            
