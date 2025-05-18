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
        jugador.consultar_digicoin()
        print("Elige que objeto desea comprar")
        print("1.Digipyballs -----> 5 digicoins")
        print("2.Cocaina -------> 3 digicoins -----> 10 puntos de vida")
        print("3.MK677 -------> 4 digicoins -----> 7 puntos de ataque")
        print("4.Salir")
        opciontienda = input()
        if opciontienda == "1":
            if jugador.digicoins >= 5:
                print("Has comprado digipyballs")
                jugador.digicoins -= 5
                inventario.añadir_objeto("digipyballs", 1)
            else:
                print("Eres un pobre")
        if opciontienda == "2":
            print("Has comprado cocaina")
            if jugador.digicoins >= 3:
                jugador.digicoins -= 3
                inventario.añadir_objeto("cocaina", 1)
            else:
                print("Eres un pobre")
        if opciontienda == "3":
            if jugador.digicoins >= 4:
                jugador.digicoins -= 4
                print("Has comprado mk677")
                inventario.añadir_objeto("mk677", 1)
            else:
                print("Eres un pobre")
        if opciontienda == "4":
            print("Estas saliendo de la tienda")
            time.sleep(3)
            salir_tienda = False
# Esta función digishop lo que hace es que según las monedad que tú tengas; puedas comprar ciertos items para que los puedas usar en tus 
# digipymons dandoles ciertos beneficios que eso te lo añade en el inventario y los podras usar cuando quieras    
        

def generar_digipymon_aleatorio(lista_nombre):
    vida = random.randint(10 , 20)
    ataque = random.randint(1 , 10)
    nivel = random.randint(1 , 3)
    listatipo = ["fuego", "agua", "planta"]
    tipo = random.choice(listatipo)
    
    
    nombre = lista_nombre.obtener_nombre_digipymon()
    digypimon = Digipymon(nombre,vida,ataque,nivel,tipo)
    
    return digypimon
# Esta función generar_digipymon_aleatorio lo que hace es generarte ciertas estadisticas aleatorias para poder crear digipymons generados
# automáticamente, y el nombre lo coge del método de la clase ListaNombre obtener_nombre_digipymon
def combate(jugador):
    lista_nombre = ListaNombres()
    enemigos = Enemigo(lista_nombre.obtener_nombre_entrenador())
    print("Te vas a enfrentar a un entrenador enemigo")
    print("Te toca enfrentarte a " + enemigos.nombre)
    opcionpelea = input("¿Quieres pelear contra el? si/no ")
    if opcionpelea == "si":
        victoriajug = 0
        victoriaenm = 0
        enemigos.lista_digipymon = []
        for _ in range(jugador.cantidad_digipymon):
            enemigos.añadir_digipymon(generar_digipymon_aleatorio(lista_nombre))
        for i in range(jugador.cantidad_digipymon):
            digipymon_jugador = jugador.lista_digipymon[i]
            digipymon_enemigo = enemigos.lista_digipymon[i]
            
            if digipymon_jugador.vida == 0:
                print("Tu digipymon llamado " + digipymon_jugador.nombre + "se ha quedado sin vida. Por lo que pierdes el combate")
                victoriaenm += 1
            elif digipymon_jugador.ataque > digipymon_enemigo.ataque:
                print("El digipymon " + digipymon_jugador.nombre + " del jugador es más fuerte que el digipymon enemigo " + digipymon_enemigo.nombre + ", ganas el combate") 
                vidarestante = digipymon_jugador.vida  - digipymon_enemigo.vida
                digipymon_jugador.vida = digipymon_jugador.vida - vidarestante
                victoriajug += 1
                if digipymon_jugador.vida <= 0:
                    print("Tu digipymon a muerto en combate")
            elif digipymon_jugador.ataque < digipymon_enemigo.ataque:
                print("El digipymon " + digipymon_jugador.nombre + " del jugador es más débil que el digipymon enemigo " + digipymon_enemigo.nombre + ", pierdes el combate")
                vidarestante = digipymon_jugador.vida  - digipymon_enemigo.vida
                digipymon_jugador.vida = digipymon_jugador.vida - vidarestante
                victoriaenm += 1
                if digipymon_jugador.vida <= 0:
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
# Esta función combate lo que hace es primero generarte el nombre de tu enemigo y tu decides si quieres pelear con el o no; si decides no 
# pelear con él te quita una digicoin; pero si peleas con el; primero lo que hará sera generarle al enemigo los digipymons según cuantos el 
# jugador tenga y luego segun la vida del digipymon que tenga el jugador podrá pelear o no; si tiene vida ya lo que hace es comprobar el 
# ataque del digipymon del jugador con el del enemigo para saber si gana o pierde el combate y se va acumulando las victorias y derrotas
# y cuando terminen de pelear todos los combates de todos los digipymons se decide si ha ganado el jugador o a perdidor; en base a eso;
# se le quitan digicoins o se le dan
        
    

    
    
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
# Esta función menu lo que hace es imprimirte el menu del juego
def buscar_digipymon(jugador, inventario, lista_nombre):
    digipymon = generar_digipymon_aleatorio(lista_nombre)
    print(digipymon)
    porcentaje_captura = 100 - (digipymon.nivel * 10)
    print(f"Porcentaje de captura de capturar al digipymon: " + str(porcentaje_captura) )
    opcion = input("Quieres Capturar al digipymon: (s/n) ")
        
    if opcion == "s":
        if inventario.objetos["digipyballs"] >= 1:
            print(inventario.objetos["digipyballs"])
            
            if jugador.cantidad_digipymon < 6:
                print(f"Puedes empezar a capturar al digipymon: " + " propabilidad de capturar al digipymon " + str(porcentaje_captura))
        
                captura = random.randint(1,100) <= porcentaje_captura
        
                if captura:
                    jugador.añadir_digipymon(digipymon)
                    print (f"Capturaste a " + str(digipymon))
                else: 
                    print (f"No has conseguido capturar a " + str(digipymon))
            else: 
                print ("Estas en tu límite no puedes capturar mas Digipymon")
        else:
            ("No tienes digipyballs no puedes capturar")
    elif opcion == "n":
        ("Has huido por que no querias capturar al digipymon (o eres un cagao)")
