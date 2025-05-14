import random
import time

from clase_listanombres import ListaNombres
from clase_enemigo import Enemigo
from clase_jugador import Jugador
from clase_digipymon import Digipymon
from clase_inventario import Inventario


def digishop(jugador, inventario):
    salir_tienda = True
    while salir_tienda:
        print("Elige que objeto desea comprar")
        print("1.Digipyballs -----> 5 digicoins")
        print("2.Cocaina -------> 3 digicoins -----> 10 puntos de vida")
        print("3.MK677 -------> 4 digicoins -----> 7 untos de ataque")
        print("4.Salir")
        opciontienda = input()
        if opciontienda == 1:
            if jugador.digicoins >= 5:
                jugador.digicoins - 5
                inventario.añadir_objeto("Digipyballs", 1)
            else:
                print("Eres un pobre")
        if opciontienda == 2:
            if jugador.digicoins >= 3:
                jugador.digicoins - 3
                inventario.añadir_objeto("Cocaina", 1)
            else:
                print("Eres un pobre")
        if opciontienda == 3:
            if jugador.digicoins >= 4:
                jugador.digicoins - 4
                inventario.añadir_objeto("MK677", 1)
            else:
                print("Eres un pobre")
        if opciontienda == 4:
            print("Estas saliendo de la tienda")
            time.sleep(5)
            salir_tienda = False
            
        

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
    lista_nombre = ListaNombres()
    enemigos = Enemigo(lista_nombre.obtener_nombre_entrenador())
    print("Te vas a enfrentar a un entrenador enemigo")
    print("Te toca enfrentarte a " + enemigos.nombre)
    opcionpelea = input("¿Quieres pelear contra el? si/no")
    if opcionpelea == "si":
        

        
    

    
    
def menu():
    print("Elige una opcion") 
    print("1.Buscar Digipymon")
    print("2.Luchar contra entrenador")
    print("3.Ir a la tienda")
    print("4.Usar objetos" )
    print("5.Consultar inventario" )
    print("6.Consultar digypimon") 
    print("7.Salir")
    
    return menu

def buscar_digipymon(self,jugador,inventario):"""Funcion buscar digipymon"""
self.jugador = jugador
self.inventario = inventario
digipymon = generar_digipymon_aleatorio()
print(digipymon)
porcentaje_captura = 100 - (digipymon.nivel * 10)
print(f"Porcentaje de captura de capturar al digipymon: " + porcentaje_captura )
opcion = print("Quieres Capturar al digipymon: (s/n) ")
    
if opcion == "s":
    if inventario.objetos["Digipyballs"] >= 1:
        print(inventario.objetos["Digipyballs"])
        
        if jugador.cantidad_digipymon < 6:
            print(f"Puedes empezar a capturar al digipymon: " + " propabilidad de capturar al digipymon " + porcentaje_captura)
     
            captura = random.radint(1,100) <= porcentaje_captura
     
            if captura:
             jugador.cantidad_digipymon += 1
             print ("Capturaste a " + [digipymon])
            else: 
             print ("No has conseguido capturar a " + [digipymon])
        else: 
            print ("Estas en tu límite no puedes capturar mas Digipymon")
    else:
        ("No tienes digipyballs no puedes capturar")
elif opcion == "n":
    ("Has huido por que no querias capturar al digipymon (o eres un cagao)")

def usar_item(jugado):
    Jugador = Jugador()
    Jugador.mostrar_inventario()

    if not Jugador.objetos:
        return
    
    seleccionar_objeto = ()

    if seleccionar_objeto in Jugador.objetos:
        if Jugador.objetos[seleccionar_objeto] > 0:
            print(f"Has usado {seleccionar_objeto} ")
        else:
            print("No puedes usar ese item ")
            return
    else:
        print("El item no esta en el inventario")
        return 
    
    if seleccionar_objeto == "Digipyballs":
        print("No puedes usar este objeto en un Digipymon directamente")
        return
    if Jugador.lista_digipymon:
        seleccionar_digipymon = Jugador.lista_digipymon[0]
        if seleccionar_objeto == "Cocaina":
            seleccionar_digipymon.vida + 10
            print(f"{seleccionar_digipymon} ha recuperado 20 de vida ")
        elif seleccionar_objeto == "MK677":
            seleccionar_digipymon.ataque + 7
            print(f"{seleccionar_digipymon} ha aumentado su ataque en 7 ")
        else:
            print("Este objeto no se encuentra disponible")
            return
        
        if Jugador.usar_objeto(seleccionar_objeto):
            print(f"Has usado el objeto {seleccionar_objeto} ")
        else:
            print(f"No se ha podido usar el objeto {seleccionar_objeto}")

        if seleccionar_objeto in Jugador.objetos:
            if Jugador.objetos[seleccionar_objeto] > 0:
                print(f"Te quedan {Jugador.objetos[seleccionar_objeto]}")
            else:
                print(f"Ya no te quedan más objetos {seleccionar_objeto}")
        else:
            print("No tienes Digipymons en tu equipo ")
         
def main():
    
    jugador = Jugador(lista_nombre.Obtener_nombre_entrenador)
    