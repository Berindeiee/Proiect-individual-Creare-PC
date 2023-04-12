import os
from PIL import ImageTk,Image
from tkinter import Tk, Frame, Canvas
from tkinter import *
from tkinter import font
from tkinter import messagebox
import json
import customtkinter

from COMPONENTE import *


def get_culoare():
    if customtkinter.get_appearance_mode() == "Light":
        return 'gray92'
    else:
        return 'gray14'


def bttn1(fereastra, text, bcolor, cmd):
    fcolor = get_culoare()

    def on_enter(e):
        mybutton.configure(fg_color=bcolor)
        mybutton.configure(text_color=get_culoare())
        mybutton.configure(bg_color=get_culoare())

    def on_leave(e):
        mybutton.configure(fg_color=get_culoare())
        mybutton.configure(text_color=bcolor)
        mybutton.configure(bg_color=get_culoare())

    mybutton = customtkinter.CTkButton(fereastra, text=text,
                                       text_color=bcolor,
                                       # hover_color=bcolor,
                                       fg_color=fcolor,
                                       command=cmd,
                                       corner_radius=8,
                                       state="disabled"
                                       )
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)
    mybutton.pack(pady=1, padx=1)
    return mybutton


# Implementing event on register button

def logg(fereastra):
    width = 900
    height = 600

    def login_event():
        print("Login pressed - username:", username_entry.get(), "password:", password_entry.get())

        fereastra.login_frame.grid_forget()  # remove login frame
        fereastra.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

    def back_event():
        main_frame.grid_forget()  # remove main frame
        login_frame.grid(row=0, column=0, sticky="ns")  # show login frame

    login = customtkinter.CTkToplevel(fereastra)
    login.title("CustomTkinter example_background_image.py")
    login.geometry(f"{900}x{600}")
    login.resizable(False, False)
    light_image = Image.open("GPU.png")
    # load and create background image
    # current_path = os.path.dirname(os.path.realpath(__file__))
    bg_image = customtkinter.CTkImage(light_image=Image.open("bg_gradient.jpg"),
                                      dark_image=Image.open("bg_gradient.jpg"),
                                      size=(width, height))
    bg_image_label = customtkinter.CTkLabel(login, image=bg_image)
    bg_image_label.grid(row=0, column=0)

    # create login frame
    login_frame = customtkinter.CTkFrame(login, corner_radius=0)
    login_frame.grid(row=0, column=0, sticky="ns")
    login_label = customtkinter.CTkLabel(login_frame, text="CustomTkinter\nLogin Page",
                                         font=customtkinter.CTkFont(size=20, weight="bold"))
    login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
    username_entry = customtkinter.CTkEntry(login_frame, width=200, placeholder_text="username")
    username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
    password_entry = customtkinter.CTkEntry(login_frame, width=200, show="*", placeholder_text="password")
    password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
    login_button = customtkinter.CTkButton(login_frame, text="Login", command=login_event, width=200)
    login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    # create main frame
    main_frame = customtkinter.CTkFrame(login, corner_radius=0)
    main_frame.grid_columnconfigure(0, weight=1)
    main_label = customtkinter.CTkLabel(main_frame, text="CustomTkinter\nMain Page",
                                        font=customtkinter.CTkFont(size=20, weight="bold"))
    main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
    back_button = customtkinter.CTkButton(main_frame, text="Back", command=back_event, width=200)
    back_button.grid(row=1, column=0, padx=30, pady=(15, 15))
