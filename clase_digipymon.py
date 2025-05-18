class Digipymon:
    def __init__(self,nombre,vida,ataque,nivel,tipo):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel
        self.tipo = tipo
    
    def __str__(self):
        return f"Nombre: {self.nombre}, vida: {self.vida}, ataque: {self.ataque}, nivel: {self.nivel}, tipo: {self.tipo} "
# esta clase Digipymon lo que hace es pedir unos valores por parámetros y luego los devuelve son el str