# Esta función buscar_digipymon lo que hace es que te genera una posibilidad de captura de un digipymon aleatorio y ya tu decides si quieres 
# capturarlo o no; si lo intentas capturar ya que no sabes si lo vas a conseguir; te quita una digiball siempre; aunque no lo captures y podrás 
# intentar capturar digipymons hasta tener 5; despues de eso no podras capturar
def usar_item(jugador, inventario):
    print(inventario.objetos)

    if not inventario.objetos:
        print("No tienes onjetos en el inventario")
        return
    print("¿Que item desea usar?")
    seleccionar_objeto = input()

    if seleccionar_objeto in inventario.objetos:
        if inventario.objetos[seleccionar_objeto] > 0:
            print(f"Has usado {seleccionar_objeto} ")
        else:
            print("No puedes usar ese item ")
            return
    else:
        print("El item no esta en el inventario")
        return 
    
    if seleccionar_objeto == "digipyballs":
        print("No puedes usar este objeto en un Digipymon directamente")
        return
    if jugador.lista_digipymon:
        seleccionar_digipymon = jugador.lista_digipymon[0]
        if seleccionar_objeto == "cocaina":
            seleccionar_digipymon.vida += 10
            inventario.usar_objeto(seleccionar_objeto)
            print(f"{seleccionar_digipymon} ha recuperado 10 de vida ")
        elif seleccionar_objeto == "mk677":
            seleccionar_digipymon.ataque += 7
            inventario.usar_objeto(seleccionar_objeto)
            print(f"{seleccionar_digipymon} ha aumentado su ataque en 7 ")
        else:
            print("Este objeto no se encuentra disponible")
            return
# Esta función usar_item lo que hace es usar los items que ya tengas comprados o los que te dan al inicio y te va quitando 
# ese objeto con la función usar_objeto          
def main():
    lista_nombre = ListaNombres()
    enemigos = Enemigo(lista_nombre.obtener_nombre_entrenador())
    inventario = Inventario()
    print("En este mundo de digipymons, entra un nuevo entrenador de digipymones, que empieza una nueva aventura; dinos cual es tu nombre")
    jugador = Jugador(lista_nombre.obtener_nombre_entrenador())
    print("Saludos " + jugador.nombre)
    print("Estas apunto de empezar tu nueva aventura y dentro de nada seras el mejor entrenador de digipymons del mundo, que empiece tu aventura")
    print("Te daré un digipymon aleatorio y también te daré ciertos items para que puedes tener un buen comienzo. ¡Buena suerte!")
    digipymon = generar_digipymon_aleatorio(lista_nombre)
    print(digipymon)
    jugador.añadir_digipymon(digipymon)
    print("Te dieron 3 digipyballs y una de cocaina")
    inventario.añadir_objeto("digipyballs", 3)
    inventario.añadir_objeto("cocaina", 1)
    salir = True; 
    while salir:
        menu()
        opcion = input()
        if opcion == "1":
            buscar_digipymon(jugador, inventario, lista_nombre)
        elif opcion == "2":
            combate(jugador)
        elif opcion == "3":
            digishop(jugador, inventario)
        elif opcion == "4":
            usar_item(jugador, inventario)
        elif opcion == "5":
            print(inventario.objetos)
        elif opcion == "6":
            print("Estos son todos tus digipymons: ")
            print(jugador.consultar_digipymon())
        elif opcion == "7":
            print("Gracias por jugar a nuestro juego; te espero pronto")
            salir = False
# Esta función main lo que hace es crear al principio una mini historia del juego; te genera un nombre aleatorio y te genera un digipymon aleatorio
# y tambien te da ciertos items; y luego llama a las funciones implementadas arriba según lo que pida el usuario según la opción elegida en el menu
main()   
# Esto : main() lo que hace es llamar a la función main y ejecutarla

