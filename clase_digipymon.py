class Digipymon:
 def __init__(self,nombre,vida,ataque,tipo,nivel):
    self.nombre = nombre
    self.vida = vida
    self.ataque = ataque
    self.tipo = tipo
    self.nivel = nivel
    
    def __str__(self):
        return f"Nombre: {self.nombre}, vida: {self.vida}, ataque: {self.ataque}, tipo: {self.ataque}, nivel: {self.nivel} "