def surse_json():
    sursa = [
        SURSA('EcoGreen 550 Pro', 'Epic Gear', 150, 500, 1, 'Da', 550, '80+ Gold'),
        SURSA('EcoGreen 350 Pro', 'Epic Gear', 130, 450, 2, 'Da', 350, '80+ Gold'),
        SURSA('Gas VR 750', 'Gasneo', 200, 700, 3, 'Da', 750, '80+ Platinum'),
        SURSA('Gas VR 650', 'Gasneo', 160, 500, 4, 'Da', 650, '80+ Platinum'),
        SURSA('Neon Bronze 600', 'Neoxio', 120, 600, 5, 'Nu', 600, '80+ Bronze'),
        SURSA('Neon Bronze 500', 'Neoxio', 105, 500, 6, 'Nu', 500, '80+ Bronze'),
        SURSA('Fanta Gamer 900', 'Cyutron', 200, 800, 7, 'Da', 900, '80+ Platinum'),
        SURSA('Fanta Gamer 750', 'Cyutron', 140, 600, 8, 'Da', 750, '80+ Platinum'),
        SURSA('Geo 850', 'Geosafe', 150, 750, 9, 'Da', 850, '80+ Gold'),
        SURSA('Geo 750', 'Geosafe', 140, 600, 10, 'Da', 750, '80+ Gold'),
        SURSA('Kore 750', 'Korex', 110, 550, 11, 'Da', 750, '80+ Bronze'),
        SURSA('Kore 600', 'Korex', 100, 400, 12, 'Da', 600, '80+ Bronze'),
        SURSA('Vent 700', 'Airent', 130, 500, 13, 'Da', 700, '80 Plus'),
        SURSA('Vent 500', 'Airent', 140, 400, 14, 'Da', 500, '80 Plus'),
        SURSA('Cirrus 850', 'Artech', 170, 750, 15, 'Da', 850, '80+ Titanium'),
        SURSA('Cirrus 750', 'Artech', 140, 650, 16, 'Da', 750, '80+ Titanium'),
        SURSA('Luma 750', 'Lumar', 150, 650, 17, 'Da', 750, '80+ Silver'),
        SURSA('Luma 600', 'Lumar', 130, 550, 18, 'Da', 600, '80+ Silver'),
        SURSA('Vita 850', 'Vitalip', 175, 800, 19, 'Da', 850, '80 Plus'),
        SURSA('Vita 700', 'Vitalip', 140, 700, 20, 'Da', 700, '80 Plus'),
    ]
    with open('sursa.json', 'w') as file:
        json.dump(sursa, file, default=lambda o: o.__dict__, indent=4)
def stocari_json():
  stocari = [
      STOCARE('HDD Seagate Barracuda', 'Seagate', 300, '20', '1', '120', '150', '1TB', 'HDD'),
      STOCARE('SSD Corsair', 'Corsair', 400, '10', '2', '480', '520', '1TB', 'SSD'),
      STOCARE('HDD WD Blue', 'WD', 250, '25', '3', '90', '180', '1TB', 'HDD'),
      STOCARE('SSD Kingston A400', 'Kingston', 350, '5', '4', '450', '540', '1TB', 'SSD'),
      STOCARE('HDD Toshiba P300', 'Toshiba', 270, '15', '5', '100', '150', '1TB', 'HDD'),
      STOCARE('SSD Corsair Neutron NX500', 'Corsair', 480, '7', '6', '550', '600', '1TB', 'SSD'),
      STOCARE('HDD Seagate FireCuda', 'Seagate', 320, '17', '7', '110', '200', '1TB', 'HDD'),
      STOCARE('SSD Samsung 860 EVO', 'Samsung', 400, '10', '8', '520', '550', '1TB', 'SSD'),
      STOCARE('HDD Seagate SkyHawk', 'Seagate', 350, '27', '9', '90', '180', '1TB', 'HDD'),
      STOCARE('SSD Intel 760p', 'Intel', 380, '2', '10', '480', '560', '1TB', 'SSD'),
      STOCARE('HDD HGST Deskstar', 'HGST', 320, '20', '11', '100', '110', '1TB', 'HDD'),
      STOCARE('SSD OCZ RD400', 'OCZ', 500, '7', '12', '520', '600', '1TB', 'SSD'),
      STOCARE('SSD WD Black', 'WD', 500, '10', '13', '560', '600', '1TB', 'SSD'),
      STOCARE('HDD HGST Ultrastar', 'HGST', 300, '25', '14', '90', '150', '1TB', 'HDD'),
      STOCARE('SSD Samsung 860 QVO', 'Samsung', 420, '7', '15', '480', '550', '1TB', 'SSD'),
      STOCARE('HDD Toshiba X300', 'Toshiba', 340, '15', '16', '100', '125', '1TB', 'HDD'),
      STOCARE('SSD Samsung 970 Pro', 'Samsung', 600, '7', '17', '560', '650', '1TB', 'HDD'),
      STOCARE('SSD Intel 750', 'Intel', 570, '2', '18', '520', '600', '1TB', 'SSD'),
      STOCARE('HDD WD Red', 'WD', 280, '20', '19', '90', '160', '1TB', 'HDD'),
      STOCARE('SSD Patriot Scorch', 'Patriot', 490, '3', '20', '480', '520', '1TB', 'SSD')]
  with open('stocare.json', 'w') as file:
      json.dump(stocari, file, default=lambda o: o.__dict__, indent=4)
