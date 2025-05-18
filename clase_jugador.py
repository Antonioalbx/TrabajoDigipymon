class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1
        print("Has añadido a " + str(digipymon) + "a tus digipymones")
    def consultar_digipymon(self):
        for digipymon in self.lista_digipymon:
            print("Este es tu digipypon " + str(digipymon))
    def consultar_digicoin(self):
        print("Estas son tus monedas " + str(self.digicoins) ) 
        
# Esta clase Jugador lo que hace es pedir un nombre por parámetros y tiene una lista vacia; una cantidad de digipymons iniciada a 0
# y digicoins a 10; la método de añadir_digipymons para que guarde el digipymon en la lista y sume uno a la cantidad y te imprima un texto
# y el método consultar_digicoin que te devuelve un print con las monedas que tienes


