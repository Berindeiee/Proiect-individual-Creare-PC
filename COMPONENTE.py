import datetime
from typing import Callable, Union

import customtkinter

from componenta import *

class PLACA_DE_BAZA(Componenta):
    def __init__(self, nume, firma, pret, consum, id, slot_m2, placa_retea, placa_sunet, nr_usb, display_port, hdmi
                 , socket, versiune_ddr, capacitate_ram):  # consuml va fi trecut fara W
        super().__init__(nume, firma, pret, consum, id)  # pretul este in lei
        self.capacitate_ram = capacitate_ram
        self.versiune_ddr = versiune_ddr
        self.socket = socket
        self.hdmi = hdmi
        self.display_port = display_port
        self.nr_usb = nr_usb
        self.slot_m2 = slot_m2
        self.placa_retea = placa_retea
        self.placa_sunet = placa_sunet

    def scor(self):
        score = 50 - float(self.consum) + (self.capacitate_ram / 12) - self.pret / 100
        if (self.slot_m2 == 1):
            score += 1
        if (self.display_port == 1):
            score += 1
        if (self.hdmi == 1):
            score += 1
        score += self.nr_usb

        return score

    def __str__(self):
        return (
            f"Name:  {self.nume}\nCompany:  {self.firma}\nNetwork card:  {self.placa_retea}\nM2 Slots:  {self.slot_m2}\n"
            f"Power consumption:  {self.consum} W\nPrice:  {self.pret} RON\nNumber of USB ports:  {self.nr_usb}\nDisplay port:  {self.display_port}"
            f"\nHDMI:  {self.hdmi}\nSocket:  {self.socket}\nDDR version:  {self.versiune_ddr}\nRAM capacity:  {self.capacitate_ram}\nID:  {self.id}")

class CARCASA(Componenta):
    def __init__(self, nume, firma, pret, consum, id, panou_sticla, ventilatoare, capacitate, tip):
        super().__init__(nume, firma, pret, consum, id)
        self.panou_sticla = panou_sticla
        self.ventilatoare = ventilatoare
        self.capacitate = capacitate
        self.tip = tip

    def scor(self):
        score = self.ventilatoare * 4 + 10 * self.capacitate - float(self.consum) - self.pret / 100
        if (self.panou_sticla):
            score += 3
        return score

    def __str__(self):
        return (f"Name: {self.nume}\nCompany: {self.firma}\nFans:"
                f" {self.ventilatoare}\nGlass panel: {self.panou_sticla}\n"
                f"Type: {self.tip}\nPower consumption: {self.consum} W\nPrice: {self.pret} RON\nID: {self.id}")

class CPU(Componenta):
    def __init__(self, nume, firma, pret, consum, id, socket, an, gpu, frecventa):
        super().__init__(nume, firma, pret, consum, id)
        self.socket = socket
        self.an = an
        self.gpu = gpu
        self.frecventa = frecventa

    def scor(self):
        score = float(self.consum) / self.frecventa * 10 - (self.pret / 100)
        if (self.gpu == "Da"):
            score += 50
        score = score - ((datetime.datetime.now().year - self.an) * 15)
        return score

    def __str__(self):
        return (f"Name:{self.nume}\nCompany: {self.firma}\nYear: {self.an}\nGPU: {self.gpu}\nSocket: {self.socket}\n"
                f"Frequency: {self.frecventa} GHz\nPower consumption: {self.consum} W\nPrice: {self.pret} RON\nID: {self.id}")

class GPU(Componenta):
    def __init__(self, nume, firma, pret, consum, id, an):
        super().__init__(nume, firma, pret, consum, id)
        self.an = an

    def scor(self):
        score = 350 + float(self.consum) / 7
        score = score - ((datetime.datetime.now().year - self.an) * 15)
        return score

    def __str__(self):
        return (f"Name:   {self.nume}\nCompany:  {self.firma}\nYear:  {self.an}\nPower consumption:  {self.consum}"
                f" W\nPrice:  {self.pret} RON\nID:  {self.id}")

class RAM(Componenta):
    def __init__(self, nume, firma, pret, consum, id, versiune_ddr, capacitate, viteza, frecventa):
        super().__init__(nume, firma, pret, consum, id)
        self.versiune_ddr = versiune_ddr
        self.capacitate = capacitate
        self.viteza = viteza
        self.frecventa = frecventa

    def scor(self):
        score = 100 + self.viteza / 100 - self.pret / 100 - float(self.consum) / 8 + self.capacitate * 2
        return score

    def __str__(self):
        return (
            f"Name: {self.nume}\nCompany: {self.firma}\nSpeed: {self.viteza} MHz\nCapacity: {self.capacitate} Gb\nFrequency: {self.frecventa}\n"
            f"DDR version: {self.versiune_ddr}\nPower consumption: {self.consum} W\nPrice: {self.pret} RON\nID: {self.id}")

class STOCARE(Componenta):
    def __init__(self, nume, firma, pret, consum, id, viteza_scriere, viteza_citire, capacitate, tip):
        super().__init__(nume, firma, pret, consum, id)
        self.viteza_scriere = viteza_scriere
        self.viteza_citire = viteza_citire
        self.capacitate = capacitate
        self.tip = tip

    def scor(self):
        if self.tip in "SSD":
            score = 25
        else:
            score = 15
        score += float(self.viteza_citire) / 76 + float(self.viteza_scriere) / 76 - self.pret / 70
        return score

    def __str__(self):
        return (f"Name:  {self.nume}\nCompany: {self.firma}\nRead speed:"
                f":  {self.viteza_citire} mb/s\nCapacity: {self.capacitate}\nWrite speed:  {self.viteza_scriere} mb/s\n"
                f"Type: {self.tip}\nPower consumption:  {self.consum} W\nPrice:  {self.pret} RON\nID:  {self.id}")

class SURSA(Componenta):
    def __init__(self, nume, firma, pret, consum, id, modulara, capacitate, certificare):
        super().__init__(nume, firma, pret, consum, id)
        self.modulara = modulara
        self.capacitate = capacitate
        self.certificare = certificare

    def scor(self):
        score = self.capacitate / 10 - self.pret / 10
        return score

    def __str__(self):
        return (
            f"Name:   {self.nume}\nCompany: {self.firma}\nCertification: {self.certificare}\nModularity: {self.modulara}\n"
            f"Capacity: {self.capacitate} W\nPrice:  {self.pret} RON\nID: {self.id}")

class FloatSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int, float] = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0.0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[float, None]:
        try:
            return float(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(float(value)))