def ram_json():
    ram_uri = []
    ram1 = RAM('Viper', 'Corsair', 350, 35, 1, 'DDR4', 16, 3200, 'cl16')
    ram2 = RAM('Trident', 'G.Skill', 540, 23, 2, 'DDR4', 16, 3600, 'cl16')
    ram3 = RAM('Dominator Platinum', 'Corsair', 1600, 28, 3, 'DDR4', 32, 3200, 'cl16')
    ram4 = RAM('Ripjaws', 'G.Skill', 900, 25, 4, 'DDR4', 16, 4000, 'cl20')
    ram5 = RAM('Squad', 'HyperX', 560, 24, 5, 'DDR4', 8, 3200, 'cl16')
    ram6 = RAM('Flare X', 'O.C.M', 300, 26, 6, 'DDR3', 8, 1600, 'cl9')
    ram7 = RAM('Force', 'G.Skill', 340, 26, 7, 'DDR3', 8, 1600, 'cl10')
    ram8 = RAM('Neo Forza', 'Corsair', 240, 25, 8, 'DDR4', 8, 2133, 'cl13')
    ram9 = RAM('Trident', 'G.Skill', 260, 35, 9, 'DDR4', 8, 2400, 'cl14')
    ram10 = RAM('Ripjaws', 'G.Skill', 560, 30, 10, 'DDR3', 16, 1600, 'cl9')
    ram11 = RAM('Vengeance', 'Corsair', 400, 35, 11, 'DDR4', 16, 2400, 'cl13')
    ram12 = RAM('Ripjaws', 'G.Skill', 800, 26, 12, 'DDR4', 16, 3000, 'cl19')
    ram13 = RAM('Fury', 'HyperX', 800, 26, 13, 'DDR4', 16, 3200, 'cl18')
    ram14 = RAM('Viper', 'Corsair', 680, 28, 14, 'DDR4', 16, 2400, 'cl14')
    ram15 = RAM('8 GB DDR4', 'Komputerbay', 170, 29, 15, 'DDR4', 8, 2666, 'cl15')
    ram16 = RAM('Ripjaws V', 'G.Skill', 740, 31, 16, 'DDR4', 16, 2800, 'cl17')
    ram17 = RAM('AEGIS', 'Team', 240, 25, 17, 'DDR4', 8, 2133, 'cl14')
    ram18 = RAM('Dominator', 'Corsair', 1050, 29, 18, 'DDR4', 32, 3200, 'cl16')
    ram19 = RAM('Force', 'G.Skill', 580, 27, 19, 'DDR3', 16, 1600, 'cl11')
    ram20 = RAM('Aegis II', 'Team', 260, 24, 20, 'DDR4', 8, 2133, 'cl13')
    ram_uri.extend((ram1, ram2, ram3, ram4, ram5, ram6, ram7, ram8, ram9, ram10, ram11, ram12, ram13, ram14, ram15, ram16, ram17, ram18, ram19, ram20))

    with open('ram.json', 'w') as file:
        json.dump([el.__dict__ for el in ram_uri], file, indent = 4)
