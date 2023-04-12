import random
import time
import tkinter
import socket
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from os.path import basename

from Functii import *
from PIL import Image
import customtkinter
import smtplib
from email.message import EmailMessage
import ssl
from email.mime.text import MIMEText
from string import Template
import string
import pygame
from COMPONENTE import *
from CONFIGURATIE import *
import webbrowser
import os

surse_json()
stocari_json()
ram_json()
gpu_json()
cpu_json()
carcasa_json()
placa_de_baza_json()

ok = 1
score = 60
limit = 0
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"


# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
# Designing window for login
def log(fereastra):
    width = 1000
    height = 720
    global code
    code = None
    global score_label
    global textbox_f3
    global total_f3
    global consum_f3

    def delete_password_not_recognised():
        password_not_recog_screen.destroy()

    def delete_user_not_found_screen():
        user_not_found_screen.destroy()

    def user_not_found():
        global user_not_found_screen
        user_not_found_screen = customtkinter.CTkToplevel(login_screen)
        user_not_found_screen.title("Upss...")
        user_not_found_screen.geometry("250x100")
        play_music('sounds/error1.mp3')
        customtkinter.CTkLabel(user_not_found_screen, text="User Not Found").pack()
        customtkinter.CTkButton(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

    # Designing popup for login invalid password
    def password_not_recognised():
        global password_not_recog_screen
        password_not_recog_screen = customtkinter.CTkToplevel(login_screen)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        play_music('sounds/error1.mp3')
        customtkinter.CTkLabel(password_not_recog_screen, text="Invalid Password ").pack()
        customtkinter.CTkButton(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

    # Designing popup for login success
    def login_success():
        login_frame.grid_forget()  # remove login frame
        main_frame.grid(row=0, column=0, sticky='nsew', padx=50)
        main_frame1.grid(row=0, column=0, sticky="nsew", padx=10)  # show main frame
        main_frame2.grid(row=0, column=1, sticky="nsew", padx=10)

    def login_verify():
        username1 = username_entry.get()
        password1 = password_entry.get()

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify or code == password1:
                login_success()

            else:
                password_not_recognised()

        else:
            user_not_found()

    def back_event1():
        main_frame.grid_forget()
        main_frame1.grid_forget()  # remove main frame
        main_frame2.grid_forget()
        main_frame3.grid_forget()
        login_frame.grid(row=0, column=0, sticky="ns")  # show login frame

    def back_event2():
        main_frame3.grid_forget()  # show login frame
        main_frame.grid(row=0, column=0, sticky='nsew', padx=50)
        main_frame1.grid(row=0, column=0, sticky="nsew", padx=10)  # show main frame
        main_frame2.grid(row=0, column=1, sticky="nsew", padx=10)

    def next_event():
        main_frame.grid_forget()
        main_frame1.grid_forget()  # remove main frame
        main_frame2.grid_forget()
        main_frame3.grid(row=0, column=0, sticky="nsew", padx=100)  # show login frame
        if round(total_scor(), 2) == 0:
            score_label.configure(
                text="Score: " + str(round(total_scor(), 2)) + " (it is 0 because the sistem is incomplete)")
        else:
            score_label.configure(
                text="Score: " + str(round(total_scor(), 2)))
        text_f3_update()
        total_f3.configure(text="Total: " + str(pret_total()) + " RON")
        consum_f3.configure(text="Total system power requirements: " + str(total_consum()) + "W")

    global login_screen
    global login_frame
    login_screen = customtkinter.CTkToplevel(fereastra)
    login_screen.title("The Components page")
    login_screen.geometry(f"{width}x{height}")
    login_screen.resizable(False, False)
    # load and create background image
    # current_path = os.path.dirname(os.path.realpath(__file__))
    bg_image = customtkinter.CTkImage(light_image=Image.open("bg_gradient.jpg"),
                                      dark_image=Image.open("bg_gradient.jpg"),
                                      size=(width, height))
    bg_image_label = customtkinter.CTkLabel(login_screen, image=bg_image)
    bg_image_label.grid(row=0, column=0)

    # create login frame
    login_frame = customtkinter.CTkFrame(login_screen, corner_radius=0)
    login_frame.grid(row=0, column=0, sticky="ns")
    login_label = customtkinter.CTkLabel(login_frame, text="Make your perfect build\nLogin Page",
                                         font=customtkinter.CTkFont(size=20, weight="bold"))
    login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
    username_entry = customtkinter.CTkEntry(login_frame, width=200, placeholder_text="username")
    username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
    password_entry = customtkinter.CTkEntry(login_frame, width=200, show="*", placeholder_text="password")
    password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
    login_button = customtkinter.CTkButton(login_frame, text="Login", command=login_verify, width=200)
    login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    def parola_email():
        global code
        dialog = customtkinter.CTkInputDialog(text="We will send you an email\nType your username:", title="Forgot password")
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

        username = dialog.get_input()
        list_of_files = os.listdir()
        if username in list_of_files:
            file1 = open(username, "r")
            verify = file1.read().splitlines()
            email = verify[2]

            trimite_email_parola(email, code)
        else:
            user_not_found()

    button_T = customtkinter.CTkButton(master=login_frame,
                                       width=120,
                                       height=32,
                                       border_width=0,
                                       corner_radius=8,
                                       text="Forgot password",
                                       command=parola_email,
                                       fg_color='transparent', text_color=("#1A8C52", "#FFFFFF"))
    button_T.grid(row=4, column=0, padx=10, pady=10)

    # create main frame
    main_frame = customtkinter.CTkFrame(login_screen, corner_radius=0)
    main_frame1 = customtkinter.CTkFrame(main_frame, corner_radius=0)
    main_frame2 = customtkinter.CTkFrame(main_frame, corner_radius=0)
    main_frame3 = customtkinter.CTkFrame(login_screen, corner_radius=0)
    main_frame3.grid_forget()
    # main_frame1.grid_columnconfigure(0,weight=1)
    # main_frame2.grid_columnconfigure(1,weight=1)

    main_label = customtkinter.CTkLabel(main_frame1, text="Make your perfect build\nMain Page",
                                        font=customtkinter.CTkFont(size=20, weight="bold"))
    main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
    back_button1 = customtkinter.CTkButton(main_frame, text="Back", command=back_event1, width=200)
    back_button1.grid(row=1, column=0, padx=30, pady=(15, 15))

    next_button = customtkinter.CTkButton(main_frame, text="Next", command=next_event, width=200, state="disabled")
    next_button.grid(row=1, column=1, padx=30, pady=(15, 15))

    global textbox
    global warning_box
    global total_label
    global checkbox

    global cpu_o
    global placa_de_baza_o
    global gpu_o
    global sursa_o
    global stocare_o
    global carcasa_o
    global ram_o
    global avertizari

    cpu_o = None
    placa_de_baza_o = None
    gpu_o = None
    sursa_o = None
    stocare_o = None
    carcasa_o = None
    ram_o = None
    avertizari = None

    def text_box():
        global textbox
        text_label = customtkinter.CTkLabel(main_frame2, text="Information about\ncomponent",
                                            font=customtkinter.CTkFont(size=10, weight="bold"))
        text_label.grid(row=0, column=0, padx=10)
        textbox = customtkinter.CTkTextbox(main_frame2, width=350, height=300, font=("Sistem", 14))
        textbox.grid(row=1, column=0, padx=30, pady=(10, 15))
        textbox.insert("0.0", "Hello, have fun with us")  # insert at line 0 character 0
        # text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
        textbox.configure(state="disabled")

    def warnings_text_box():
        global warning_box
        text_label = customtkinter.CTkLabel(main_frame2, text=" Warnings",
                                            font=customtkinter.CTkFont(size=14, weight="bold"))
        text_label.grid(row=3, column=0, padx=10)
        warning_box = customtkinter.CTkTextbox(main_frame2, width=300, height=200, font=("Sistem", 14),
                                               fg_color=('#DE3163', '#8F0029'), )
        warning_box.grid(row=4, column=0, padx=30, pady=(10, 15))
        warning_box.insert("0.0", "Warning messages will appear here")  # insert at line 0 character 0
        # text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
        warning_box.configure(state="disabled")

    def combo_placadebaza():
        # combobox placa de baza
        placa_label = customtkinter.CTkLabel(main_frame1, text="Motherboard",
                                             font=customtkinter.CTkFont(size=10, weight="bold"))
        placa_label.grid(row=2, column=0, padx=10)
        combobox_var = customtkinter.StringVar(value="No")  # set initial value
        with open('placi_de_baza.json', 'r') as f:
            date_placi_de_baza = json.load(f)
        placi_de_baza = []

        for placa in date_placi_de_baza:
            placa_de_baza = PLACA_DE_BAZA(placa["nume"], placa["firma"], placa["pret"], placa["consum"], placa["id"],
                                          placa["slot_m2"], placa["placa_retea"], placa["placa_sunet"], placa["nr_usb"],
                                          placa["display_port"], placa["hdmi"], placa["socket"], placa["versiune_ddr"],
                                          placa["capacitate_ram"])
            placi_de_baza.append(placa_de_baza)
        list_placi = [placa.getnume() for placa in placi_de_baza]

        def search(event):
            value = event.widget.get()
            print(value)
            if value == '':
                combobox.configure(values=list_placi)
            else:
                data = []
                for item in list_placi:
                    if value.lower() in item.lower():
                        data.append(item)
                combobox.configure(values=data)

        def combobox_callback(choice):
            global placa_de_baza_o
            if (choice == "No"):

                placa_de_baza_o = "No"
                # print(placa_de_baza_o)
                avertizariii()
            for i in placi_de_baza:
                if (i.getnume() == choice):
                    textbox.configure(state="normal")
                    textbox.delete("0.0", "end")
                    textbox.insert("0.0", i)
                    textbox.configure(state="disabled")
                    placa_de_baza_o = i
                    # print(placa_de_baza_o)
                    avertizariii()

        list_placi.insert(0, "No")
        combobox = customtkinter.CTkComboBox(master=main_frame1,
                                             width=290,
                                             values=list_placi,
                                             command=combobox_callback,
                                             font=("Sistem", 13),
                                             dropdown_font=("Sistem", 13),
                                             variable=combobox_var)
        combobox.grid(row=3, column=0, padx=20, pady=2)
        combobox.bind('<KeyRelease>', search)

    def combo_cpu():
        # combobox placa de baza
        placa_label = customtkinter.CTkLabel(main_frame1, text="CPU",
                                             font=customtkinter.CTkFont(size=10, weight="bold"))
        placa_label.grid(row=4, column=0, padx=10)
        combobox_var = customtkinter.StringVar(value="No")  # set initial value
        with open('cpu.json', 'r') as f:
            date_cpu = json.load(f)
        cpus = []
        for cpu in date_cpu:
            cpu = CPU(cpu["nume"], cpu["firma"], cpu["pret"], cpu["consum"], cpu["id"],
                      cpu["socket"], cpu["an"], cpu["gpu"], cpu["frecventa"])
            cpus.append(cpu)
        list_cpus = [cpu.getnume() for cpu in cpus]

        def search(event):
            value = event.widget.get()
            print(value)
            if value == '':
                combobox.configure(values=list_cpus)
            else:
                data = []
                for item in list_cpus:
                    if value.lower() in item.lower():
                        data.append(item)
                combobox.configure(values=data)

        def combobox_callback(choice):
            global cpu_o
            if (choice == "No"):
                cpu_o = "No"
                # print(placa_de_baza_o)
                avertizariii()
            for i in cpus:
                if (i.getnume() == choice):
                    textbox.configure(state="normal")
                    textbox.delete("0.0", "end")
                    textbox.insert("0.0", i)
                    textbox.configure(state="disabled")

                    cpu_o = i
                    # print(cpu_o)
                    avertizariii()

        list_cpus.insert(0, "No")
        combobox = customtkinter.CTkComboBox(master=main_frame1,
                                             width=290,
                                             values=list_cpus,
                                             command=combobox_callback,
                                             font=("Sistem", 13),
                                             dropdown_font=("Sistem", 13),
                                             variable=combobox_var)
        combobox.grid(row=5, column=0, padx=20, pady=2)
        combobox.bind('<KeyRelease>', search)

    def combo_carcasa():
        # combobox placa de baza
        placa_label = customtkinter.CTkLabel(main_frame1, text="Case",
                                             font=customtkinter.CTkFont(size=10, weight="bold"))
        placa_label.grid(row=6, column=0, padx=10)
        combobox_var = customtkinter.StringVar(value="No")  # set initial value
        with open('carcase.json', 'r') as f:
            date_carcase = json.load(f)
        dict = []
        for carcasa in date_carcase:
            carcasa = CARCASA(carcasa["nume"], carcasa["firma"], carcasa["pret"], carcasa["consum"], carcasa["id"],
                              carcasa["panou_sticla"], carcasa["ventilatoare"], carcasa["capacitate"], carcasa["tip"])
            dict.append(carcasa)
        list = [carcasa.getnume() for carcasa in dict]

        def search(event):
            value = event.widget.get()
            print(value)
            if value == '':
                combobox.configure(values=list)
            else:
                data = []
                for item in list:
                    if value.lower() in item.lower():
                        data.append(item)
                combobox.configure(values=data)

        def combobox_callback(choice):
            global carcasa_o
            if (choice == "No"):
                carcasa_o = "No"
                # print(placa_de_baza_o)
                avertizariii()
            for i in dict:
                if (i.getnume() == choice):
                    textbox.configure(state="normal")
                    textbox.delete("0.0", "end")
                    textbox.insert("0.0", i)
                    textbox.configure(state="disabled")

                    carcasa_o = i
                    avertizariii()

        list.insert(0, "No")
        combobox = customtkinter.CTkComboBox(master=main_frame1,
                                             width=290,
                                             values=list,
                                             command=combobox_callback,
                                             font=("Sistem", 13),
                                             dropdown_font=("Sistem", 13),
                                             variable=combobox_var)
        combobox.grid(row=7, column=0, padx=20, pady=2)
        combobox.bind('<KeyRelease>', search)

    def combo_gpu():
        # combobox placa de baza
        placa_label = customtkinter.CTkLabel(main_frame1, text="GPU",
                                             font=customtkinter.CTkFont(size=10, weight="bold"))
        placa_label.grid(row=8, column=0, padx=10)
        combobox_var = customtkinter.StringVar(value="No")  # set initial value
        with open('gpu.json', 'r') as f:
            date_gpus = json.load(f)
        dict = []
        for gpu in date_gpus:
            gpu = GPU(gpu["nume"], gpu["firma"], gpu["pret"], gpu["consum"], gpu["id"], gpu["an"])
            dict.append(gpu)
        list = [gpu.getnume() for gpu in dict]

        def search(event):
            value = event.widget.get()
            print(value)
            if value == '':
                combobox.configure(values=list)
            else:
                data = []
                for item in list:
                    if value.lower() in item.lower():
                        data.append(item)
                combobox.configure(values=data)

        def combobox_callback(choice):
            global gpu_o
            if (choice == "No"):
                gpu_o = "No"
                # print(placa_de_baza_o)
                avertizariii()
            for i in dict:
                if (i.getnume() == choice):
                    textbox.configure(state="normal")
                    textbox.delete("0.0", "end")
                    textbox.insert("0.0", i)
                    textbox.configure(state="disabled")
                    gpu_o = i
                    avertizariii()

        list.insert(0, "No")
        combobox = customtkinter.CTkComboBox(master=main_frame1,
                                             width=290,
                                             values=list,
                                             command=combobox_callback,
                                             font=("Sistem", 13),
                                             dropdown_font=("Sistem", 13),
                                             variable=combobox_var)
        combobox.grid(row=9, column=0, padx=20, pady=2)
        combobox.bind('<KeyRelease>', search)

    def combo_ram():
        # combobox placa de baza
        placa_label = customtkinter.CTkLabel(main_frame1, text="RAM",
                                             font=customtkinter.CTkFont(size=10, weight="bold"))
        placa_label.grid(row=10, column=0, padx=10)
        combobox_var = customtkinter.StringVar(value="No")  # set initial value
        with open('ram.json', 'r') as f:
            date_ram = json.load(f)
        dict = []
        for ram in date_ram:
            ram = RAM(ram["nume"], ram["firma"], ram["pret"], ram["consum"], ram["id"], ram["versiune_ddr"],
                      ram["capacitate"], ram["viteza"], ram["frecventa"])
            dict.append(ram)
        list = [ram.getnume() for ram in dict]

        def search(event):
            value = event.widget.get()
            print(value)
            if value == '':
                combobox.configure(values=list)
            else:
                data = []
                for item in list:
                    if value.lower() in item.lower():
                        data.append(item)
                combobox.configure(values=data)

        def combobox_callback(choice):
            global ram_o
            if (choice == "No"):
                ram_o = "No"
                # print(placa_de_baza_o)
                avertizariii()
            for i in dict:
                if (i.getnume() == choice):
                    textbox.configure(state="normal")
                    textbox.delete("0.0", "end")
                    textbox.insert("0.0", i)
                    textbox.configure(state="disabled")
                    ram_o = i
                    avertizariii()

        list.insert(0, "No")
        combobox = customtkinter.CTkComboBox(master=main_frame1,
                                             width=290,
                                             values=list,
                                             command=combobox_callback,
                                             font=("Sistem", 13),
                                             dropdown_font=("Sistem", 13),
                                             variable=combobox_var)
        combobox.grid(row=11, column=0, padx=20, pady=2)
        combobox.bind('<KeyRelease>', search)

    def combo_stocare():
        # combobox placa de baza
        placa_label = customtkinter.CTkLabel(main_frame1, text="Storage",
                                             font=customtkinter.CTkFont(size=10, weight="bold"))
        placa_label.grid(row=12, column=0, padx=10)
        combobox_var = customtkinter.StringVar(value="No")  # set initial value
        with open('stocare.json', 'r') as f:
            date_stocare = json.load(f)
        dict = []
        for stocare in date_stocare:
            stocare = STOCARE(stocare["nume"], stocare["firma"], stocare["pret"], stocare["consum"], stocare["id"],
                              stocare["viteza_scriere"], stocare["viteza_citire"], stocare["capacitate"],
                              stocare["tip"])
            dict.append(stocare)
        list = [stocare.getnume() for stocare in dict]

        def search(event):
            value = event.widget.get()
            print(value)
            if value == '':
                combobox.configure(values=list)
            else:
                data = []
                for item in list:
                    if value.lower() in item.lower():
                        data.append(item)
                combobox.configure(values=data)

        def combobox_callback(choice):
            global stocare_o
            if (choice == "No"):
                stocare_o = "No"
                # print(placa_de_baza_o)
                avertizariii()
            for i in dict:
                if (i.getnume() == choice):
                    textbox.configure(state="normal")
                    textbox.delete("0.0", "end")
                    textbox.insert("0.0", i)
                    textbox.configure(state="disabled")
                    stocare_o = i
                    avertizariii()

        list.insert(0, "No")
        combobox = customtkinter.CTkComboBox(master=main_frame1,
                                             width=290,
                                             values=list,
                                             command=combobox_callback,
                                             font=("Sistem", 13),
                                             dropdown_font=("Sistem", 13),
                                             variable=combobox_var)
        combobox.grid(row=13, column=0, padx=20, pady=2)
        combobox.bind('<KeyRelease>', search)

    def combo_sursa():
        # combobox placa de baza

        placa_label = customtkinter.CTkLabel(main_frame1, text="Power supply",
                                             font=customtkinter.CTkFont(size=10, weight="bold"))
        placa_label.grid(row=14, column=0, padx=10)
        combobox_var = customtkinter.StringVar(value="No")  # set initial value
        with open('sursa.json', 'r') as f:
            date_sursa = json.load(f)
        dict = []
        for sursa in date_sursa:
            sursa = SURSA(sursa["nume"], sursa["firma"], sursa["pret"], sursa["consum"], sursa["id"], sursa["modulara"],
                          sursa["capacitate"], sursa["certificare"])
            dict.append(sursa)
        list = [sursa.getnume() for sursa in dict]

        def search(event):
            value = event.widget.get()
            print(value)
            if value == '':
                combobox.configure(values=list)
            else:
                data = []
                for item in list:
                    if value.lower() in item.lower():
                        data.append(item)
                combobox.configure(values=data)

        def combobox_callback(choice):
            global sursa_o
            if (choice == "No"):
                sursa_o = "No"
                # print(placa_de_baza_o)
                avertizariii()
            for i in dict:
                if (i.getnume() == choice):
                    textbox.configure(state="normal")
                    textbox.delete("0.0", "end")
                    textbox.insert("0.0", i)
                    textbox.configure(state="disabled")
                    sursa_o = i
                    avertizariii()

        list.insert(0, "No")
        combobox = customtkinter.CTkComboBox(master=main_frame1,
                                             width=290,
                                             values=list,
                                             command=combobox_callback,
                                             font=("Sistem", 13),
                                             dropdown_font=("Sistem", 13),
                                             variable=combobox_var)
        combobox.grid(row=15, column=0, padx=20, pady=2)
        combobox.bind('<KeyRelease>', search)

    def label_total():
        global total_label
        total_label = customtkinter.CTkLabel(main_frame1, text="Total: 0 RON",
                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        total_label.grid(row=16, column=0, padx=10, pady=20)

    def total_consum():
        totalconsum = 50
        if type(placa_de_baza_o) is PLACA_DE_BAZA:
            totalconsum += int(placa_de_baza_o.consum)
        if type(cpu_o) is CPU:
            totalconsum += int(cpu_o.consum)
        if type(carcasa_o) is CARCASA:
            totalconsum += int(carcasa_o.consum)
        if type(gpu_o) is GPU:
            totalconsum += int(gpu_o.consum)
        if type(ram_o) is RAM:
            totalconsum += int(ram_o.consum)
        if type(stocare_o) is STOCARE:
            totalconsum += int(stocare_o.consum)
        return totalconsum

    def pret_total():
        total = 0
        if type(placa_de_baza_o) is PLACA_DE_BAZA:
            total += int(placa_de_baza_o.pret)
        if type(cpu_o) is CPU:
            total += int(cpu_o.pret)
        if type(carcasa_o) is CARCASA:
            total += int(carcasa_o.pret)
        if type(gpu_o) is GPU:
            total += int(gpu_o.pret)
        if type(ram_o) is RAM:
            total += int(ram_o.pret)
        if type(stocare_o) is STOCARE:
            total += int(stocare_o.pret)
        return total

    def check_avertizari():
        global checkbox
        check_var = tkinter.StringVar()

        def checkbox_event():
            avertizariii()

        checkbox = customtkinter.CTkCheckBox(master=main_frame2, text="Ignore warnings", command=checkbox_event,
                                             variable=check_var, onvalue="on", offvalue="off")
        checkbox.grid(row=5, column=0, padx=20, pady=5)

    def total_scor():
        scor = 0
        if (type(placa_de_baza_o) is PLACA_DE_BAZA and type(cpu_o) is CPU and type(gpu_o) is GPU and type(
                carcasa_o) is CARCASA and type(sursa_o) is SURSA and type(stocare_o) is STOCARE and type(ram_o) is RAM):
            scor += placa_de_baza_o.scor()
            scor += cpu_o.scor()
            scor += gpu_o.scor() + carcasa_o.scor() + sursa_o.scor() + stocare_o.scor() + ram_o.scor()
        return scor

    def text_f3_update():
        textbox_f3.configure(state="normal")
        textbox_f3.delete("0.0", "end")
        if type(placa_de_baza_o) is PLACA_DE_BAZA:
            textbox_f3.insert("end", "            Motherboard\n" + str(placa_de_baza_o) + "\n\n")
        else:
            textbox_f3.insert("end", "            Motherboard\nNo\n\n")
        if type(cpu_o) is CPU:
            textbox_f3.insert("end", "            CPU\n" + str(cpu_o) + "\n\n")
        else:
            textbox_f3.insert("end", "            CPU\nNo\n\n")
        if type(carcasa_o) is CARCASA:
            textbox_f3.insert("end", "            Case\n" + str(carcasa_o) + "\n\n")
        else:
            textbox_f3.insert("end", "            Case\nNo\n\n")
        if type(gpu_o) is GPU:
            textbox_f3.insert("end", "            GPU\n" + str(gpu_o) + "\n\n")
        else:
            textbox_f3.insert("end", "            GPU\nNo\n\n")
        if type(ram_o) is RAM:
            textbox_f3.insert("end", "            RAM\n" + str(ram_o) + "\n\n")
        else:
            textbox_f3.insert("end", "            RAM\nNo\n\n")
        if type(stocare_o) is STOCARE:
            textbox_f3.insert("end", "            Storage\n" + str(stocare_o) + "\n\n")
        else:
            textbox_f3.insert("end", "            Storage\nNo\n\n")
        if type(sursa_o) is SURSA:
            textbox_f3.insert("end", "            Power supply\n" + str(sursa_o) + "\n\n")
        else:
            textbox_f3.insert("end", "        Power supply\nNo\n\n")
        textbox_f3.configure(state="disabled")

    def obiecte_main3():
        global score_label
        global textbox_f3
        global total_f3
        global consum_f3
        back_button2 = customtkinter.CTkButton(main_frame3, text="Back", command=back_event2, width=200)
        back_button2.place(relx=0.1, rely=0.9, anchor='sw')

        text_label = customtkinter.CTkLabel(main_frame3, text="Information about\nyour configuration",
                                            font=customtkinter.CTkFont(size=10, weight="bold"))
        text_label.pack(pady=10, padx=10)
        textbox_f3 = customtkinter.CTkTextbox(main_frame3, width=350, height=300, font=("Sistem", 14))
        textbox_f3.pack(pady=10, padx=10)
        text_f3_update()

        score_label = customtkinter.CTkLabel(main_frame3,
                                             text="Score: 0 (it is 0 because the sistem is incomplete)",
                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        score_label.pack(pady=5, padx=10)

        total_f3 = customtkinter.CTkLabel(main_frame3, text="Total: 0 RON",
                                          font=customtkinter.CTkFont(size=15, weight="bold"))
        total_f3.pack(pady=5, padx=10)

        consum_f3 = customtkinter.CTkLabel(main_frame3, text="Total system power requirements: 0 W",
                                           font=customtkinter.CTkFont(size=15, weight="bold"))
        consum_f3.pack(pady=5, padx=10)

        progressbar = customtkinter.CTkProgressBar(master=main_frame3, mode="indeterminate")
        progressbar.pack(padx=20, pady=10)
        progressbar.start()

        def trimite_conf(text):
            username = username_entry.get()
            list_of_files = os.listdir()
            if username in list_of_files:
                file1 = open(username, "r")
                verify = file1.read().splitlines()
                email = verify[2]
                trimite_configuratie(email, text)
            else:
                user_not_found()
            exceptie = customtkinter.CTkToplevel(main_frame3)
            exceptie.title("Succes")
            exceptie.resizable(False, False)
            exceptie.geometry("200x100")
            t=customtkinter.CTkLabel(exceptie, text="Email sent"
                                   )
            t.pack(padx=10, pady=10)
            customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)

        send_configuration = customtkinter.CTkButton(main_frame3, text="Send build on email",
                                                     command=lambda: trimite_conf(
                                                         textbox_f3.get("0.0", "end") + "\n" + score_label.cget(
                                                             "text") + "\n" + total_f3.cget(
                                                             "text") + "\n" + consum_f3.cget("text")), width=200)
        send_configuration.place(relx=0.9, rely=0.9, anchor='se')

    def avertizariii():
        total_label.configure(text="Total: " + str(pret_total()) + " RON")
        avertizari = ""
        x = 0
        if type(ram_o) is RAM and type(
                placa_de_baza_o) is PLACA_DE_BAZA and placa_de_baza_o.versiune_ddr != ram_o.versiune_ddr:
            avertizari = avertizari + "     The ddr version of the motherboard is not" + "\n compatible with the ram\n"
            x += 1
        if type(cpu_o) is CPU and type(
                placa_de_baza_o) is PLACA_DE_BAZA and placa_de_baza_o.socket != cpu_o.socket:
            avertizari = avertizari + "     The socket of motherboard is not\n compatible with cpu socket\n"
            x += 1
        if type(sursa_o) is SURSA and total_consum() > sursa_o.capacitate:
            avertizari = avertizari + "     The power supply you chosen is too weak. The deficit is of: " + str(
                sursa_o.capacitate - total_consum()) + "W\n"
            x += 1
        if type(stocare_o) is STOCARE and type(
                placa_de_baza_o) is PLACA_DE_BAZA and stocare_o.tip == "SSD" and placa_de_baza_o.slot_m2 == 0:
            avertizari = avertizari + "     The moterboard dont have M2\n slot for SSD\n"
            x += 1
        if type(placa_de_baza_o) is not PLACA_DE_BAZA or placa_de_baza_o == "No":
            avertizari = avertizari + "     Missing motherboard\n"
            x += 1
        if type(ram_o) is not RAM or ram_o == "No":
            avertizari = avertizari + "     Missing ram\n"
            x += 1
        if type(stocare_o) is not STOCARE or sursa_o == "No":
            avertizari = avertizari + "     Missing storage\n"
            x += 1
        if type(sursa_o) is not SURSA or sursa_o == "No":
            avertizari = avertizari + "     Missing power supply\n"
            x += 1
        if type(cpu_o) is not CPU or cpu_o == "No":
            avertizari = avertizari + "     Missing CPU\n"
            x += 1
        if type(carcasa_o) is not CARCASA or carcasa_o == "No":
            avertizari = avertizari + "     Missing Case\n"
            x += 1
        if type(cpu_o) is CPU and type(gpu_o) != GPU and cpu_o.gpu == "Nu" or gpu_o=="No":
            avertizari = avertizari + "     Missing GPU(dedicated or integrated)\n"
            x += 1
        avertizari = avertizari + "Total Warnings: " + str(x)
        if x == 0 or checkbox.get() == "on":
            next_button.configure(state="normal")
        else:
            print(checkbox.get())
            next_button.configure(state="disabled")
        warning_box.configure(state="normal")
        warning_box.delete("0.0", "end")
        warning_box.insert("0.0", avertizari)
        warning_box.configure(state="disabled")

    text_box()
    warnings_text_box()
    combo_placadebaza()
    combo_cpu()
    combo_carcasa()
    combo_gpu()
    combo_ram()
    combo_stocare()
    combo_sursa()
    label_total()
    check_avertizari()

    obiecte_main3()


def trimite_email_parola(catre, numar):
    email_sender = "build.pc.318@gmail.com"
    email_password = 'atydpcqtkqwtnjat'
    email_receiver = catre

    subiect = "Message for password"
    htm = """\
    <div>
  <div><!-- [if mso]>
    <noscript>
        <xml>
            <o:OfficeDocumentSettings>
                <o:AllowPNG/>
                <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
    </noscript>
    <![endif]--> <!-- [if lte mso 11]>
    <style type="text/css">
        .mj-outlook-group-fix { width:100% !important; }
    </style>
    <![endif]--></div>
</div>
<style>@media screen and (max-width: 359px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 300px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media screen and (min-width: 360px) and (max-width: 374px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 340px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media only screen and (min-width: 375px) and (max-width: 413px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 355px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media only screen and (min-width: 414px) and (max-width: 479px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 394px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media only screen and (min-width: 480px) and (max-width: 567px) {
  #logo-line {
    width: 440px !important;
    height: 5px !important;
  }
}
@media only screen and (min-width: 568px) and (max-width: 639px) {
  #logo-line {
    width: 528px !important;
    height: 5px !important;
  }
}
.button:hover {
  background-color: #2f82fb !important;
  color: #ffffff !important;
}
.button:active {
  background-color: #2872e0 !important;
  color: #ffffff !important;
}
.button.main:hover {
  background-color: #3c8cfc !important;
}
.button.main:active {
  background-color: #2872e0 !important;
}</style>
<div>
  <table style="border-spacing: 0px; margin: 0px; border-collapse: separate; border: 0px; max-width: 600px; font-family: Arial, Helvetica, 'sans-serif'; height: 334px;" border="0" cellspacing="0" cellpadding="0" align="left" bgcolor="#ffffff">
    <tbody>
      <tr style="height: 43px;">
        <td style="border-collapse: separate; margin: 0px; padding: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 43px; width: 600px;" align="left">
          <table id="logo-and-promo-text" style="border-spacing: 0px; border: 0px none; border-collapse: separate; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 501px; height: 104px;" border="0" cellspacing="0" cellpadding="0" align="left">
            <tbody>
              <tr>
                <td style="border-collapse: separate; padding: 0px 20px 0px 0px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 306px;">
                  <img style="height: 83px; display: inline-block; vertical-align: middle; padding: 0px;" src="https://share1.cloudhq-mkt3.net/a5d1450971468e.png" alt="Desktop" width="306" height="43" border="0">
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 16px; margin: 0px; font-size: 12px; line-height: 14px; color: #212121; font-weight: bold; vertical-align: middle; font-family: Arial, Helvetica, 'sans-serif'; width: 159px;" valign="middle">The way you can build your pc 
                  <img src="https://cdn.tiny.cloud/1/744os35bk6lfhnyx14onzpqa8er3gs4s21opocmie2wxar65/tinymce/4.9.11-104/plugins/emoticons/img/smiley-cool.gif" alt="cool">
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
      <tr style="height: 10px;">
        <td style="border-collapse: separate; padding: 0px; margin: 0px; line-height: 5px; font-family: Arial, Helvetica, 'sans-serif'; height: 10px; width: 600px;">
          <img id="logo-line" style="width: 600px; height: 5px; padding: 0px;" src="https://static.g2a.com/_/mail/g2a-line.png" width="600" height="5" border="0">
        </td>
      </tr>
      <tr style="height: 172px;">
        <td id="template-content" style="border-collapse: separate; padding: 30px 0px 0px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 172px; width: 600px;" align="left" valign="top">
          <h1 style="font-size: 20px; color: #000000; padding: 0; margin: 0 0 10px; font-weight: bold; line-height: 30px;">Email verification</h1>
          <div class="body-1" style="color: #000000; font-size: 16px; line-height: 24px; font-weight: normal; margin-bottom: 30px;">Email verification code is: $numar</div>
          <div class="body-1" style="color: #000000; font-size: 16px; line-height: 24px; font-weight: normal; margin-bottom: 30px;">Insert this code instead of your passoword</div>
          <div class="body-1" style="color: #000000; font-size: 16px; line-height: 24px; font-weight: normal; margin-bottom: 30px;">Best wishes, 
            <br>Make your perfect build
          </div>
        </td>
      </tr>
      <tr style="height: 40px;">
        <td style="border-collapse: separate; margin: 0px; font-size: 14px; height: 40px; vertical-align: middle; border-top: 1px solid #e0e0e0; padding: 10px 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 600px;" align="left" valign="middle" height="40">This email has been generated automatically. 
          <br>
          <strong>Please do not reply to it.</strong>
        </td>
      </tr>
      <tr style="height: 27px;">
        <td style="border-collapse: separate; margin: 0px; border-top: 1px solid #e0e0e0; padding: 16px 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 27px; width: 600px;" align="left">
          <table style="border-spacing: 0px; border: 0px none; border-collapse: separate; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 438px; height: 35px;" border="0" cellspacing="0" cellpadding="0" align="left">
            <tbody>
              <tr style="height: 72px;">
                <td style="border-collapse: separate; padding: 0px; margin: 0px; font-size: 12px; line-height: 24px; color: #888888; font-family: Arial, Helvetica, 'sans-serif'; width: 42.3854px; height: 72px;">Find us on:</td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <a href="https://github.com/Berindeiee/Proiect--pi.git">
                    <img src="https://share1.cloudhq-mkt3.net/2fd99bd42c6346.png" alt="" width="46" height="46">
                  </a> 
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 42.5938px; height: 72px;">&nbsp;</td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
      <tr style="height: 16px;">
        <td style="border-collapse: separate; padding: 0px 0px 16px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 16px; width: 600px;" align="left">&nbsp;</td>
      </tr>
      <tr style="height: 10px;">
        <td style="border-collapse: separate; padding: 0px 0px 16px; margin: 0px; border-bottom: 1px solid #e0e0e0; font-family: Arial, Helvetica, 'sans-serif'; height: 10px; width: 600px;" align="left">&nbsp;</td>
      </tr>
      <tr style="height: 16px;">
        <td style="border-collapse: separate; padding: 15px 0px 0px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 16px; width: 600px;" align="left">&nbsp;</td>
      </tr>
    </tbody>
  </table>
  <img src="https://ea.pstmrk.it/open/v3_bItdwZZHrGrP7pe-SzHJ2_aBDsAhpRrbjrnfudf2Ksz8-uVLih00eg7Iqlsc5_waqkJwsN4inacdLtPn-qYiuT8QXnn14oLzvr25iQrpeNyJP92Ovw2V9pldJvUx5TpJLCqV1w9xHk9cE_PXmTlbrzC15Xa6h1F-Qof5tKMc5khLPFkDS3YsxmHoAZM_9eyDkcZ-F94gtp5XeFFIHDyYzYMHMIpfSjQ7mLaRcRsQCCkPkrW4eN7PWIzYHC0bY_GqyEfKaL7oCqeKhfNvCFoQtfWDgi7-SQdOrkZv63cn-8Nsvx4Rn3_q1ujdK3mgB2dA1IEiphGk8W39Mf9YoKYisNxQiEqQp1BqHglHpJ1lSZz_P4KIH-z4c0M9QEjenS1ESi6jVv21FR81pRpSDmA22A" alt="" width="1" height="1" border="0">
</div>
    """
    html = Template(htm).safe_substitute(numar=numar)
    body = MIMEText(html, 'html')
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subiect
    em.set_content(body)
    context = ssl.create_default_context()
    em.attach(html)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        try:
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        except:
            exceptie = Toplevel(registration_screen)
            exceptie.title("Failed")
            exceptie.resizable(False, False)
            exceptie.geometry("300x150")
            play_music('sounds/error.mp3')
            customtkinter.CTkLabel(exceptie, text="Sending faild" + "\n" + " the email does not work",
                                   text_color="red").pack(padx=10, pady=10)
            customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)


def trimite_configuratie(catre, configuratie):
    email_sender = "build.pc.318@gmail.com"
    email_password = 'atydpcqtkqwtnjat'
    email_receiver = catre

    subiect = "Here is your configuration"
    html = """<div>
  <img src="http://news.libris.ro/gif/202212231033115d0f04b9a12cf4f05c9109203a338112:698167.gif" width="5" height="5">
  <div style="display: none; font-size: 1px; color: #333333; line-height: 1px; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;"></div>
  <p style="margin: 0; padding: 6px 10px; font-size: 12px; font-family: Arial, Helvetica, sans-serif;" align="center">
    <img src="https://freegoogleslidestemplates.com/wp-content/uploads/2016/04/FGST0013-modern-presentation-pitch-template-13.jpg" alt="">
    <br>
  </p>
  <br>
  <br>
</div>
"""
    body = MIMEText(html, 'html')
    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subiect
    # em.set_content(body)
    context = ssl.create_default_context()
    em.attach(body)

    f = open("Configuration.txt", "w")
    f.write(configuratie)
    f.close()
    f = "Configuration.txt"
    with open(f, "r") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(f)
        )
    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(f))
    em.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        try:
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        except:
            exceptie = customtkinter.CTk()
            exceptie.title("Failed")
            exceptie.resizable(False, False)
            exceptie.geometry("300x150")
            play_music('sounds/error.mp3')
            customtkinter.CTkLabel(exceptie, text="Sending faild" + "\n" + " the email does not work",
                                   text_color="red").pack(padx=10, pady=10)
            customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)
    os.remove("Configuration.txt")


