from componenta import *


class CARCASA(Componenta):
    def __init__(self, nume, firma, pret, consum, id, panou_sticla, ventilatoare, capacitate, tip):
        super().__init__(nume, firma, pret, consum, id)
        self.panou_sticla = panou_sticla
        self.ventilatoare = ventilatoare
        self.capacitate = capacitate
        self.tip = tip

    def __str__(self):
        return (f"Nume:{self.nume}\nFirma: {self.firma}\nVentilatoare"
                f": {self.ventilatoare}\nPanou_sticla: {self.panou_sticla}\n"
                f"Tip:{self.tip}\nConsum energie: {self.consum}\nPret: {self.pret} lei\nid: {self.id}")
