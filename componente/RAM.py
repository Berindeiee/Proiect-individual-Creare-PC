from componenta import *


class RAM(Componenta):
    def __init__(self, nume, firma, pret, consum, id, versiune_ddr, capacitate, viteza, frecventa):
        super().__init__(nume, firma, pret, consum, id)
        self.versiune_ddr = versiune_ddr
        self.capacitate = capacitate
        self.viteza = viteza
        self.frecventa = frecventa

    def __str__(self):
        return (f"Nume:{self.nume}\nFirma: {self.firma}\nViteza: {self.viteza}\nCapacitate {self.capacitate}\nFrecventa: {self.frecventa}\n"
                f"Versiune ddr:{self.versiune_ddr}\nConsum energie: {self.consum}\nPret: {self.pret} lei\nid: {self.id}")