def trimite_email_confirmare(catre, numar):
    email_sender = "build.pc.318@gmail.com"
    email_password = 'atydpcqtkqwtnjat'
    email_receiver = catre

    subiect = "Mesaj de verificare email"
    htm = """\
    <div>
  <div><!-- [if mso]>
    <noscript>
        <xml>
            <o:OfficeDocumentSettings>
                <o:AllowPNG/>
                <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
    </noscript>
    <![endif]--> <!-- [if lte mso 11]>
    <style type="text/css">
        .mj-outlook-group-fix { width:100% !important; }
    </style>
    <![endif]--></div>
</div>
<style>@media screen and (max-width: 359px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 300px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media screen and (min-width: 360px) and (max-width: 374px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 340px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media only screen and (min-width: 375px) and (max-width: 413px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 355px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media only screen and (min-width: 414px) and (max-width: 479px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 394px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media only screen and (min-width: 480px) and (max-width: 567px) {
  #logo-line {
    width: 440px !important;
    height: 5px !important;
  }
}
@media only screen and (min-width: 568px) and (max-width: 639px) {
  #logo-line {
    width: 528px !important;
    height: 5px !important;
  }
}
.button:hover {
  background-color: #2f82fb !important;
  color: #ffffff !important;
}
.button:active {
  background-color: #2872e0 !important;
  color: #ffffff !important;
}
.button.main:hover {
  background-color: #3c8cfc !important;
}
.button.main:active {
  background-color: #2872e0 !important;
}</style>
<div>
  <table style="border-spacing: 0px; margin: 0px; border-collapse: separate; border: 0px; max-width: 600px; font-family: Arial, Helvetica, 'sans-serif'; height: 334px;" border="0" cellspacing="0" cellpadding="0" align="left" bgcolor="#ffffff">
    <tbody>
      <tr style="height: 43px;">
        <td style="border-collapse: separate; margin: 0px; padding: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 43px; width: 600px;" align="left">
          <table id="logo-and-promo-text" style="border-spacing: 0px; border: 0px none; border-collapse: separate; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 501px; height: 104px;" border="0" cellspacing="0" cellpadding="0" align="left">
            <tbody>
              <tr>
                <td style="border-collapse: separate; padding: 0px 20px 0px 0px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 306px;">
                  <img style="height: 83px; display: inline-block; vertical-align: middle; padding: 0px;" src="https://share1.cloudhq-mkt3.net/a5d1450971468e.png" alt="Desktop" width="306" height="43" border="0">
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 16px; margin: 0px; font-size: 12px; line-height: 14px; color: #212121; font-weight: bold; vertical-align: middle; font-family: Arial, Helvetica, 'sans-serif'; width: 159px;" valign="middle">The way you can build your pc 
                  <img src="https://cdn.tiny.cloud/1/744os35bk6lfhnyx14onzpqa8er3gs4s21opocmie2wxar65/tinymce/4.9.11-104/plugins/emoticons/img/smiley-cool.gif" alt="cool">
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
      <tr style="height: 10px;">
        <td style="border-collapse: separate; padding: 0px; margin: 0px; line-height: 5px; font-family: Arial, Helvetica, 'sans-serif'; height: 10px; width: 600px;">
          <img id="logo-line" style="width: 600px; height: 5px; padding: 0px;" src="https://static.g2a.com/_/mail/g2a-line.png" width="600" height="5" border="0">
        </td>
      </tr>
      <tr style="height: 172px;">
        <td id="template-content" style="border-collapse: separate; padding: 30px 0px 0px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 172px; width: 600px;" align="left" valign="top">
          <h1 style="font-size: 20px; color: #000000; padding: 0; margin: 0 0 10px; font-weight: bold; line-height: 30px;">Email verification</h1>
          <div class="body-1" style="color: #000000; font-size: 16px; line-height: 24px; font-weight: normal; margin-bottom: 30px;">Email verification code is: $numar</div>
          <div class="body-1" style="color: #000000; font-size: 16px; line-height: 24px; font-weight: normal; margin-bottom: 30px;">Best wishes, 
            <br>Make your perfect build
          </div>
        </td>
      </tr>
      <tr style="height: 40px;">
        <td style="border-collapse: separate; margin: 0px; font-size: 14px; height: 40px; vertical-align: middle; border-top: 1px solid #e0e0e0; padding: 10px 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 600px;" align="left" valign="middle" height="40">This email has been generated automatically. 
          <br>
          <strong>Please do not reply to it.</strong>
        </td>
      </tr>
      <tr style="height: 27px;">
        <td style="border-collapse: separate; margin: 0px; border-top: 1px solid #e0e0e0; padding: 16px 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 27px; width: 600px;" align="left">
          <table style="border-spacing: 0px; border: 0px none; border-collapse: separate; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 438px; height: 35px;" border="0" cellspacing="0" cellpadding="0" align="left">
            <tbody>
              <tr style="height: 72px;">
                <td style="border-collapse: separate; padding: 0px; margin: 0px; font-size: 12px; line-height: 24px; color: #888888; font-family: Arial, Helvetica, 'sans-serif'; width: 42.3854px; height: 72px;">Find us on:</td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <a href="https://github.com/Berindeiee/Proiect--pi.git">
                    <img src="https://share1.cloudhq-mkt3.net/2fd99bd42c6346.png" alt="" width="46" height="46">
                  </a> 
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 42.5938px; height: 72px;">&nbsp;</td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
      <tr style="height: 16px;">
        <td style="border-collapse: separate; padding: 0px 0px 16px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 16px; width: 600px;" align="left">&nbsp;</td>
      </tr>
      <tr style="height: 10px;">
        <td style="border-collapse: separate; padding: 0px 0px 16px; margin: 0px; border-bottom: 1px solid #e0e0e0; font-family: Arial, Helvetica, 'sans-serif'; height: 10px; width: 600px;" align="left">&nbsp;</td>
      </tr>
      <tr style="height: 16px;">
        <td style="border-collapse: separate; padding: 15px 0px 0px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 16px; width: 600px;" align="left">&nbsp;</td>
      </tr>
    </tbody>
  </table>
  <img src="https://ea.pstmrk.it/open/v3_bItdwZZHrGrP7pe-SzHJ2_aBDsAhpRrbjrnfudf2Ksz8-uVLih00eg7Iqlsc5_waqkJwsN4inacdLtPn-qYiuT8QXnn14oLzvr25iQrpeNyJP92Ovw2V9pldJvUx5TpJLCqV1w9xHk9cE_PXmTlbrzC15Xa6h1F-Qof5tKMc5khLPFkDS3YsxmHoAZM_9eyDkcZ-F94gtp5XeFFIHDyYzYMHMIpfSjQ7mLaRcRsQCCkPkrW4eN7PWIzYHC0bY_GqyEfKaL7oCqeKhfNvCFoQtfWDgi7-SQdOrkZv63cn-8Nsvx4Rn3_q1ujdK3mgB2dA1IEiphGk8W39Mf9YoKYisNxQiEqQp1BqHglHpJ1lSZz_P4KIH-z4c0M9QEjenS1ESi6jVv21FR81pRpSDmA22A" alt="" width="1" height="1" border="0">
</div>
    """
    html = Template(htm).safe_substitute(numar=numar)
    body = MIMEText(html, 'html')
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subiect
    em.set_content(body)
    context = ssl.create_default_context()
    em.attach(html)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        try:
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        except:
            exceptie = Toplevel(registration_screen)
            exceptie.title("Failed")
            exceptie.resizable(False, False)
            exceptie.geometry("300x150")
            play_music('sounds/error.mp3')
            customtkinter.CTkLabel(exceptie, text="Sending faild" + "\n" + " the email does not work",
                                   text_color="red").pack(padx=10, pady=10)
            customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)


