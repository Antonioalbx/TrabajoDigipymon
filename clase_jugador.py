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


