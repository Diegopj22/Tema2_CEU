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
            

class Rectángulo:
    def __init__(self,punto_inicial,punto_final):
        self.punto_inicial=punto_inicial
        self.punto_final=punto_final
        if punto_final or punto_inicial ==None:
            punto_inicial=0
            punto_final=0
    
    def base(self):
        self.base=abs(self.punto_final.x-self.punto_inicial.x)
        print("la base del rectángulo es",self.base)
    
    def altura(self):
        self.altura=abs(self.punto_final.y-self.punto_inicial.y)
        print("la altura del rectángulo es",self.altura)
    
    def area(self):
        self.area=abs(self.base*self.altura)
        print("El área del rectángulo es",self.area)
    
        
    

        




        


    
        
    