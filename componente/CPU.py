from componenta import *


class CPU(Componenta):
    def __init__(self, nume, firma, pret, consum, id, socket, an, gpu, frecventa):
        super().__init__(nume, firma, pret, consum, id)
        self.socket = socket
        self.an = an
        self.gpu = gpu
        self.frecventa = frecventa

    def __str__(self):
        return (f"Nume:{self.nume}\nFirma: {self.firma}\nAn: {self.an}\nGPU: {self.gpu}\nSoket: {self.socket}\n"
                f"Frcventa:{self.frecventa}\nConsum energie: {self.consum}\nPret: {self.pret} lei\nid: {self.id}")
