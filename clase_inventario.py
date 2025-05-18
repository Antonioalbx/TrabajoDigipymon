class Inventario:
    def __init__(self):
        self.objetos = {}
        
    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else: 
            self.objetos[nombre] = cantidad       
        
    def usar_objeto(self,nombre):
        if nombre in self.objetos and self.objetos[nombre] > 0:
            self.objetos[nombre] -= 1
    
            if self.objetos[nombre] == 0 :
                del self.objetos[nombre]
# Esta clase Inventario lo que hace es crear un diccionario vacio; luego tiene un método añadir_objeto para ese diccionario que añade 
# un objeto al diccionario y su cantidad; y luego tiene el método de usar_objeto que lo que hace es usar ese itean comprobando que
# primero exista ese objeto y que haya cantidades para poder usarse y que cuando no queden cantidades lo elimine del diccionario
        
       