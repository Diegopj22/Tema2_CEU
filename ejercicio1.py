class Punto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self) :
        
        return(self.x,self.y)
    
    def cuadrante(self):
        if self.x>0 and self.y>0:
            print("El punto pertenece al primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print("El punto pertenece al segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print("El punto pertenence al tercer cuadrante")
        else:
            print("El punto pertenece al cuarto cuadrante")

            


        


    
        
    