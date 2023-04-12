class Componenta:
    def __init__(self, nume, firma, pret, consum, id):
        self.nume = nume
        self.firma = firma
        self.pret = pret
        self.consum = consum
        self.id = id
    def getnume(self):
        return self.nume+"   "+self.firma+" "+str(self.pret)+" lei"