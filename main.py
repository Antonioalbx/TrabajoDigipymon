import random
import time

from clase_listanombres import ListaNombres
from clase_enemigo import Enemigo
from clase_jugador import Jugador
from clase_digipymon import Digipymon
from clase_inventario import Inventario

listanombre = ListaNombres()
enemigos = Enemigo()
jugador = Jugador()
digypimon = Digipymon()
inventario = Inventario()

def generar_digipymon_aleatorio():
    vida = random.radiant(10 , 20)
    ataque = random.radiant(1 , 10)
    nivel = random.radiant(1 , 3)
    tipo = random.choice("fuego, agua y planta")
    
    lista_nombres = ListaNombres()
    nombre = lista_nombres.obtener_nombre_digipymon()
    digypimon = Digipymon(nombre,vida,ataque,nivel,tipo)
    
    return digypimon

def combate():
    print("Te vas a enfrentar a un entrenador enemigo")
    
    



def menu():
    print("Elige una opcion") 
    print("1.Buscar Digipymon")
    print("2.Luchar contra entrenador")
    print("3.Ir a la tienda")
    print("4.Usar objetos" )
    print("5.Consultar inventario" )
    print("6.Consultar digypimon") 
    print("7.Salir")


    