class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1
    def consultar_digipymon(self):
        for digipon in self.lista_digipymon:
            print("Este es tu digipypon " + digipon)
    def consultar_digicoin(self):
        print("Estas son tus monedas " + str(self.digicoins) )