def gpu_json():
    my_list_of_gpu=[
        GPU("Geforce GTX 1080 Ti", "Nvidia", 2950, 260, 1, 2017),
        GPU("GeForce RTX 2060 SUPER", "Nvidia", 2550, 175, 2, 2019),
        GPU("GeForce RTX 2080 SUPER", "Nvidia", 3550, 250, 3, 2019),
        GPU("AMD Radeon RX 5700 XT", "AMD", 2300, 225, 4, 2019),
        GPU("GeForce RTX 2070 SUPER", "Nvidia", 2850, 215, 5, 2019),
        GPU("GeForce RTX 2080 Ti", "Nvidia", 4500, 350, 6, 2018),
        GPU("Radeon RX 560X", "AMD", 1050, 80, 7, 2017),
        GPU("AMD Radeon VII", "AMD", 4000, 300, 8, 2019),
        GPU("Radeon Pro V340 MxGPU", "AMD", 8583, 72, 9, 2017),
        GPU("GeForce GTX 1660 SUPER", "Nvidia", 1980, 125, 10, 2019),
        GPU("AMD Radeon RX 550", "AMD", 750, 50, 11, 2017),
        GPU("GeForce RTX 2060", "Nvidia", 1700, 160, 12, 2018),
        GPU("GeForce RTX 2080 Ti Founders Edition", "Nvidia", 5300, 375, 13, 2018),
        GPU("GeForce GTX 780", "Nvidia", 1200, 250, 14, 2013),
        GPU("AMD FirePro S7150x2", "AMD", 3192, 400, 15, 2017),
        GPU("AMD Radeon RX 580", "AMD", 1250, 185, 16, 2017),
        GPU("AMD FirePro S9170", "AMD", 7500, 375, 17, 2015),
        GPU("GeForce GTX 960", "Nvidia", 760, 120, 18, 2015),
        GPU("GeForce GTX 1070 Ti", "Nvidia", 2200, 180, 19, 2017),
        GPU("GeForce GTX TITAN X", "Nvidia", 2930, 250, 20, 2015)
    ]
    with open('gpu.json', 'w') as file:
        json.dump([el.__dict__ for el in my_list_of_gpu], file, indent = 4)
