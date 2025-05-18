import random
class ListaNombres:
    def __init__(self):
        self.lista_nombres_digipymons = ["Chango",
    "Porcupike","Porcupike","Eletic","Cooper",
    "Iroquito","Boneton","Stunpecker","Scorpairy",
    "Raccocoon","Magmingo","Blastboon","Vemon","Drago",
    "Skyress","Trigerra","Wavern","Apollonoir",
    "Hex Dragonoid","Krozem"]
        self.lista_nombres_entrenadores = ["Zafira",
    "Kiran","Vader","Thor","Ilya","Jack","Lyra",
    "Elysia", "Peniten","Moon","Mark","Reaper",
    "Lena","Luke","Han","Cerebella","Eddie","Jose",
    "Gipsy","Miku"]
    def obtener_nombre_digipymon(self):
        return random.choice(self.lista_nombres_digipymons)
          
    def obtener_nombre_entrenador(self):
        return random.choice(self.lista_nombres_entrenadores)
# En esta clase ListaNombre lo que hace es tener unas listas con nombres predeterminados para luego utilizarlos en los métodos de la propia clase,
# el método obtener_nombre_digipymon sirve para pillar aleatoriamente un nombre de esa lista para luego usarlo en las partes del main y
# el método obtener_nombre_entrenador es el mismo funcionamiento que el anterior a diferencia de que es para entrenadores y no digipymons