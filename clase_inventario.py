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
        
       