def cpu_json():
    cpus = []
    cpus.append(CPU("Core i3-9350KF", "Intel", 530, "95", "i3-9350", "LGA 1151", 2019, "UHD Graphics 610", 4.00))
    cpus.append(CPU("Ryzen 9 3900X", "AMD", 990, "105", "3900X", "AM4", 2019, "Nu", 3.8))
    cpus.append(CPU("Ryzen 5 1600", "AMD", 500, "65", "1600", "AM4", 2017, "Nu", 3.2))
    cpus.append(CPU("Core i9-9900K", "Intel", 1500, "95", "i9-9900", "LGA 1151", 2019, "UHD Graphics 630", 3.6))
    cpus.append(CPU("Core i5-9400F", "Intel", 500, "65", "i5-9400", "LGA 1151", 2018, "UHD Graphics 630", 2.9))
    cpus.append(CPU("Core i7-9700K", "Intel", 1100, "95", "i7-9700", "LGA 1151", 2019, "UHD Graphics 630", 3.6))
    cpus.append(CPU("Core i5-10400", "Intel", 600, "65", "i5-10400", "LGA 1200", 2020, "UHD Graphics 630", 2.9))
    cpus.append(CPU("Ryzen 5 3600X", "AMD", 500, "95", "3600X", "AM4", 2019, "Nu", 3.8))
    cpus.append(CPU("Ryzen 7 1700X", "AMD", 700, "95", "1700X", "AM4", 2017, "Nu", 3.4))
    cpus.append(CPU("Ryzen 5 3500X", "AMD", 300, "65", "3500X", "AM4", 2019, "Nu", 3.6))
    cpus.append(CPU("Ryzen 7 3700X", "AMD", 900, "65", "3700X", "AM4", 2019, "Nu", 3.6))
    cpus.append(CPU("Ryzen 5 3400G", "AMD", 500, "65", "3400G", "AM4", 2019, "Radeon Vega 11", 3.7))
    cpus.append(CPU("Core i5 8400", "Intel", 600, "65", "i5-8400", "LGA 1151", 2018, "UHD Graphics 630", 2.8))
    cpus.append(CPU("Ryzen 5 1600AF", "AMD", 400, "65", "1600AF", "AM4", 2019, "Nu", 3.2))
    cpus.append(CPU("Core i9-9900KF", "Intel", 1400, "95", "i9-9900", "LGA 1151", 2019, "Nu", 3.6))
    cpus.append(CPU("Ryzen 3 3200G", "AMD", 400, "65", "3200G", "AM4", 2019, "Radeon Vega 8", 3.6))
    cpus.append(CPU("Ryzen 7 2700X", "AMD", 800, "105", "2700X", "AM4", 2018, "Nu", 3.7))
    cpus.append(CPU("Ryzen 5 2600", "AMD", 300, "65", "2600", "AM4", 2018, "Nu", 3.4))
    cpus.append(CPU("Ryzen 5 3600", "AMD", 500, "65", "3600", "AM4", 2019, "Nu", 3.6))
    cpus.append(CPU("Ryzen 9 5900X", "AMD", 1400, "105", "5900X", "AM4", 2020, "Nu", 3.7))
    cpus.append(CPU("Ryzen 5 3500", "AMD", 300, "65", "3500", "AM4", 2019, "Nu", 3.6))
    cpus.append(CPU("Ryzen 5 1600X", "AMD", 400, "95", "1600X", "AM4", 2017, "Nu", 3.6))
    cpus.append(CPU("Core i7-9700KF", "Intel", 1100, "95", "i7-9700", "LGA 1151", 2019, "Nu", 3.6))
    cpus.append(CPU("Ryzen 5 2400G", "AMD", 350, "45", "2400G", "AM4", 2018, "Radeon Vega 11", 3.6))
    cpus.append(CPU("Core i7-7800X", "Intel", 500, "140", "i7-7800", "LGA 2066", 2017, "Nu", 3.5))
    cpus.append(CPU("Ryzen 9 3950X", "AMD", 1650, "105", "3950X", "AM4", 2019, "Nu", 3.5))
    cpus.append(CPU("Ryzen 3 3100", "AMD", 200, "65", "3100", "AM4", 2020, "Nu", 3.6))
    cpus.append(CPU("Ryzen 5 3400GE", "AMD", 450, "35", "3400GE", "AM4", 2019, "Radeon Vega 11", 3.3))
    cpus.append(CPU("Ryzen 3 3200GE", "AMD", 300, "35", "3200GE", "AM4", 2019, "Radeon Vega 8", 3.2))

    with open('cpu.json', 'w', encoding='utf-8') as f:
        json.dump([ob.__dict__ for ob in cpus], f, indent=4)
