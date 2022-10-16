from calendar import c
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

#Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.   
A=Punto(2,3)
B= Punto(5,5) 
C=Punto(-3,-1) 
D=Punto(0,0)    
#Consulta a que cuadrante pertenecen el punto A, C y D.
A.cuadrante()
C.cuadrante()
D.cuadrante()
#Consulta los vectores AB y BA
#A.vector(B)
#B.vector(A)

#Consulta la distancia entre los puntos 'A y B' y 'B y A' 
A.distancia(B)
B.distancia(A)

#Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0)
A.distancia(D)
B.distancia(D)
C.distancia(D)      

#Crea un rectángulo utilizando los puntos A y B.
#Consulta la base, altura y área del rectángulo
rectangulo=Rectángulo(A,B)
rectangulo.base()
rectangulo.altura()
rectangulo.area()



        


    
        
    