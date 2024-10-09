from tkinter import messagebox
from tkinter import *
import tkinter as tk
from tkinter import ttk, font
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import csv


class Smart_Cleaner:
    def __init__(self, master):

        self.registered_users = {}
        self.load_registered_users()
        # self.selected_language = tk.StringVar()


        self.master = master
        self.master.title("Smart Cleaner")
        self.master.state("zoomed")
        self.master.resizable(width=tk.TRUE, height=tk.TRUE)
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        self.frame_bawah = Frame(self.master,width=screen_width,height=screen_height)
        self.frame_bawah.place(x=0,y=0)
        self.foto=Image.open("1.png")
        self.foto=self.foto.resize((screen_width,screen_height))
        self.photoo=ImageTk.PhotoImage(self.foto)
        label_background = Label(self.frame_bawah, image=self.photoo)
        label_background.place(x=0, y=0)
        label_background.photo=self.photoo

        self.label_username = tk.Label(self.frame_bawah, text="Username:")
        self.label_username.place(x=500,y=300)
        self.entry_username = tk.Entry(self.frame_bawah)
        self.entry_username.place(x=575,y=300)

        self.label_password = tk.Label(self.frame_bawah, text="Password:")
        self.label_password.place(x=500, y=350)
        self.entry_password = tk.Entry(self.frame_bawah, show="*")
        self.entry_password.place(x=575, y =350)
        self.btn_login = tk.Button(self.frame_bawah, text="Login", command=self.cek_login)
        self.btn_login.place(x=550, y =400)

        self.btn_registrasi = tk.Button(self.frame_bawah, text="Registrasi", command=self.tampil_registrasi)
        self.btn_registrasi.place(x=650, y = 400)

    def tampil_registrasi(self):
        self.master.withdraw()
        self.window_reg = Toplevel()
        self.window_reg.title("Registrasi")
        self.window_reg.state("zoomed")
        self.window_reg.resizable(width=tk.TRUE, height=tk.TRUE)
        screen_width = self.window_reg.winfo_screenwidth()
        screen_height = self.window_reg.winfo_screenheight()
        self.frame_reg = Frame(self.window_reg,width=screen_width,height=screen_height)
        self.frame_reg.place(x=0,y=0)
        self.foto=Image.open("2.png")
        self.foto=self.foto.resize((screen_width,screen_height))
        self.photoo=ImageTk.PhotoImage(self.foto)
        label_background = Label(self.frame_reg, image=self.photoo)
        label_background.place(x=0, y=0)
        label_background.photo=self.photoo

        
        self.label_reg_username = tk.Label(self.frame_reg, text="Username:")
        self.label_reg_username.place(x=500,y=300)
        self.entry_reg_username = tk.Entry(self.frame_reg)
        self.entry_reg_username.place(x=575,y=300)
        self.label_reg_password = tk.Label(self.frame_reg, text="Password:")
        self.label_reg_password.place(x=500, y=350)
        self.entry_reg_password = tk.Entry(self.frame_reg)
        self.entry_reg_password.place(x=575, y=350)

        self.btn_registrasi = tk.Button(self.frame_reg, text="Registrasi",command=lambda: self.daftar_akun())
        self.btn_registrasi.place(x=600, y = 400)


    def load_registered_users(self):
        try:
            with open('akun.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                self.registered_users = {row['Username']: row['Password'] for row in reader}
        except FileNotFoundError:
            self.registered_users = {}

    def save_registered_users(self):
        with open('akun.csv', 'w', newline='') as file:
            fieldnames = ['Username', 'Password']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for username, password in self.registered_users.items():
                writer.writerow({'Username': username, 'Password': password})
        self.window_reg.destroy()
        self.master.deiconify()
        self.master.state("zoomed")

    def daftar_akun(self):
        username = self.entry_reg_username.get()
        password = self.entry_reg_password.get()

        if username and password:
            if 6 <= len(username) <= 20 and 6 <= len(password) <= 20:
                if any(i.islower() for i in password) and any(i.isupper() for i in password) \
                        and any(i.isdigit() for i in password) and any(ip.islower() for ip in username) \
                        and any(ip.isupper() for ip in username):
                    if any(p1.islower() for p1 in username) and any(c1.isupper() for c1 in username) \
                            and not any(c1.isdigit() for c1 in username):
                        if username in self.registered_users:
                            messagebox.showerror("Registrasi", "Username sudah terdaftar")
                        else:
                            self.registered_users[username] = password
                            messagebox.showinfo("Registrasi", "Registrasi berhasil")
                            self.window_reg.destroy()
                            self.save_registered_users()
                    else:
                        messagebox.showerror("Error", "Username must only consist of uppercase and lowercase letters")
                else:
                    messagebox.showerror("Error", "Password must include uppercase letters, lowercase letters, numbers, and username must include uppercase and lowercase letters")
            else:
                messagebox.showerror("Error", "Username must be between 6 and 20 characters, and password must be between 6 and 20 characters")
        else:
            messagebox.showerror("Error", "All fields must be filled!")

    def On_close(self):
        self.window_reg.destroy()
        self.master.deiconify()

    def pop_up(self):
        self.window_reg.destroy()
        self.master.deiconify()
        self.master.state("zoomed")


    
    def cek_login(self):
        global username
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "" or password == "":
            messagebox.showerror("Gagal", "Username atau password tidak boleh kosong")
            return

        if username not in self.registered_users:
            messagebox.showerror("Gagal", "Username tidak terdaftar")
            return

        if self.registered_users[username] != password:
            messagebox.showerror("Gagal", "Password salah")
            return

        messagebox.showinfo("Sukses", "Login berhasil")
        self.halaman_dekstop()
        

    def halaman_dekstop(self):
        if self.frame_bawah.destroy():
            window_reg = tk.Toplevel(self.root)
            window_reg.title("Desktop")
        else:
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_dsk = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_dsk.place(x=0,y=0)
            self.foto=Image.open("3.png")
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_dsk, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo

        self.label_font = font.Font(family="Helvetica", size=9, underline=True)

        self.btn_dsk_kost = tk.Button(self.frame_dsk, bg="green", width=8, height=3, relief=FLAT, command=self.kost)
        self.btn_dsk_kost.place(x=581, y=545)
        self.label_font_kost = tk.Label(self.frame_dsk, width=6, height=1, text="More info",fg="#be4308",bg="blue", font=self.label_font).place(x=581, y=545)
        self.btn_dsk_rumah = tk.Button(self.frame_dsk, bg="green", width=8, height=3, relief=FLAT, command=self.rumah)
        self.btn_dsk_rumah.place(x=280, y=530)
        self.label_font_rumah = tk.Label(self.frame_dsk, width=6, height=1, text="More info",fg="#be4308",bg="blue", font=self.label_font).place(x=280, y=530)
        self.btn_dsk_other = tk.Button(self.frame_dsk, bg="green",text="More info", font=self.label_font, width=8, height=3, relief=FLAT, command=self.other)
        self.btn_dsk_other.place(x=870, y=530)
        # self.label_font_other = tk.Label(self.frame_dsk, width=6, height=1, text="More info",fg="#be4308",bg="blue", font=self.label_font).place(x=870, y=530)

    def home_kost(self):
        home_kst = messagebox.askyesno("Home!", "Apakah Anda yakin ingin kembali ke halaman utama?")

        if home_kst:
            self.frame_kst.destroy()
            self.halaman_dekstop()
            
            pass

        else:
            self.kost()

        
    def kost(self):

        if self.frame_dsk.destroy():
            window_kst = tk.Toplevel(self.root)
            window_kst.title("Kost")
        else:
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_kst = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_kst.place(x=0,y=0)
            self.foto=Image.open("4.png")
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_kst, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo

            self.add_calendar_kst()
            self.combo_bersih_kost()
            self.btn_home_kost()

    def btn_home_kost(self):
        image = Image.open("4.png")
        image=image.resize((50,50))
        home = ImageTk.PhotoImage (image)
        self.btn_home_kst = tk.Button(self.frame_kst, command=self.home_kost, image=home)
        self.btn_home_kst.photo=home
        self.btn_home_kst.place(x=150, y=2, width=60,height=50)

    def add_calendar_kst(self):
        self.cal_kst = DateEntry(self.frame_kst, selectmode='day')
        self.cal_kst.place(x=775, y=430)

        self.label_nomor_kst = Label(self.frame_kst, text="Nomor Hp:")
        self.label_nomor_kst.place(x=655, y=400)

        self.entry_nomor_kst = Entry(self.frame_kst , width=40)
        self.entry_nomor_kst.place(x=775, y=400)

        self.label_alamat_kst = Label(self.frame_kst, text="Alamat:")
        self.label_alamat_kst.place(x=655, y=370)

        self.entry_alamat_kst = Entry(self.frame_kst , width=40)
        self.entry_alamat_kst.place(x=775, y=370)

        self.label_nama_kst = Label(self.frame_kst, text="Nama Pelanggan:")
        self.label_nama_kst.place(x=655, y=340)
        self.label_username_kst = tk.Label(self.frame_kst, text="*Nama pengguna diisi sesuai dengan username akun")
        self.label_username_kst.place(x=654,y=320)

        self.entry_nama_kst = Entry(self.frame_kst , width=40)
        self.entry_nama_kst.place(x=775, y=340)

        self.label_jadwal_kst = Label(self.frame_kst, text="Jadwal (MM/DD/YY)")
        self.label_jadwal_kst.place(x=655, y=430)

        self.label_metode_pembersihan = Label(self.frame_kst, text="Metode Pembersihan")
        self.label_metode_pembersihan.place(x=655, y=460)

        self.btn_bayar_kst = tk.Button(self.frame_kst, text="Bayar", command=self.payment_kst)
        self.btn_bayar_kst.place(x=967, y=530)
    
    def show_selected_language_kost(self):
        self.selected_language_kst = tk.StringVar()
        self.radio_button1_kst = tk.Radiobutton(self.frame_pay_kst, text="Cash", value= "Cash" , variable=self.selected_language_kst , command= self.show_selected_language_kost)
        self.radio_button1_kst.place(x=840 , y=293)

        self.radio_button2_kst = tk.Radiobutton(self.frame_pay_kst, text="Q-Ris", value= "Q-Ris" , variable=self.selected_language_kst,  command= self.show_selected_language_kost)
        self.radio_button2_kst.place(x=760 , y=450)
            
    def combo_bersih_kost(self):
            # Combobox creation 
        self.combo_bersih_kst = tk.StringVar() 
        self.metodechoosen_kst = ttk.Combobox(self.frame_kst, width = 27,state="readonly", textvariable = self.combo_bersih_kst, values=["Pembersihan Umum", "Pembersihan Mendalam"]) 

        self.metodechoosen_kst.place(x=775, y=460)
        self.metodechoosen_kst.current()

        pass

    def payment_kst(self):
        confirm_payment = messagebox.askyesno("Konfirmasi Pembayaran", "Apakah Anda yakin ingin melakukan pembayaran?")

        if confirm_payment:
            self.frame_dsk.destroy()
            
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_pay_kst = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_pay_kst.place(x=0,y=0)
            self.foto=Image.open("7.png")
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_pay_kst, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo


            self.btn_konfirmasi_kst = tk.Button(self.frame_pay_kst, text="Konfirmasi", command=self.konfirmasi_pesanan_kst)
            self.btn_konfirmasi_kst.place(x=850, y=580)

            self.show_selected_language_kost()
            
            pass

        else:
            self.kost()

    def konfirmasi_pesanan_kst(self):

        if self.frame_pay_kst.destroy():
            window_kfm_kst= tk.Toplevel(self.root)
            window_kfm_kst.title("Konfirmasi")
        else:
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_kfm_kst = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_kfm_kst.place(x=0,y=0)
            self.foto=Image.open("10.png")
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_kfm_kst, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo

        self.btn_selesai_kst = tk.Button(self.frame_kfm_kst, text="Finish", command=self.sukses_kost)
        self.btn_selesai_kst.place(x=600, y=550)

        self.add_output_kost()

    def add_output_kost(self):
        selected_date_kst = self.cal_kst.get_date()
        alamat_kst = self.entry_alamat_kst.get()
        metode_pembersih_kst = self.combo_bersih_kst.get()
        username_kst = self.entry_nama_kst.get()
        selected_language_kst = self.selected_language_kst.get()
        nomor_kst = self.entry_nomor_kst.get()

        output_jadwal_kst = f"Tanggal yang dipilih : {selected_date_kst}"
        output_label_jadwal_kst = tk.Label(self.frame_kfm_kst, text=output_jadwal_kst, font= "arial 16" , bg="white" )
        output_label_jadwal_kst.place(x=280 , y=360)

        output_alamat_kst = f"Alamat : {alamat_kst}"
        output_label_alamat_kst = tk.Label(self.frame_kfm_kst, text=output_alamat_kst, font= "arial 16" , bg="white")
        output_label_alamat_kst.place(x=280 , y=400)

        output_method_kst = f"Metode Pembersihan : {metode_pembersih_kst}"
        output_label_alamat_kst = tk.Label(self.frame_kfm_kst, text=output_method_kst, font= "arial 16" , bg="white")
        output_label_alamat_kst.place(x=280 , y=440)

        output_label_payment_pay_kst = tk.Label(self.frame_kfm_kst, text="Harga : Rp.230.000,00 " , font= "arial 16", bg="white")
        output_label_payment_pay_kst.place(x=280, y=480)

        output_nama_kst= f"Nama Pelanggan : {username_kst}"
        output_label_nama_kst = tk.Label(self.frame_kfm_kst, text=output_nama_kst, font= "arial 16" , bg="white")
        output_label_nama_kst.place(x=280 , y=320)

        output_pay_kst= f"Pembayaran : {selected_language_kst}"
        output_label_pay_kst = tk.Label(self.frame_kfm_kst, text=output_pay_kst, font= "arial 16" , bg="white")
        output_label_pay_kst.place(x=280 , y=520)

        output_nomor_kst= f"Nomor HP : {nomor_kst}"
        output_lnomor_kst = tk.Label(self.frame_kfm_kst, text=output_nomor_kst, font= "arial 16" , bg="white")
        output_lnomor_kst.place(x=280 , y=550)

   
        file_name = "output_kost.csv"  
        with open(file_name, 'a', newline='') as file:
            fieldnames = ['Nama', 'Alamat','Jadwal','Method','Pembayaran', 'Nomor HP']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Nama' : username_kst ,'Alamat' : alamat_kst ,'Jadwal' : selected_date_kst ,'Method' : metode_pembersih_kst, 'Pembayaran' : selected_language_kst, 'Nomor HP' : nomor_kst})



    def sukses_kost(self):
        if self.frame_kfm_kst.destroy():
            window_reg = tk.Toplevel(self.root)
            window_reg.title("Sukses!!")
        else:
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_sukses_kst = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_sukses_kst.place(x=0,y=0)
            self.foto=Image.open("11.png")
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_sukses_kst, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo


        self.sukses_kst = tk.Button(self.frame_sukses_kst, text="Selesai", command=self.halaman_dekstop)
        self.sukses_kst.place(x=615, y=585)
        


    def rumah(self):

        if self.frame_dsk.destroy():
            window_rmh = tk.Toplevel(self.root)
            window_rmh.title("Rumah")
        else:
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_rmh = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_rmh.place(x=0,y=0)
            self.foto=Image.open("5.png")
            self.foto=self.foto.resize((screen_width,screen_height)) 
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_rmh, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo

            self.add_calendar_rmh()
            self.combo_bersih_rumah()
            self.btn_home_rumah()

    def btn_home_rumah(self):
        image = Image.open("Home.png")
        image=image.resize((50,50))
        home = ImageTk.PhotoImage (image)
        self.btn_home_rmh = tk.Button(self.frame_rmh, command=self.home_rumah, image=home)
        self.btn_home_rmh.photo=home
        self.btn_home_rmh.place(x=150, y=2, width=60,height=50)

    
    def home_rumah(self):
        home_rmh = messagebox.askyesno("Home!", "Apakah Anda yakin ingin kembali ke halaman utama?")

        if home_rmh:
            self.frame_rmh.destroy()
            self.halaman_dekstop()
            
            pass

        else:
            self.rumah()

    
    def add_calendar_rmh(self):
        self.cal_rmh = DateEntry(self.frame_rmh, selectmode='day')
        self.cal_rmh.place(x=775, y=430)

        self.label_nomor_rmh = Label(self.frame_rmh, text="Nomor Hp")
        self.label_nomor_rmh.place(x=655, y=400)

        self.entry_nomor_rmh  = Entry(self.frame_rmh , width=40)
        self.entry_nomor_rmh.place(x=775, y=400)
       
        self.label_alamat_rmh = Label(self.frame_rmh, text="Alamat:")
        self.label_alamat_rmh.place(x=655, y=370)

        self.entry_alamat_rmh = Entry(self.frame_rmh , width=40)
        self.entry_alamat_rmh.place(x=775, y=370)

        self.label_nama_rmh  = Label(self.frame_rmh, text="Nama Pelanggan:")
        self.label_nama_rmh .place(x=655, y=340)

        self.entry_nama_rmh  = Entry(self.frame_rmh , width=40)
        self.entry_nama_rmh.place(x=775, y=340)

        self.label_jadwal_rmh = Label(self.frame_rmh, text="Jadwal (MM/DD/YY)")
        self.label_jadwal_rmh.place(x=655, y=430)

        self.label_metode_pembersihan_rmh = Label(self.frame_rmh, text="Metode Pembersihan")
        self.label_metode_pembersihan_rmh.place(x=655, y=460)

        self.btn_bayar_rmh = tk.Button(self.frame_rmh, text="Bayar", command=self.payment_rmh)
        self.btn_bayar_rmh.place(x=967, y=530)


    def show_selected_language_rumah(self):
        self.selected_language_rmh = tk.StringVar()
        self.radio_button1_rmh = tk.Radiobutton(self.frame_pay_rmh, text="Cash", variable=self.selected_language_rmh, value="Cash", command=self.show_selected_language_rumah)
        self.radio_button1_rmh.place(x=840 , y=293)

        self.radio_button2_rmh = tk.Radiobutton(self.frame_pay_rmh, text="Q-Ris", variable=self.selected_language_rmh , value="Q-Ris", command=self.show_selected_language_rumah)
        self.radio_button2_rmh.place(x=760 , y=450)

    def combo_bersih_rumah(self):
            # Combobox creation 
        self.combo_bersih_rmh = tk.StringVar() 
        self.metodechoosen_rmh = ttk.Combobox(self.frame_rmh, width = 27,state="readonly", textvariable = self.combo_bersih_rmh, values=["Pembersihan Umum", "Pembersihan Mendalam"]) 

        self.metodechoosen_rmh.place(x=775, y=460) 
        self.metodechoosen_rmh.current()

        pass

    def payment_rmh(self):
        confirm_payment = messagebox.askyesno("Konfirmasi Pembayaran", "Apakah Anda yakin ingin melakukan pembayaran?")

        if confirm_payment:
            self.frame_dsk.destroy()
            
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_pay_rmh = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_pay_rmh.place(x=0,y=0)
            self.foto=Image.open("7.png")
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_pay_rmh, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo

            self.btn_konfirmasi_rmh = tk.Button(self.frame_pay_rmh, text="Konfirmasi", command=self.konfirmasi_pesanan_rmh)
            self.btn_konfirmasi_rmh.place(x=850, y=580) 

            self.show_selected_language_rumah()
            
            pass

        else:
            self.rumah()

            pass
        
              
         
    def konfirmasi_pesanan_rmh(self):

        if self.frame_pay_rmh.destroy():
            window_kfm_rmh = tk.Toplevel(self.root)
            window_kfm_rmh.title("Konfirmasi")
        else:
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_kfm_rmh = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_kfm_rmh.place(x=0,y=0)
            self.foto=Image.open("10.png")
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_kfm_rmh, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo

        self.btn_selesai_rmh = tk.Button(self.frame_kfm_rmh, text="Finish", command=self.sukses_rumah)
        self.btn_selesai_rmh.place(x=450, y=550)

        self.add_output_rumah()

    def add_output_rumah(self):
        selected_date_rmh= self.cal_rmh.get_date()
        alamat_rmh = self.entry_alamat_rmh.get()
        metode_pembersih_rmh = self.combo_bersih_rmh.get()
        username_rmh = self.entry_nama_rmh.get()
        selected_language_rmh = self.selected_language_rmh.get()
        nomor_rmh = self.entry_nomor_rmh.get()

        output_jadwal_rmh = f"Tanggal yang dipilih : {selected_date_rmh}"
        output_label_jadwal_rmh = tk.Label(self.frame_kfm_rmh, text=output_jadwal_rmh, font= "arial 16" , bg="white" )
        output_label_jadwal_rmh.place(x=280 , y=360)

        output_alamat_rmh= f"Alamat : {alamat_rmh}"
        output_label_alamat_rmh = tk.Label(self.frame_kfm_rmh, text=output_alamat_rmh, font= "arial 16" , bg="white")
        output_label_alamat_rmh.place(x=280 , y=400)

        output_method_rmh= f"Metode Pembersihan : {metode_pembersih_rmh}"
        output_method_alamat_rmh = tk.Label(self.frame_kfm_rmh, text=output_method_rmh, font= "arial 16" , bg="white")
        output_method_alamat_rmh.place(x=280 , y=440)

        output_label_payment_pay_rmh = tk.Label(self.frame_kfm_rmh, text="Harga : Rp.350.000,00 " , font= "arial 16" , bg="white")
        output_label_payment_pay_rmh.place(x=280, y=480)

        output_nama_rmh= f"Nama pengguna : {username_rmh}"
        output_label_nama_rmh = tk.Label(self.frame_kfm_rmh, text=output_nama_rmh, font= "arial 16" , bg="white")
        output_label_nama_rmh.place(x=280 , y=320)

        output_pay_rmh= f"Pembayaran : {selected_language_rmh}"
        output_label_pay_rmh = tk.Label(self.frame_kfm_rmh, text=output_pay_rmh, font= "arial 16" , bg="white")
        output_label_pay_rmh.place(x=280 , y=520)

        output_nomor_rmh= f"Nomor HP : {nomor_rmh}"
        output_nomor_rmh = tk.Label(self.frame_kfm_rmh, text=output_nomor_rmh, font= "arial 16" , bg="white")
        output_nomor_rmh.place(x=280 , y=520)

        file_name = "output_rmh.csv"  
        with open(file_name, 'a', newline='') as file:
            fieldnames = ['Nama', 'Alamat','Jadwal','Method','Pembayaran','Nomor HP']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Nama' : username_rmh ,'Alamat' : alamat_rmh ,'Jadwal' : selected_date_rmh ,'Method' : metode_pembersih_rmh, 'Pembayaran' : selected_language_rmh, 'Nomor HP' : nomor_rmh})



    def sukses_rumah(self):
        if self.frame_kfm_rmh.destroy():
            window_reg = tk.Toplevel(self.root)
            window_reg.title("Sukses!!")
        else:
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_sukses_rmh = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_sukses_rmh.place(x=0,y=0)
            self.foto=Image.open("11.png")
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_sukses_rmh, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo


        self.sukses_rmh = tk.Button(self.frame_sukses_rmh, text="Selesai", command=self.halaman_dekstop)
        self.sukses_rmh.place(x=615, y=585)


    def other(self):

        if self.frame_dsk.destroy():
            window_oth = tk.Toplevel(self.root)
            window_oth.title("Lain - lain")
        else:
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_oth = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_oth.place(x=0,y=0)
            self.foto=Image.open("6.png")
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_oth, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo

            self.add_calendar_oth()
            self.combo_bersih_other()
            self.btn_home_other()

    def btn_home_other(self):
        image = Image.open("Home.png")
        image=image.resize((50,50))
        home = ImageTk.PhotoImage (image)
        self.btn_home_oth = tk.Button(self.frame_oth, command=self.home_other, image=home)
        self.btn_home_oth.photo=home
        self.btn_home_oth.place(x=150, y=2, width=60,height=50)

    
    def home_other(self):
        home_oth = messagebox.askyesno("Home!", "Apakah Anda yakin ingin kembali ke halaman utama?")

        if home_oth:
            self.frame_oth.destroy()
            self.halaman_dekstop()
            
            pass

        else:
            self.other()


    def combo_bersih_other(self):
            # Combobox creation 
        self.combo_bersih_oth = tk.StringVar() 
        self.metodechoosen_oth = ttk.Combobox(self.frame_oth, width = 27,state="readonly", 
                                              textvariable = self.combo_bersih_oth, 
                                              values=["Tempat Ibadah", "Gedung", "Kios"]) 

        self.metodechoosen_oth.place(x=775, y=460) 
        self.metodechoosen_oth.current()

    def add_calendar_oth(self):
        self.cal_oth = DateEntry(self.frame_oth, selectmode='day')
        self.cal_oth.place(x=775, y=430)

        self.label_nomor_oth = Label(self.frame_oth, text="Nomor Hp")
        self.label_nomor_oth.place(x=655, y=400)

        self.entry_nomor_oth = Entry(self.frame_oth , width=40)
        self.entry_nomor_oth.place(x=775, y=400)
       
        self.label_alamat_oth = Label(self.frame_oth, text="Alamat:")
        self.label_alamat_oth.place(x=655, y=370)

        self.entry_alamat_oth= Entry(self.frame_oth, width=40)
        self.entry_alamat_oth.place(x=775, y=370)

        self.label_nama_oth  = Label(self.frame_oth, text="Nama Pelanggan:")
        self.label_nama_oth.place(x=655, y=340)

        self.entry_nama_oth  = Entry(self.frame_oth , width=40)
        self.entry_nama_oth.place(x=775, y=340)

        self.label_jadwal_oth = Label(self.frame_oth, text="Jadwal (MM/DD/YY)")
        self.label_jadwal_oth.place(x=655, y=430)

        self.label_metode_pembersihan_oth= Label(self.frame_oth, text="Metode Pembersihan")
        self.label_metode_pembersihan_oth.place(x=655, y=460)

        self.btn_bayar_oth = tk.Button(self.frame_oth, text="Bayar", command=self.payment_rmh)
        self.btn_bayar_oth.place(x=967, y=530)

    def show_selected_language_other(self):
        self.selected_language_oth = tk.StringVar()
        self.radio_button1_oth = tk.Radiobutton(self.frame_pay_oth, text="Cash", variable=self.selected_language_oth, value="Cash", command=self.show_selected_language_other)
        self.radio_button1_oth.place(x=845 , y=350)

        self.radio_button2_oth= tk.Radiobutton(self.frame_pay_oth, text="Q-Ris", variable=self.selected_language_oth, value="Q-Ris", command=self.show_selected_language_other)
        self.radio_button2_oth.place(x=745 , y=500)


    def payment_oth(self):
        confirm_payment = messagebox.askyesno("Konfirmasi Pembayaran", "Apakah Anda yakin ingin melakukan pembayaran?")

        if confirm_payment:
            self.frame_dsk.destroy()
            
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_pay_oth= Frame(self.master,width=screen_width,height=screen_height)
            self.frame_pay_oth.place(x=0,y=0)
            self.foto=Image.open("7.png")
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_pay_oth, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo

            self.btn_konfirmasi_oth = tk.Button(self.frame_pay_oth, text="Konfirmasi", command=self.konfirmasi_pesanan_oth)
            self.btn_konfirmasi_oth.place(x=850, y=580)

            self.show_selected_language_other()

            pass

        else:
            self.other()

            pass

              
    def konfirmasi_pesanan_oth(self):

        if self.frame_pay_oth.destroy():
            window_kfm_oth = tk.Toplevel(self.root)
            window_kfm_oth.title("Konfirmasi")
        else:
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_kfm_oth = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_kfm_oth.place(x=0,y=0)
            self.foto=Image.open("10.png")
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_kfm_oth, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo

        self.btn_selesai_oth = tk.Button(self.frame_kfm_oth, text="Finish", command=self.sukses_other)
        self.btn_selesai_oth.place(x=600, y=550) 

        self.add_output_other()

    def add_output_other(self):
        selected_date_oth= self.cal_oth.get_date()
        alamat_oth= self.entry_alamat_oth.get()
        metode_pembersih_oth = self.combo_bersih_oth.get()
        username_oth = self.entry_nama_oth.get()
        selected_language_oth = self.selected_language_oth.get()
        nomor_oth = self.entry_nomor_oth.get()
    
        output_nama_oth= f"Nama Pelanggan : {username_oth}"
        output_label_nama_oth = tk.Label(self.frame_kfm_oth, text=output_nama_oth, font= "arial 16" , bg="white")
        output_label_nama_oth.place(x=280 , y=320)

        output_alamat_oth= f"Alamat : {alamat_oth}"
        output_label_alamat_oth= tk.Label(self.frame_kfm_oth, text=output_alamat_oth, font= "arial 16" , bg="white")
        output_label_alamat_oth.place(x=280 , y=360)

        output_jadwal_oth = f"Tanggal yang dipilih : {selected_date_oth}"
        output_label_jadwal_oth = tk.Label(self.frame_kfm_oth, text=output_jadwal_oth, font= "arial 16" , bg="white" )
        output_label_jadwal_oth.place(x=280 , y=400)

        output_label_payment_pay_oth = tk.Label(self.frame_kfm_oth, text="Harga : Rp.300.000,00 - Rp.1.500.000,00 (tergantung luas bangunan) " , font= "arial 16" , bg="white")
        output_label_payment_pay_oth.place(x=280, y=480)

        output_method_oth= f"Metode Pembersihan : {metode_pembersih_oth}"
        output_method_label_oth = tk.Label(self.frame_kfm_oth, text=output_method_oth, font= "arial 16" , bg="white")
        output_method_label_oth.place(x=280 , y=440)

        output_pay_oth= f"Pembayaran : {selected_language_oth}"
        output_method_pay_oth = tk.Label(self.frame_kfm_oth, text=output_pay_oth, font= "arial 16" , bg="white")
        output_method_pay_oth.place(x=280 , y=520)

        output_nomor_oth= f"Nomor HP : {nomor_oth}"
        output_nomor_oth = tk.Label(self.frame_kfm_oth, text=output_nomor_oth, font= "arial 16" , bg="white")
        output_nomor_oth.place(x=280 , y=550)

        file_name = "output_oth.csv"
        with open(file_name, 'a', newline='') as file:
            fieldnames = ['Nama', 'Alamat','Jadwal','Method','Pembayaran', 'Nomor HP']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Nama' : username_oth ,'Alamat' : alamat_oth ,'Jadwal' : selected_date_oth ,'Method' : metode_pembersih_oth, 'Pembayaran' : selected_language_oth, 'Nomor' : nomor_oth})


    def sukses_other(self):
        if self.frame_kfm_oth.destroy():
            window_reg = tk.Toplevel(self.root)
            window_reg.title("Sukses!!")
        else:
            self.master.resizable(width=tk.TRUE, height=tk.TRUE)
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            self.frame_sukses_oth = Frame(self.master,width=screen_width,height=screen_height)
            self.frame_sukses_oth.place(x=0,y=0)
            self.foto=Image.open("11.png") 
            self.foto=self.foto.resize((screen_width,screen_height))
            self.photoo=ImageTk.PhotoImage(self.foto)
            label_background = Label(self.frame_sukses_oth, image=self.photoo)
            label_background.place(x=0, y=0)
            label_background.photo=self.photoo

        self.sukses_oth = tk.Button(self.frame_sukses_oth, text="Selesai", command=self.halaman_dekstop)
        self.sukses_oth.place(x=615, y=585)

root = tk.Tk()
my_gui = Smart_Cleaner(root)
root.mainloop()