# Designing window for registration
def register():
    global registration_screen
    registration_screen = customtkinter.CTkToplevel(main_screen)
    registration_screen.geometry(f"{400}x{800}")
    registration_screen.title("Registration")
    global username
    global password
    global email
    global password_r

    global username_entry
    global password_entry
    global password_r_entry
    global email_entry
    global cod
    global cod_introdus_entry
    global trimis
    global inregistrare

    username = StringVar()
    password = StringVar()
    password_r = StringVar()
    email = StringVar()

    customtkinter.CTkLabel(registration_screen, text="Please enter your information", font=("Roboto", 20),
                           # text_color="black",
                           fg_color=("#B8A11D"),
                           corner_radius=8
                           ).pack(pady=5, padx=10)
    customtkinter.CTkLabel(registration_screen, text="Username*", font=("Roboto", 15),
                           # text_color="black"
                           ).pack(pady=1, padx=10)

    username_entry = customtkinter.CTkEntry(registration_screen, placeholder_text="numele de utilizator",
                                            textvariable=username)
    username_entry.pack(pady=1, padx=10)

    customtkinter.CTkLabel(registration_screen, text="Email*", font=("Roboto", 15),
                           # text_color="black"
                           ).pack(pady=1, padx=10)
    email_entry = customtkinter.CTkEntry(registration_screen, placeholder_text="emailul dumneavoastra",
                                         textvariable=email)
    email_entry.pack(pady=1, padx=10)

    customtkinter.CTkLabel(registration_screen, text="Password*", font=("Roboto", 15),
                           # text_color="black"
                           ).pack(pady=1, padx=10)
    password_entry = customtkinter.CTkEntry(registration_screen, placeholder_text="parola", show="😄",
                                            textvariable=password)
    password_entry.pack(pady=1, padx=10)

    customtkinter.CTkLabel(registration_screen, text="Re-enter Password*", font=("Roboto", 15),
                           # text_color="black"
                           ).pack(pady=1, padx=10)
    password_r_entry = customtkinter.CTkEntry(registration_screen, placeholder_text="reintroduceti parola", show="😄",
                                              textvariable=password_r)
    password_r_entry.pack(pady=1, padx=10)

    email_image = customtkinter.CTkImage(light_image=Image.open("email_l.png"),
                                         dark_image=Image.open("email_d.png"),
                                         size=(30, 30))

    register_image = customtkinter.CTkImage(light_image=Image.open("imagini/register_l.png"),
                                            dark_image=Image.open("imagini/register_d.png"),
                                            size=(30, 30))
    global cod

    trimis = customtkinter.CTkButton(registration_screen, image=email_image, text="Send verfication email",
                                     corner_radius=8,
                                     # text_color="black",
                                     compound="right",
                                     command=lambda: timer(registration_screen)
                                     )
    trimis.pack(padx=5, pady=20)

    inregistrare = customtkinter.CTkButton(registration_screen, image=register_image, text="Sign up",
                                           corner_radius=8,
                                           # text_color="black",
                                           compound="right",
                                           command=register_user,
                                           state="disabled"
                                           )
    inregistrare.pack(pady=1, padx=10)


