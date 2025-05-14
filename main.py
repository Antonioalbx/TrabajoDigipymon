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
        print("3.MK677 -------> 4 digicoins -----> 7 puntos de ataque")
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

def combate(jugador, enemigos, digypimon):
    print("Te vas a enfrentar a un entrenador enemigo")
    lista_nombre = ListaNombres()
    enemigos = Enemigo(lista_nombre.obtener_nombre_entrenador())
    print("Te vas a enfrentar a un entrenador enemigo")
    print("Te toca enfrentarte a " + enemigos.nombre)
    opcionpelea = input("¿Quieres pelear contra el? si/no")
    if opcionpelea == "si":
        victoriajug = 0
        victoriaenm = 0
        for i in range(int(jugador.cantidad_digipymon)):
            enemigos.añadir_digipymon(generar_digipymon_aleatorio())
        for m in range(int(jugador.cantidad_digipymon)):
            digipymon_jugador = jugador.lista_digipymon[m]
            digipymon_enemigo = enemigos.lista_digipymon[m]
            
            if digipymon_jugador.vida == 0:
                print("Tu digipymon llamado " + digipymon_jugador.nombre + "se ha quedado sin salir. Por lo que pierdes el combate")
                victoriaenm += 1
            elif digipymon_jugador.ataque > digipymon_enemigo:
                print("El digipymon " + digipymon_jugador + " del jugador es más fuerte que el digipymon enemigo " + digipymon_enemigo) 
                vidarestante = digipymon_jugador.vida  - digipymon_enemigo.vida
                digipymon_jugador -= vidarestante
                victoriajug += 1
                if digipymon_jugador.vida == 0:
                    print("Tu digipymon a muerto en combate")
            elif digipymon_jugador.ataque < digipymon_enemigo:
                print("El digipymon " + digipymon_jugador + " del jugador es más débil que el digipymon enemigo " + digipymon_enemigo)
                vidarestante = digipymon_jugador.vida  - digipymon_enemigo.vida
                digipymon_jugador -= vidarestante
                victoriaenm += 1
                if digipymon_jugador.vida == 0:
                    print("Tu digipymon a muerto en combate")
            elif digipymon_jugador.ataque == digipymon_enemigo:     
                    print("Ni ganais ni perdeis; es un empate")
        if victoriajug > victoriaenm:
            print("Has ganado el combate")
            jugador.digicoins += victoriajug
        elif victoriajug < victoriaenm:
            print("Has perdido el combate")
            jugador.digicoins -= victoriaenm
            if jugador.digicoins < 0:
                jugador.digicoins = 0
        
    elif opcionpelea == "no":
        print("Has decicido no pelear, te quitamos una digicoin")
        jugador.digicoins -= 1
        if jugador.digicoins < 0:
           jugador.digicoins = 0

        
    

    
    
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

def main():
    
    jugador = Jugador(lista_nombre.Obtener_nombre_entrenador)
    