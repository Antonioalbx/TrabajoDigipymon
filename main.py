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

def buscar_digipymon(self,jugador,inventario):
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
         
def main():
    
    jugador = Jugador(lista_nombre.Obtener_nombre_entrenador)
    