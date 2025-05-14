import random
class ListaNombres:"""Clase ListaNombres definida"""
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
          
def Obtener_nombre_entrenador(self):
    return random.choice(self.lista_nombres_entrenadores)