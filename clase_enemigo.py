class Enemigo:
        def __init__(self, nombre):
                self.nombre = nombre
                self.lista_digipymon = []
                self.cantidad_digipymon = 0
        def añadir_digipymon(self, digipymon):
                self.lista_digipymon.append(digipymon)
                self.cantidad_digipymon += 1
# Esta clase Enemigo lo que hace es pedir un nombre por parámetros y tiene una lista vacia; una cantidad de digipymons iniciada a 0,
# la método de añadir_digipymons para que guarde el digipymon en la lista y sume uno a la cantidad
