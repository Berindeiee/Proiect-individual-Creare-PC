from componenta import *


class GPU(Componenta):
    def __init__(self, nume, firma, pret, consum, id, an):
        super().__init__(nume, firma, pret, consum, id)
        self.an = an

    def __str__(self):
        return (f"Nume:{self.nume}\nFirma: {self.firma}\nAn: {self.an}"
                f"\nPret: {self.pret} lei\nid: {self.id}")
