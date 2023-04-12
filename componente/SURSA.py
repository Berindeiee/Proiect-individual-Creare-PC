from componenta import *


class SURSA(Componenta):
    def __init__(self, nume, firma, pret, consum, id, modulara, capacitate, certificare, frecventa):
        super().__init__(nume, firma, pret, consum, id)
        self.modulara = modulara
        self.capacitate = capacitate
        self.certificare = certificare
        self.frecventa = frecventa

    def __str__(self):
        return (f"Nume:{self.nume}\nFirma: {self.firma}\nCapacitate: {self.capacitate}W\nCertificare: {self.certificare}\nModulara: {self.modulara}\n"
                f"Consum energie: {self.consum}\nPret: {self.pret} lei\nid: {self.id}")
