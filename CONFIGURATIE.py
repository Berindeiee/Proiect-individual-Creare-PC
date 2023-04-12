class CONFIGURATIE:
    def __init__(self, placa_de_baza, cpu, gpu, ram, carcasa, sursa, stocare):
        self.placa_de_baza = placa_de_baza
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.carcasa = carcasa
        self.stocare = stocare
        self.sursa = sursa

    def __str__(self):
        return (f"Placa de baza: {self.placa_de_baza}\nCPU: {self.cpu}\nGPU: {self.gpu}\nRAM: {self.ram}\n"
                f"Carcasa: {self.carcasa}\nSursa: {self.sursa}\nStocare: {self.stocare}")
