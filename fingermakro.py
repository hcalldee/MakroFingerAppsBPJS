import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import mysql.connector
import webbrowser
import time
import os
import pyautogui
import subprocess
from datetime import date

from ttkbootstrap.dialogs import Messagebox

class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        self.s = ttk.Style()
        ttk.Style().configure("TButton", font="Arial 15")
        super().__init__(master, padding=(20, 5))
        self.pack(fill=BOTH, expand=YES)
        self.widthbtn = 10
        self.heightbtn = 10
        # form variables
        self.rm = ttk.StringVar(value="")

        # form header
        hdr_txt = "Silahkan Masukkan Nomer RM" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=40)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("No RM", self.rm)
        self.create_buttonnumber1()
        self.create_buttonnumber2()
        self.create_buttonnumber3()
        self.create_buttonnumber4()

    def on_button_pressed(self, txt):
        """Handles and routes all button press events."""
        display = self.rm.get()
        if len(display)<6:
            self.press_number(display, txt)

    def getPeserta(self,param):
        config = {}

        # Read the configuration from the text file
        with open('db_config.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                config[key] = value

        # Establish the MySQL connection using the configuration
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("SELECT * FROM pasien WHERE no_rkm_medis = '"+param+"'")
        cursor.execute(query)
        
        for (value) in cursor:
            usr = value

        cursor.close()
        cnx.close()
        return usr
    
    def press_number(self, display, txt):
        """A digit button is pressed"""
        if display == "":
            self.rm.set(txt)
        else:
            self.rm.set(f"{display}{txt}")

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=1)

        lbl = ttk.Label(master=container, text=label.title(), width=6,font=('Arial 18'))
        lbl.pack(side=LEFT, padx=0, pady=30)

        ent = ttk.Entry(master=container, textvariable=variable,font=('Arial 30'))
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES,)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Cari",
            style='my.TButton',
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        cnl_btn.pack(side=RIGHT, padx=5)


    def create_buttonnumber1(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=3, padx=80)

        one = ttk.Button(
            master=container,
            text="1",
            command=lambda x="1": self.on_button_pressed(x),

            bootstyle=INFO,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        one.pack(side=LEFT, padx=5)
        one.focus_set()

        two = ttk.Button(
            master=container,
            text="2",
            command=lambda x="2": self.on_button_pressed(x),
            bootstyle=INFO,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        two.pack(side=LEFT, padx=5)
        two.focus_set()

        three = ttk.Button(
            master=container,
            text="3",
            command=lambda x="3": self.on_button_pressed(x),
            bootstyle=INFO,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        three.pack(side=LEFT, padx=5)
        three.focus_set()

    def create_buttonnumber2(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=3, padx=80)

        one = ttk.Button(
            master=container,
            text="4",
            command=lambda x="4": self.on_button_pressed(x),
            bootstyle=INFO,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        one.pack(side=LEFT, padx=5)
        one.focus_set()

        two = ttk.Button(
            master=container,
            text="5",
            command=lambda x="5": self.on_button_pressed(x),
            bootstyle=INFO,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        two.pack(side=LEFT, padx=5)
        two.focus_set()

        three = ttk.Button(
            master=container,
            text="6",
            command=lambda x="6": self.on_button_pressed(x),
            bootstyle=INFO,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        three.pack(side=LEFT, padx=5)
        three.focus_set()


    def create_buttonnumber3(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=3, padx=80)

        one = ttk.Button(
            master=container,
            text="7",
            command=lambda x="7": self.on_button_pressed(x),
            bootstyle=INFO,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        one.pack(side=LEFT, padx=5)
        one.focus_set()

        two = ttk.Button(
            master=container,
            text="8",
            command=lambda x="8": self.on_button_pressed(x),
            bootstyle=INFO,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        two.pack(side=LEFT, padx=5)
        two.focus_set()

        three = ttk.Button(
            master=container,
            text="9",
            command=lambda x="9": self.on_button_pressed("9"),
            bootstyle=INFO,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        three.pack(side=LEFT, padx=5)
        three.focus_set()

    def create_buttonnumber4(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=3, padx=80)

        one = ttk.Button(
            master=container,
            text="0",
            command=lambda x="0": self.on_button_pressed(x),
            bootstyle=INFO,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        one.pack(side=LEFT, padx=5)

        sub_btn = ttk.Button(
            master=container,
            text="Cari",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        sub_btn.pack(side=RIGHT, padx=5)

        cnl_btn = ttk.Button(
            master=container,
            text="Hapus",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=self.widthbtn,
            padding=self.heightbtn
        )
        cnl_btn.pack(side=RIGHT, padx=5)




    def settings(self):
        config = {}

        # Read the configuration from the text file
        with open('db_config.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                config[key] = value

        # Establish the MySQL connection using the configuration
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("SELECT * FROM mlite_settings WHERE module = 'afm'")
        cursor.execute(query)
        i=0
        for (value) in cursor:
            if i == 0:
                usr = value[3]
            else:
                pswd = value[3]
            i+=1

        cursor.close()
        cnx.close()
        return [usr,pswd]
    
    # makro
    def macro_run(self,param,param2):
        with open('host_config.txt', 'r') as host_file:
            timesleep = host_file.read().strip()
            timesleep = timesleep.splitlines()[1]
        time.sleep(timesleep)
        pyautogui.write(param[0], interval=0.01)
        time.sleep(timesleep * (10 / 100))
        pyautogui.press('tab')
        pyautogui.write(param[1], interval=0.01)
        pyautogui.press('enter')
        time.sleep(timesleep * (10 / 100))
        pyautogui.press('enter')
        time.sleep(round(timesleep * (50 / 100)))
        pyautogui.write(param2)

    def run_macro(self,param):
        # utama
        cmd = "tasklist /FI \"imagename eq after.exe\" "
        setting = self.settings()

        returned_output = subprocess.check_output(cmd)
        info = returned_output.decode("utf-8")
        if "INFO" in info:
            os.system("start After.lnk ")
            self.macro_run(setting,param)

        elif "After.exe" in info:
            print('kill first')
            os.system("taskkill /im after.exe /f")
            os.system("start After.lnk ")
            self.macro_run(setting,param)
        
    def on_submit(self):
        """Print the contents to console and return the values."""
        jns = self.getPeserta(self.rm.get())[18]
        noka = self.getPeserta(self.rm.get())[19]
        rm = self.rm.get()
        self.rm.set("")
        tgl = ''
        if jns == 'BPJ' and noka != '':
            # 137995
            config = {}

            # Read the configuration from the text file
            with open('db_config.txt', 'r') as file:
                for line in file:
                    key, value = line.strip().split('=')
                    config[key] = value

            # Establish the MySQL connection using the configuration
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()

            query = ("SELECT b.tgl_rencana FROM bridging_sep AS a JOIN bridging_surat_kontrol_bpjs AS b ON a.no_sep = b.no_sep WHERE nomr = '"+rm+"' ORDER BY tglsep DESC LIMIT 1")
            cursor.execute(query)
            i=0
            for (value) in cursor:
                if i == 0:
                    tgl = value[0]

            cursor.close()
            cnx.close()
            with open('host_config.txt', 'r') as host_file:
                host_url = host_file.read().strip()
                host_url = host_url.splitlines()[0]

            if tgl == date.today():
                webbrowser.open(f"{host_url}/anjungan/sep/{noka}/{rm}", new=2)
                self.run_macro(noka)
            elif tgl == '':
                webbrowser.open(f"{host_url}/anjungan/sep/{noka}/{rm}", new=2)
                self.run_macro(noka)
            else:
                # webbrowser.open(f"{host_url}/anjungan/sep/{noka}/{rm}", new=2)
                # self.run_macro(noka)
                self.msgbox('Mohon Maaf, Silahkan Kontrol Sesuai Jadwal,\n atau Silahkan Mengambil Antrian FO')
                

        elif jns == 'BPJ' and noka == '':
            self.msgbox('Mohon Maaf, Nomer Kartu Pasien Belum Direkam')
        else:
            self.msgbox('Mohon Maaf, bukan peserta BPJS')

    def on_cancel(self):
        """Cancel and close the application."""
        self.rm.set("")

    def msgbox(self,message):
        mb = Messagebox.yesno(message,'Error')


if __name__ == "__main__":

    app = ttk.Window("Anjungan Finger Mandiri", "superhero", resizable=(FALSE, FALSE))
    DataEntryForm(app)
    app.mainloop()