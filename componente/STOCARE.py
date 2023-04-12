from componenta import *


class STOCARE(Componenta):
    def __init__(self, nume, firma, pret, consum, id, viteza_scriere, viteza_citire, capacitate, tip):
        super().__init__(nume, firma, pret, consum, id)
        self.viteza_scriere = viteza_scriere
        self.viteza_citire = viteza_citire
        self.capacitate = capacitate
        self.tip = tip

    def __str__(self):
        return (f"Nume:{self.nume}\nFirma: {self.firma}\nViteza_citire"
                f": {self.viteza_citire}\nCapacitate: {self.capacitate}Gb\nViteza_scriere: {self.viteza_scriere}\n"
                f"Tip:{self.tip}\nConsum energie: {self.consum}\nPret: {self.pret} lei\nid: {self.id}")