def timer(fer):
    global cod
    cod = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    if email.get():
        inregistrare.configure(state="normal")
        trimis.configure(state="disabled")
        # aici se apeleaza functia pentru a trimitye codul de verificare
        trimite_email_confirmare(email.get(), cod)

        global ok
        if ok == 1:
            global cod_introdus_entry
            global cod_introdus
            cod_introdus = StringVar()
            cod_label = customtkinter.CTkLabel(fer, text="Code*", font=("Roboto", 15),
                                               # text_color="black"
                                               )
            cod_label.pack(pady=1, padx=10)
            cod_introdus_entry = customtkinter.CTkEntry(fer, placeholder_text="dfs", width=100,
                                                        textvariable=cod_introdus)
            cod_introdus_entry.pack(pady=1, padx=10)

        def update():
            global score
            score = score - 1
            ScoreL.configure(text="You have " + str(score) + " seconds left to enter the code")
            if score > limit:
                # schedule next update 1 second later
                fer.after(1000, update)
            else:
                global ok
                inregistrare.configure(state="disabled")
                ScoreL.destroy()
                cod_introdus_entry.destroy()
                cod_label.destroy()
                ok = 1
                score = 120
                trimis.configure(state="normal")

        if ok == 1:
            ScoreL = customtkinter.CTkLabel(fer, text="You have " + str(score) + " seconds left to enter the code",
                                            # text_color="black"
                                            )
            ScoreL.pack(pady=1, padx=10)
            ok = 0
        fer.after(1000, update)  # start the update 1 second later
    else:
        play_music('sounds/please_enter_an_email.mp3')