def carcasa_json():
    carcase = []
    carcase.append(CARCASA("SilentiumPC Regnum RG4T", "Silentium", 299, 0, 1, False, 2, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Aerocool Project 7 P7C0", "Aerocool", 330, 0, 2, True, 2, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Cooler Master MasterBox MB500", "Cooler Master", 300, 0, 3, False, 2, 0.5, "Midi Tower"))
    carcase.append(CARCASA("SilentiumPC Regnum RG4T", "Silentium", 319, 0, 4, True, 3, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Aerocool P7-C1", "Aerocool", 400, 0, 5, True, 3, 0.4, "Midi Tower"))
    carcase.append(CARCASA("Aerocool Aero-700", "Aerocool", 200, 0, 6, False, 2, 0.2, "Midi Tower"))
    carcase.append(CARCASA("Cooler Master MasterBox MB600L", "Cooler Master", 230, 0, 7, False, 3, 0.4, "Midi Tower"))
    carcase.append(CARCASA("Aerocool P7-C1", "Aerocool", 350, 0, 8, False, 2, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Cooler Master MasterBox MB500", "Cooler Master", 270, 0, 9, True, 2, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Aerocool Aero-500", "Aerocool", 330, 0, 10, True, 2, 0.4, "Midi Tower"))
    carcase.append(CARCASA("Fractal Design Define S2", "Fractal Design", 500, 0, 11, True, 3, 0.4, "Midi Tower"))
    carcase.append(CARCASA("SilentiumPC Regnum RG4T", "Silentium", 250, 0, 12, False, 3, 0.4, "Midi Tower"))
    carcase.append(CARCASA("Aerocool P7-C1", "Aerocool", 280, 0, 13, True, 3, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Cooler Master MasterCase H500M", "Cooler Master", 650, 0, 14, False, 3, 0.5, "Full Tower"))
    carcase.append(CARCASA("Aerocool P7-C1", "Aerocool", 430, 0, 15, False, 2, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Cooler Master MasterBox MB500", "Cooler Master", 320, 0, 16, True, 2, 0.4, "Midi Tower"))
    carcase.append(CARCASA("Aerocool Aero-500", "Aerocool", 270, 0, 17, False, 2, 0.4, "Midi Tower"))
    carcase.append(CARCASA("Fractal Design Define S2", "Fractal Design", 450, 0, 18, True, 3, 0.4, "Midi Tower"))
    carcase.append(CARCASA("SilentiumPC Regnum RG4T", "Silentium", 290, 0, 19, False, 2, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Aerocool Project 7 P7C0", "Aerocool", 400, 0, 20, False, 2, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Cooler Master MasterBox MB500", "Cooler Master", 350, 0, 21, True, 2, 0.5, "Midi Tower"))
    carcase.append(CARCASA("SilentiumPC Regnum RG4T", "Silentium", 340, 0, 22, False, 3, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Aerocool P7-C1", "Aerocool", 320, 0, 23, True, 3, 0.4, "Midi Tower"))
    carcase.append(CARCASA("Aerocool Aero-700", "Aerocool", 310, 0, 24, False, 2, 0.2, "Midi Tower"))
    carcase.append(CARCASA("Cooler Master MasterBox MB600L", "Cooler Master", 270, 0, 25, False, 3, 0.4, "Midi Tower"))
    carcase.append(CARCASA("Aerocool P7-C1", "Aerocool", 390, 0, 26, False, 2, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Cooler Master MasterBox MB500", "Cooler Master", 310, 0, 27, True, 2, 0.3, "Midi Tower"))
    carcase.append(CARCASA("Aerocool Aero-500", "Aerocool", 350, 0, 28, True, 2, 0.4, "Midi Tower"))
    carcase.append(CARCASA("Fractal Design Define S2", "Fractal Design", 480, 0, 29, True, 3, 0.4, "Midi Tower"))
    carcase.append(CARCASA("SilentiumPC Regnum RG4T", "Silentium", 290, 0, 30, False, 3, 0.4, "Midi Tower"))
    with open('carcase.json', 'w') as f:
        json.dump([c.__dict__ for c in carcase], f, indent=4)
def placa_de_baza_json():
    placi_de_baza = []

    placi_de_baza.append(PLACA_DE_BAZA("P8Z77-V LX", "ASUS", 599, 40, 1, 0,  "IEEE 802.11a/b/g/n/ac",
                                       "Realtek ALC887 8-Channel High Definition Audio CODEC", 6, 1, 1, "LGA 1155",
                                       "DDR3", 16))
    placi_de_baza.append(PLACA_DE_BAZA("A320M-A PRO MAX", "MSI", 379, 28, 2, 0,  "Realtek 8111H Gigabit LAN",
                                       "Realtek ALC887 8-Channel High Definition Audio CODEC", 6, 0, 1, "AM4", "DDR4",
                                       32))
    placi_de_baza.append(PLACA_DE_BAZA("B450M-A PRO MAX", "MSI", 419, 31, 3, 0,  "Realtek 8118 Gaming LAN",
                                       "Realtek ALC892 7.1-Channel High Definition Audio CODEC", 6, 0, 1, "AM4", "DDR4",
                                       64))
    placi_de_baza.append(PLACA_DE_BAZA("B450 GAMING PLUS MAX", "MSI", 439, 32, 4, 1,  "Realtek 8111H Gigabit LAN",
                                       "Realtek ALC892 7.1-Channel High Definition Audio CODEC", 6, 1, 1, "AM4", "DDR4",
                                       32))
    placi_de_baza.append(PLACA_DE_BAZA("GA-H81M-S2H", "Gigabyte", 299, 30, 5, 0, "Realtek GbE LAN chip",
                                       "Realtek ALC887 8-Channel High Definition Audio CODEC", 6, 0, 0, "LGA 1150",
                                       "DDR3", 16))
    placi_de_baza.append(PLACA_DE_BAZA("Z97-P", "ASUS", 499, 32, 6, 1,  "Intel I218V Gigabit LAN",
                                       "Realtek ALC887 8-Channel High Definition Audio CODEC", 6, 0, 1, "LGA 1150",
                                       "DDR3", 32))
    placi_de_baza.append(PLACA_DE_BAZA("H370 GAMING PRO CARBON", "MSI", 569, 29, 7, 0,  "Intel I219V Gigabit LAN",
                                       "Realtek ALC892 7.1-Channel High Definition Audio CODEC", 6, 1, 1, "LGA 1151",
                                       "DDR4", 64))
    placi_de_baza.append(PLACA_DE_BAZA("Z170A GAMING M7", "MSI", 759, 38, 8, 1,  "Killer E2400 Gigabit LAN",
                                       "Realtek ALC1150 8-Channel High Definition Audio CODEC", 6, 1, 1, "LGA 1151",
                                       "DDR4", 32))
    placi_de_baza.append(PLACA_DE_BAZA("X570 GAMING X", "MSI", 799, 40, 9, 1,  "Realtek RTL8125B 2.5G LAN",
                                       "Realtek ALC1220 7.1-Channel High Definition Audio CODEC", 8, 1, 1, "AM4",
                                       "DDR4", 64))
    placi_de_baza.append(PLACA_DE_BAZA("X99-DELUXE II", "ASUS", 1099, 30, 10, 0,  "Intel I218-V Gigabit LAN",
                                       "Realtek ALC1150 8-Channel High Definition Audio CODEC", 6, 0, 1, "LGA 2011",
                                       "DDR4", 32))
    placi_de_baza.append(
        PLACA_DE_BAZA("X299 GAMING PRO CARBON AC", "MSI", 1299, 34, 11, 0,  "Killer E2500 Gigabit LAN",
                      "Realtek ALC1220 7.1-Channel High Definition Audio CODEC", 6, 1, 1, "LGA 2066", "DDR4", 64))
    placi_de_baza.append(PLACA_DE_BAZA("H310M-A PRO MAX", "MSI", 179, 23, 12, 0,  "Realtek 8111H Gigabit LAN",
                                       "Realtek ALC887 8-Channel High Definition Audio CODEC", 6, 0, 1, "LGA 1151",
                                       "DDR4", 16))
    placi_de_baza.append(PLACA_DE_BAZA("B360M-A PRO", "MSI", 299, 28, 13, 1,  "Realtek 8111H Gigabit LAN",
                                       "Realtek ALC892 7.1-Channel High Definition Audio CODEC", 6, 0, 1, "LGA 1151",
                                       "DDR4", 32))
    placi_de_baza.append(PLACA_DE_BAZA("Z390 GAMING X", "MSI", 799, 38, 14, 0,  "Realtek 8118 Gaming LAN",
                                       "Realtek ALC1220 7.1-Channel High Definition Audio CODEC", 6, 1, 1, "LGA 1151",
                                       "DDR4", 64))
    placi_de_baza.append(PLACA_DE_BAZA("X299 AORUS XTREME", "Gigabyte", 1669, 48, 15, 1,  "Intel I211-AT Gigabit LAN",
                                       "Realtek ALC1220 7.1-Channel High Definition Audio CODEC", 8, 1, 1, "LGA 2066",
                                       "DDR4", 64))
    placi_de_baza.append(PLACA_DE_BAZA("X570 AORUS MASTER", "Gigabyte", 1399, 42, 16, 0,  "Intel I211-AT Gigabit LAN",
                                       "Realtek ALC1220 7.1-Channel High Definition Audio CODEC", 8, 1, 1, "AM4",
                                       "DDR4", 64))
    placi_de_baza.append(PLACA_DE_BAZA("B450I GAMING PLUS AC", "MSI", 459, 32, 17, 1,  "Realtek 8111H Gigabit LAN",
                                       "Realtek ALC892 7.1-Channel High Definition Audio CODEC", 6, 1, 1, "AM4", "DDR4",
                                       32))
    placi_de_baza.append(PLACA_DE_BAZA("B365M GAMING HD", "MSI", 299, 28, 18, 0,  "Realtek 8111H Gigabit LAN",
                                       "Realtek ALC892 7.1-Channel High Definition Audio CODEC", 6, 0, 1, "LGA 1151",
                                       "DDR4", 32))
    placi_de_baza.append(PLACA_DE_BAZA("B550M-A PRO", "MSI", 499, 32, 19, 1,  "Realtek 8111H Gigabit LAN",
                                       "Realtek ALC892 7.1-Channel High Definition Audio CODEC", 6, 0, 1, "AM4", "DDR4",
                                       64))
    placi_de_baza.append(PLACA_DE_BAZA("X299 DESIGNARE EX", "Gigabyte", 1499, 42, 20, 0,  "Intel I219LM Gigabit LAN",
                                       "Realtek ALC1220 7.1-Channel High Definition Audio CODEC", 8, 1, 1, "LGA 2066",
                                       "DDR4", 64))
    placi_de_baza.append(PLACA_DE_BAZA("Z390 AORUS ULTRA", "Gigabyte", 899, 38, 21, 1, "Intel I219V Gigabit LAN",
                                       "Realtek ALC1220 7.1-Channel High Definition Audio CODEC", 8, 1, 1, "LGA 1151",
                                       "DDR4", 64))
    placi_de_baza.append(PLACA_DE_BAZA("B460M MORTAR WI-FI", "MSI", 659, 30, 22, 0,  "Intel Wi-Fi 6 AX200",
                                       "Realtek ALC1220 7.1-Channel High Definition Audio CODEC", 6, 1, 1, "LGA 1200",
                                       "DDR4", 64))
    placi_de_baza.append(PLACA_DE_BAZA("X570 AORUS ULTRA", "Gigabyte", 1299, 42, 23, 1,  "Intel I211-AT Gigabit LAN",
                                       "Realtek ALC1220 7.1-Channel High Definition Audio CODEC", 8, 1, 1, "AM4",
                                       "DDR4", 64))
    placi_de_baza.append(PLACA_DE_BAZA("X299 AORUS ELITE", "Gigabyte", 1199, 38, 24, 0,  "Intel I219V Gigabit LAN",
                                       "Realtek ALC1220 7.1-Channel High Definition Audio CODEC", 8, 1, 1, "LGA 2066",
                                       "DDR4", 32))
    placi_de_baza.append(PLACA_DE_BAZA("H370M D3H", "Gigabyte", 369, 25, 25, 1,  "Realtek GbE LAN chip",
                                       "Realtek ALC887 8-Channel High Definition Audio CODEC", 6, 0, 0, "LGA 1151",
                                       "DDR4", 16))
    with open('placi_de_baza.json', 'w') as f:
        json.dump([c.__dict__ for c in placi_de_baza], f, indent=4)
