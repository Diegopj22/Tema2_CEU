import math


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
        elif self.x > 0 and self.y < 0:
            print("El punto pertenence al cuarto cuadrante ")
        else:
            print("El punto se encuentra en el origen ya que x=0 y=0")
    
    def vector(self,punto):
        print("El vector entre{} y {} es ({},{})".format(self,punto,punto.x-self.x,punto.y-self.y))
    
    def distancia(self,punto):
        dis=math.sqrt((punto.x-self.x)**2 + (punto.y-self.y)**2)
        print("La distancia es ",dis)
            

            


        


    
        
    