# Implementing event on register button
# def validare_email(email):

def register_user():
    username_info = username.get()
    password_info = password.get()
    password_r_info = password_r.get()
    email_info = email.get()
    cod_introdus_info = cod_introdus.get()
    if os.path.isfile('./' + username_info) == 1:
        exceptie = Toplevel(registration_screen)
        exceptie.title("Failed")
        exceptie.resizable(False, False)
        play_music('sounds/error1.mp3')
        exceptie.geometry("300x150")
        customtkinter.CTkLabel(exceptie, text="Sign up faild" + "\n" + " username already exist",
                               text_color="red").pack(padx=10, pady=10)
        customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)
    elif password_info != password_r_info:
        exceptie = Toplevel(registration_screen)
        exceptie.title("Failed")
        exceptie.resizable(False, False)
        play_music('sounds/error1.mp3')
        exceptie.geometry("300x150")
        customtkinter.CTkLabel(exceptie, text="Registration faild" + "\n" + " password do not match",
                               text_color="red").pack(padx=10, pady=10)
        customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)
    elif cod != cod_introdus_info:
        exceptie = Toplevel(registration_screen)
        exceptie.title("Failed")
        exceptie.resizable(False, False)
        play_music('sounds/error1.mp3')
        exceptie.geometry("300x150")
        customtkinter.CTkLabel(exceptie, text="Registration faild" + "\n" + " the code is wrong",
                               text_color="red").pack(padx=10, pady=10)
        customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)
    elif password_info == password_r_info:  # verificare reintroducere parola
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.write(email_info + "\n")
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        password_r_entry.delete(0, END)
        email_entry.delete(0, END)
        exceptie = Toplevel(registration_screen)
        exceptie.title("Sign up succes")
        exceptie.resizable(False, False)
        exceptie.geometry("300x150")
        customtkinter.CTkLabel(exceptie, text="Registration succecs" + "\n" + " now you can sign up",
                               text_color="green").pack(padx=10, pady=10)
        customtkinter.CTkButton(exceptie, text="OK", command=lambda: destroy_registeration(exceptie)).pack(padx=1,
                                                                                                           pady=1)


def destroy_registeration(exceptie):
    exceptie.destroy()
    registration_screen.destroy()


# Designing popup for user not found


def get_culoare():
    if customtkinter.get_appearance_mode() == "Light":
        return 'gray92'
    else:
        return 'gray14'


def actualizare_culoare(mybutton1, mybutton2):
    fcolor = get_culoare()
    bcolor = '#25dae9'
    mybutton1.configure(fg_color=fcolor)
    mybutton1.configure(text_color=bcolor)
    mybutton1.configure(bg_color=fcolor)
    bcolor = '#ffcc66'
    mybutton2.configure(fg_color=fcolor)
    mybutton2.configure(text_color=bcolor)
    mybutton2.configure(bg_color=fcolor)


def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)
    actualizare_culoare(mybutton1, mybutton2)


def change_set_default_color_theme(new_default_color_theme: str):
    if(new_default_color_theme!="Color theme"):
        customtkinter.set_default_color_theme(new_default_color_theme)
        main_screen.destroy()
        main_account_screen()


def play_music(muzica):
    try:
        pygame.mixer.music.load(muzica)
        pygame.mixer.music.play(loops=0)
    except:
        print("asta este")


# Designing Main(first) window

def main_account_screen():
    pygame.mixer.init()
    global main_screen
    global mybutton1
    global mybutton2
    global appearance_mode_optionemenu

    def open_pdf(link):
        # webbrowser.open(link)
        os.startfile("Terms and conditions.pdf")
        mybutton2.configure(state="normal")
        mybutton1.configure(state="normal")
        term.destroy()

    main_screen = customtkinter.CTk()
    main_screen.geometry(f"{300}x{320}")
    main_screen.eval('tk::PlaceWindow . center')
    main_screen.title("Make your perfect build")
    main_screen.protocol("WM_DELETE_WINDOW",
                         lambda: [play_music('sounds/byebye.mp3'), time.sleep(0.75), main_screen.destroy()])
    customtkinter.CTkLabel(master=main_screen, text="Welcome", font=("", 20)).pack(pady=1, padx=1)
    # Button(text="Login", height="2", width="30", command=login).pack()
    # Label(text="").pack()
    # Button(text="Register", height="2", width="30", command=register).pack()
    mybutton1 = bttn1(main_screen, "S I G N   I N ", '#25dae9', lambda: log(main_screen))
    mybutton2 = bttn1(main_screen, "S I G N   U P ", '#ffcc66', register)

    appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=main_screen, values=["Dark", "Light"],
                                                              command=change_appearance_mode_event)
    appearance_mode_optionemenu.pack(pady=3, padx=5)

    global color_them_optionmenu

    color_them_optionmenu = customtkinter.CTkOptionMenu(master=main_screen, values=["Color theme","green", "blue"],
                                                        command=change_set_default_color_theme)
    color_them_optionmenu.pack(pady=3, padx=5)
    actualizare_culoare(mybutton1, mybutton2)

    button_T = customtkinter.CTkButton(master=main_screen,
                                       width=120,
                                       height=32,
                                       border_width=0,
                                       corner_radius=8,
                                       text="Terms and conditions",
                                       command=lambda: open_pdf("https://pastebin.com/Jat12QmJ"),
                                       fg_color='transparent', text_color=("#1A8C52", "#FFFFFF"))
    button_T.place(relx=0.5, rely=1, anchor="s")
    term = customtkinter.CTkLabel(master=main_screen, text="To use the app please\n read Terms and conditions",
                                  font=("", 10))
    term.pack(pady=1, padx=1)
    play_music('sounds/tuturu.mp3')

    print(main_screen.cget("fg_color"))

    main_screen.mainloop()


def is_connected():
    try:
        # Incercam sa obtinem IP-ul unui host bine cunoscut (Ex: google.com)
        socket.gethostbyname("www.google.com")
        return True
    except:
        return False


if is_connected():
    print("Sistemul este conectat la internet")
    main_account_screen()
else:
    exceptie = customtkinter.CTk()
    exceptie.title("Failed")
    exceptie.resizable(False, False)
    play_music('sounds/error1.mp3')
    exceptie.geometry("300x150")
    customtkinter.CTkLabel(exceptie, text="Starting failed" + "\n" + " the pc is not connected to the network",
                           text_color="red").pack(padx=10, pady=10)
    customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)
    exceptie.mainloop()
