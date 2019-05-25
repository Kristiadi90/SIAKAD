from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
from tkinter import Tk,Button,Frame,Label,Entry,Spinbox,Menu,PhotoImage,Entry,END
import csv

root =Tk()
root.title("SIAKAD")
width = 800
height = 500
root.configure(background ="purple4")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.configure(background ="purple4")
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0,0)
#Membuat ikon
logo_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
root.tk.call('wm','iconphoto',root._w,logo_icon)
#=======================  Variabel =============================#Admin (Database)
USERNAME = StringVar()
PASSWORD = StringVar()

#PMB : Registrasi(Database1),Ijazah (Database2) & KTP (Database3)
#Tabel_Registrasi
NO1 =IntVar()
NAMA1=StringVar()
PRODI1 = StringVar()#Program Studi
PROPE1 = StringVar()#Program Pendidikan ( SARJANA)
AGAMA1=StringVar()
NOHP1=StringVar()
ALAMAT1=StringVar()
EMAIL1=StringVar()
JENKEL1=StringVar()
SEARCH1=StringVar()
temp1=StringVar()

NO1.set("")#0
NAMA1.set("")#1
PRODI1.set("")#2
PROPE1.set("")#3
AGAMA1.set("")#4
NOHP1.set("")#5
ALAMAT1.set("")#6
EMAIL1.set("")#7
JENKEL1.set("")#8

#Tabel_Ijazah(Database2)
NO2=StringVar()
NOMORPESERTA2=StringVar()#0
NOMORINDUK2=StringVar()#1
TTL2=StringVar()#3
NAMAORTU2=StringVar()#4
ASALSEKOLAH2=StringVar()#5
TAHUNLULUS2=StringVar()#6
DN2=StringVar()#7
SEARCH2=StringVar()
temp2=StringVar()

NO2.set("")#0
NOMORPESERTA2.set("")#1
NOMORINDUK2.set("")#2
TTL2.set("")#3
NAMAORTU2.set("")#4
ASALSEKOLAH2.set("")#5
TAHUNLULUS2.set("")#6
DN2.set("")#7

#Tabel_KTP (Database3)
NO3=IntVar()#0
NIK3=StringVar()#1
GOLDARAH3=StringVar()#2
RTRW3=StringVar()#3
DESA3=StringVar()#4
KECAMATAN3=StringVar()#5
SP3=StringVar()#6
PEKERJAAN3=StringVar()#7
KEWARGANEGARAAN3=StringVar()#8
BERLAKUHINGGA3=StringVar()#9
SEARCH3=StringVar()
temp3=StringVar()


NO3.set("")#0
NIK3.set("")#1
GOLDARAH3.set("")#2
RTRW3.set("")#3
DESA3.set("")#4
KECAMATAN3.set("")#5
SP3.set("")#6
PEKERJAAN3.set("")#7
KEWARGANEGARAAN3.set("")#8
BERLAKUHINGGA3.set("")#9

#Mahasiswa
#Tabel_ProfilMAHASISWA
NO4=IntVar()#0
NPM4=StringVar()#1
NAMA4=StringVar()#2
JENKEL4=StringVar()#3
PERGURUAN_TINGGI4=StringVar()#4
PRODI4=StringVar()#5
SEMESTERAWAL4=StringVar() #Tahun Ganjil/Genap
STATUSAWALMAHASIWA4=StringVar()#Alih Jenjang
STATUSMAHASISWAINI4=StringVar()#Aktif,Tidak Aktif ,Mengundurkan diri,Lulus,Tiddak Lulus,Pindah Perodi
TANGGALLULUS4=StringVar()
NOMORIJAZAH4=StringVar()
SEARCH4=StringVar()
temp4=StringVar()

NO4.set("")#0
NPM4.set("")#1
NAMA4.set("")#2
JENKEL4.set("")#3
PERGURUAN_TINGGI4.set("")#4
PRODI4.set("")#5
SEMESTERAWAL4.set("")#6
STATUSAWALMAHASIWA4.set("")#7
STATUSMAHASISWAINI4.set("")#8
TANGGALLULUS4.set("")#9
NOMORIJAZAH4.set("")#10

#Tabel_RiwayatStatusKuliah
NO5=IntVar()#0
SEMESTER5=StringVar()
STATUS5=StringVar()#Aktif,Tidak Aktif
SKS5=StringVar()
SEARCH5=StringVar()
temp5=StringVar()

NO5.set("")#0
SEMESTER5.set("")#1
STATUS5.set("")#2
SKS5.set("")#3

#Tabel_RiwayatStudi
NO6=IntVar()
NPM6=StringVar()
NAMA6=StringVar()
SEMESTER6=StringVar()
KODEMATKUL6=StringVar()
MATKUL6=StringVar()
SKS6=StringVar()
SEARCH6=StringVar()
temp6=StringVar()

NO6.set("")#0
NPM6.set("")#1
NAMA6.set("")#2
SEMESTER6.set("")#3
KODEMATKUL6.set("")#4
MATKUL6.set("")#5
SKS6.set("")#6


#Keuangan (Database7)
NO7=IntVar()
NPM7=StringVar()
NAMA7=StringVar()
WAKTU7=StringVar()
URAIAN7=StringVar()
JUMLAHDIBAYAR7=IntVar()
SISA7=IntVar()
SEARCH7=StringVar()
temp7=StringVar()

NO7.set("")#0
NPM7.set("")#1
NAMA7.set("")#2
WAKTU7.set("")#3
URAIAN7.set("")#4
JUMLAHDIBAYAR7.set("")#5
SISA7.set("")#6

#Penjadwalan
NO8=IntVar()#0
Penjadwalan8=StringVar()#1
HARI_TANGGAL_TAHUN8=StringVar()#2
JAM8=StringVar()#3
KODEMATKUL8=StringVar()#4
MATKUL8=StringVar()#5
SEMESTER8=IntVar()#6
PRODI8=StringVar()#7
PROPE8=StringVar()#8
SEARCH8=StringVar()
temp8=StringVar()

NO8.set("")#0
Penjadwalan8.set("")#1
HARI_TANGGAL_TAHUN8.set("")#2
JAM8.set("")#3
KODEMATKUL8.set("")#4
MATKUL8.set("")#5
SEMESTER8.set("")#6
PRODI8.set("")#7
PROPE8.set("")#8

#Perodi : KRS,Transkrip Nilai,
#KRS(Database9)
NO9=IntVar()#0
NPM9=StringVar()#1
NAMA9=StringVar()#2
MATKUL9=StringVar()#3
SKS9=StringVar()#4
SEMESTER9=StringVar()#5
PRODI9=StringVar()#6
PROPE9=StringVar()#7
TAHUNAKADEMIK9=StringVar()#8
SEARCH9=StringVar()
temp9=StringVar()

NO9.set("")#0
NPM9.set("")#1
NAMA9.set("")#2
MATKUL9.set("")#3
SKS9.set("")#4
SEMESTER9.set("")#5
PRODI9.set("")#6
PROPE9.set("")#7
TAHUNAKADEMIK9.set("")#8

#Transkrip_Nilai
NO10=IntVar()#0
NPM10=StringVar()#1
NAMA10=StringVar()#2
KODEMATKUL10=StringVar()#3
MATKUL10=StringVar()#4
HM10=StringVar()#5
AM10=StringVar()#6
K10=StringVar()#7
SEARCH10=StringVar()
temp10=StringVar()

NO10.set("")#0
NPM10.set("")#1
NAMA10.set("")#2
KODEMATKUL10.set("")#3
MATKUL10.set("")#4
HM10.set("")#5
AM10.set("")#6
K10.set("")#7

#Master : Dosen,Riwayat Pendidkan,Jadwal Mengajar,Riwayat Mengajar, Penilitian

#Dosen
NO_12=IntVar()
NAMA12=StringVar()
PERGURUAN_TINGGI12=StringVar()
JENKEL12=StringVar()
PENDIDIKAN_TERTINGGI12=StringVar()
STATUS_IKATAN_KERJA12=StringVar()
STATUS_AKTIVITAS12=StringVar()
SEARCH12=StringVar()
temp12=StringVar()

NO_12.set("")
NAMA12.set("")
PERGURUAN_TINGGI12.set("")
JENKEL12.set("")
PENDIDIKAN_TERTINGGI12.set("")
STATUS_IKATAN_KERJA12.set("")
STATUS_AKTIVITAS12.set("")

#Pencarian_Dosen
NO13=IntVar()
GELAR13=StringVar()
SEARCH13=StringVar()
temp13=StringVar()

NO13.set("")
GELAR13.set("")

#Riwayat Pendidkan
NO14=IntVar()
NAMA14=StringVar()
GELAR_AKADEMIK14=StringVar()
TANGGAL_IJAZAH14=StringVar()
JENJANG14=StringVar()
SEARCH14=StringVar()
temp14=StringVar()

NO14.set("")
NAMA14.set("")
GELAR_AKADEMIK14.set("")
TANGGAL_IJAZAH14.set("")
JENJANG14.set("")


#Jadwal_Mengajar 
NO15=IntVar()#0
HARI15=StringVar()#1
JAM15=StringVar()#2
KODEMATKUL15=StringVar()#3
MATKUL15=StringVar()#4
SEARCH15=StringVar()
temp15=StringVar()

NO15.set("")#0
HARI15.set("")#1
JAM15.set("")#2
KODEMATKUL15.set("")#3
MATKUL15.set("")#4

#Riwayat_Mengajar
NO16=IntVar()
SEMESTER16=StringVar()
TAHUN16=StringVar()
SEARCH16=StringVar()
temp16=StringVar()

NO16.set("")
SEMESTER16.set("")
TAHUN16.set("")

#Penilitian
NO17=IntVar()
KATEGORI_PENILITIAN17=StringVar()
JUDUL_PENILITIAN17=StringVar()
BIDANG_ILMU17=StringVar()
LEMBAGA17=StringVar()
TAHUN17=StringVar()
SEARCH17=StringVar()
temp17=StringVar()

NO17.set("")#0
KATEGORI_PENILITIAN17.set("")#1
JUDUL_PENILITIAN17.set("")#2
BIDANG_ILMU17.set("")#3
LEMBAGA17.set("")#4
TAHUN17.set("")#5

#======================================== METHODS 0 ==========================================================================================
#Data Admin
def Database():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()
		
#======================================== METHODS 1 ==========================================
#PMB : Registrasi(Database1),Ijazah(Database2)
def Database1():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_Registrasi` (NO1 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,NAMA1 TEXT,PRODI1 TEXT, PROPE1  TEXT,AGAMA1 TEXT,NOHP1 TEXT,ALAMAT1 TEXT,EMAIL1 TEXT,JENKEL1 BOOL)")

#Ijazah(Database2)
def Database2():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_Ijazah` (NO2 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,NOMORPESERTA2 TEXT,NOMORINDUK2 TEXT,TTL2  TEXT,NAMAORTU2 TEXT,ASALSEKOLAH2 TEXT,TAHUNLULUS2 TEXT,DN2 TEXT)")

#Tabel_KTP(Database3)
def Database3():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_KTP` (NO3 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,NIK3 TEXT,GOLDARAH3 TEXT,RTRW3  TEXT,DESA3 TEXT,KECAMATAN3 TEXT,SP3 TEXT,PEKERJAAN3 TEXT,KEWARGANEGARAAN3 TEXT,BERLAKUHINGGA3 TEXT)")

#Tabel_ProfillMAHASISWA(Database4)
def Database4():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_ProfillMAHASISWA` (NO4 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,NPM4 TEXT,NAMA4 TEXT,JENKEL4 TEXT,PERGURUAN_TINGGI4  TEXT,PRODI4 TEXT,SEMESTERAWAL4 TEXT,STATUSAWALMAHASIWA4 TEXT,STATUSMAHASISWAINI4 TEXT,TANGGALLULUS4 TEXT,NOMORIJAZAH4 TEXT)")

#Tabel_RiwayatStatusKuliah(Database5)
def Database5():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_RiwayatStatusKuliah` (NO5 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,SEMESTER5 TEXT,STATUS5 TEXT, SKS5 TEXT)")


#Tabel_RiwayatStudi(Database6)
def Database6():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_RiwayatStudi` (NO6 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,NPM6 TEXT,NAMA6 TEXT,SEMESTER6 TEXT,KODEMATKUL6 TEXT,MATKUL6 TEXT,SKS6 NUMERIC)")

#Tabel_Keuangan(Database7)
def Database7():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_Keuangan` (NO7 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,NPM7 TEXT,NAMA7 TEXT,WAKTU7 TEXT,URAIAN7 TEXT,JUMLAHDIBAYAR7 NUMERIC,SISA7 TEXT)")

#Tabel_Penjadwalan(Database8)
def Database8():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_Penjadwalan` (NO8 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Penjadwalan8 TEXT,HARI_TANGGAL_TAHUN8 TEXT,JAM8 TEXT,KODEMATKUL8 TEXT,MATKUL8 TEXT,SEMESTER8 TEXT,PRODI8 TEXT,PROPE8 TEXT)")

#Tabel_KRS(Database9)
def Database9():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_KRS` (NO9 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,NPM9 TEXT,NAMA9 TEXT,MATKUL9 TEXT,SKS9 TEXT,SEMESTER9 TEXT,PRODI9 TEXT,PROPE9 TEXT,TAHUNAKADEMIK9 NUMERIC)")

#Tabel_Transkrip_Nilai(Database10)
def Database10():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_Transkrip_Nilai` (NO10 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,NPM10 TEXT,NAMA10 TEXT,KODEMATKUL10 TEXT,MATKUL10 TEXT,HM10 TEXT,AM10 NUMERIC,K10 NUMERIC)")

#Tabel_Dosen(Database11)
def Database11():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_Dosen` (NO_12 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,NAMA12 TEXT,PERGURUAN_TINGGI12 TEXT,JENKEL12 TEXT,PENDIDIKAN_TERTINGGI12 TEXT,STATUS_IKATAN_KERJA12 TEXT,STATUS_AKTIVITAS12 TEXT)")

#Tabel_Pencarian_Dosen(Database12)
def Database12():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_Pencarian_Gelar` (NO13 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,GELAR13 TEXT)")

#Tabel_Riwayat_Pendidkan(Database13)
def Database13():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_Riwayat_Pendidkan` (NO14 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,NAMA14 TEXT,GELAR_AKADEMIK14 TEXT,TANGGAL_IJAZAH14 TEXT,JENJANG14 TEXT)")

#Tabel_Jadwal_Mengajar(Database14)
def Database14():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_Jadwal_Mengajar` (NO15 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,HARI15 TEXT,JAM15 TEXT,KODEMATKUL15 TEXT,MATKUL15 TEXT)")

#Tabel_Riwayat_Mengajar(Database15)
def Database15():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_Riwayat_Mengajar` (NO16 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,SEMESTER16 NUMERIC,TAHUN16 NUMERIC)")

#Tabel_Penilitian(Database16)
def Database16():
    global conn, cursor
    conn = sqlite3.connect("SIAKAD_db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tabel_Penilitian` (NO17 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,KATEGORI_PENILITIAN17 TEXT,JUDUL_PENILITIAN17 TEXT,BIDANG_ILMU17 TEXT,LEMBAGA17 TEXT,TAHUN17 NUMERIC )")

def Exit():
    result = tkMessageBox.askquestion('SIAKAD', 'Anda yakin ingin keluar?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('SIAKAD', 'Anda yakin ingin keluar?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()	

def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("SIAKAD")
#Membuat ikon
    login_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    loginform.tk.call('wm','iconphoto',loginform._w,login_icon)
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()

def LoginForm():
    global lbl_result
#atur frame
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Admin Masuk", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_text.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
#atur input nama pengguna
    lbl_username = Label(MidLoginForm, text="Nama pengguna", font=('arial', 25), bd=18)
    lbl_username.grid(row=0, column=0,sticky=W)
    lbl_username.config(foreground ="#00FFFF")
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1,sticky=W)
#atur input kata sandi
    lbl_password = Label(MidLoginForm, text="Kata sandi", font=('arial', 25), bd=18)
    lbl_password.grid(row=1,column=0,sticky=W)
    lbl_password.config(foreground ="#00FFFF")
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15,show="*")
    password.grid(row=1, column=1,sticky=W)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30,bg="#009ACD",foreground ="white", command=Login,)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)

def Home():
    global Home
    Home = Tk()
    Home.title("SIAKAD")
    width = 890
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0,1)
    Title = Frame(Home, bd=0, relief="flat")
    Title.pack(pady=10)
    lbl_display = Label(Title, text="SIAKAD", font=('arial', 26))
    lbl_display.pack()
    lbl_display.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    menubar = Menu(Home) 
    menubar.configure(foreground ="#00FFFF",background ="purple4") 
    filemenu = Menu(menubar, tearoff=0,foreground ="#00FFFF",background ="purple4")
    filemenu1 = Menu(menubar, tearoff=0,foreground ="#00FFFF",background ="purple4")#Input (PMB)
    filemenu2 = Menu(menubar, tearoff=0,foreground ="#00FFFF",background ="purple4")#Input (MAHASISWA)
    filemenu3 = Menu(menubar, tearoff=0,foreground ="#00FFFF",background ="purple4")#Input (Keuangan)
    filemenu4 = Menu(menubar, tearoff=0,foreground ="#00FFFF",background ="purple4")#Input (Penjadwalan)
    filemenu5 = Menu(menubar, tearoff=0,foreground ="#00FFFF",background ="purple4")#Input (Perodi)
    filemenu6 = Menu(menubar, tearoff=0,foreground ="#00FFFF",background ="purple4")#Input (Master)
    submenu = Menu(menubar, tearoff=0,foreground ="#00FFFF",background ="purple4")
    filemenu.add_command(label="Keluar", command=Exit2,underline=0,foreground ="#00FFFF",background ="purple4")	
    #filemenu1
    filemenu1.add_command(label="Registrasi", command=ShowAddNew1,underline=0,foreground ="#00FFFF",background ="purple4")#Registrasi
    filemenu1.add_separator()
    filemenu1.add_command(label="Ijazah SMK/SMA/MA", command=ShowAddNew2,underline=0,foreground ="#00FFFF",background ="purple4")#Ijazah
    filemenu1.add_separator()
    filemenu1.add_command(label="Gabungan Tabel Registrasi & Ijazah ",command=ShowView1,underline=0,foreground ="#00FFFF",background ="purple4")
    filemenu1.add_separator()
    filemenu1.add_command(label="KTP",command=ShowAddNew3,underline=0,foreground ="#00FFFF",background ="purple4")#KTP
    filemenu1.add_separator()
    filemenu1.add_command(label="Gabungan Tabel Registrasi & KTP ",command=ShowView2,underline=0,foreground ="#00FFFF",background ="purple4")
    #filemenu2
    filemenu2.add_command(label="Profil Mahasiswa ",command=ShowAddNew4,underline=0,foreground ="#00FFFF",background ="purple4")	
    filemenu2.add_separator()
    filemenu2.add_command(label="Riwayat Status Kuliah ",command=ShowAddNew5,underline=0,foreground ="#00FFFF",background ="purple4")
    filemenu2.add_separator()
    filemenu2.add_command(label="Gabungan Tabel Profil Mahasiswa & Riwayat Status Kuliah ",command=ShowView3,underline=0,foreground ="#00FFFF",background ="purple4")
    filemenu2.add_separator()
    filemenu2.add_command(label="Riwayat Studi",command=ShowAddNew6,underline=0,foreground ="#00FFFF",background ="purple4")
    #filemenu3
    filemenu3.add_command(label="Tambah & Lihat Data Keuangan",command=ShowAddNew7,underline=0,foreground ="#00FFFF",background ="purple4")#Keuangan
    #filemenu4
    filemenu4.add_command(label="Tambah & Lihat Data Penjadwalan",command=ShowAddNew8,underline=0,foreground ="#00FFFF",background ="purple4")#Penjadwalan
    #filemenu5
    #Perodi : KRS,Transkrip Nilai,
    filemenu5.add_command(label="KRS",command=ShowAddNew9,underline=0,foreground ="#00FFFF",background ="purple4")#Perodi
    filemenu5.add_separator()
    filemenu5.add_command(label="Gabungan Tabel Riwayat Studi & KRS",command=ShowView4,underline=0,foreground ="#00FFFF",background ="purple4")#Perodi
    filemenu5.add_separator()	
    filemenu5.add_command(label="Nilai HM,AM & K",command=ShowAddNew10,underline=0,foreground ="#00FFFF",background ="purple4")#Perodi
    filemenu5.add_separator()
    filemenu5.add_command(label="Hitung Nilai M",command=ShowView5,underline=0,foreground ="#00FFFF",background ="purple4")#Perodi
    #filemenu6
    #Master : Dosen,Jadwal Mengajar ,Riwayat Pendidkan,Riwayat Mengajar, Penilitian
    filemenu6.add_command(label="Dosen",command=ShowAddNew11,underline=0,foreground ="#00FFFF",background ="purple4")
    filemenu6.add_separator()
    filemenu6.add_command(label="Gelar",command=ShowAddNew12,underline=0,foreground ="#00FFFF",background ="purple4")
    filemenu6.add_separator()
    filemenu6.add_command(label="Gabungan Tabel Dosen & Gelar",command=ShowView6,underline=0,foreground ="#00FFFF",background ="purple4")
    filemenu6.add_separator()
    filemenu6.add_command(label="Riwayat Pendidkan",command=ShowAddNew13,underline=0,foreground ="#00FFFF",background ="purple4")
    filemenu6.add_separator()
    filemenu6.add_command(label="Jadwal Mengajar",command=ShowAddNew14,underline=0,foreground ="#00FFFF",background ="purple4")
    filemenu6.add_separator()
    filemenu6.add_command(label="Riwayat Mengajar",command=ShowAddNew15,underline=0,foreground ="#00FFFF",background ="purple4")
    filemenu6.add_separator()
    filemenu6.add_command(label="Gabungan Riwayat Pendidkan, Jadwal Mengajar,& Riwayat Mengajar",command=ShowView7,underline=0,foreground ="#00FFFF",background ="purple4")
    filemenu6.add_separator()
    filemenu6.add_command(label="Penilitian",command=ShowAddNew16,underline=0,foreground ="#00FFFF",background ="purple4") 
    filemenu6.add_separator()
    filemenu6.add_command(label="Gabungan Profil Mahasiswa,Penilitian,& Riwayat Pendidikan",command=ShowView8,underline=0,foreground ="#00FFFF",background ="purple4")
    menubar.add_cascade(label="Admin Keluar", menu=filemenu)
    menubar.add_cascade(label="Data", menu=submenu)#Data
    submenu.add_cascade(label="PMB", menu=filemenu1)#Input (PMB)
    submenu.add_separator()
    submenu.add_cascade(label="Mahasiswa", menu=filemenu2)#Input (MAHASISWA)
    submenu.add_separator()
    submenu.add_cascade(label="Keuangan", menu=filemenu3)#Input (Keuangan)
    submenu.add_separator()
    submenu.add_cascade(label="Penjadwalan", menu=filemenu4)#Input (Penjadwalan)
    submenu.add_separator()
    submenu.add_cascade(label="Perodi", menu=filemenu5)#Input (Perodi)
    submenu.add_separator()
    submenu.add_cascade(label="Master", menu=filemenu6)#Input (Master)
    Home.config(menu=menubar)
    Home.config(background ="purple4")

def ShowView8():
    global viewshow8
    viewshow8 = Toplevel()
    viewshow8.title("SIAKAD")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewshow8.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewshow8.resizable(0, 0)
    ViewShow08()
#Membuat ikon
    viewshow8_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    viewshow8.tk.call('wm','iconphoto',viewshow8._w,viewshow8_icon)
#===================================================================================================
def ViewShow08() :
    global tree4
    TopViewForm21 = Frame(viewshow8, width=600, bd=1, relief=SOLID)
    TopViewForm21.pack(side=TOP, fill=X)
    LeftViewForm21 = Frame(viewshow8, width=800)
    LeftViewForm21.pack(side=LEFT, fill=Y)
    MidViewForm21 = Frame(viewshow8, width=800)
    MidViewForm21.pack(side=RIGHT)
    lbl_text21 = Label(TopViewForm21,font=('arial', 18), width=600)
    lbl_text21.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_text21.pack(fill=X)
    lbl_txtsearch21 = Label(LeftViewForm21, text="Gabungan Profil Mahasiswa,Penilitian,& Riwayat Pendidikan", font=('arial', 10),foreground ="#FF00FF")
    lbl_txtsearch21.pack(side=TOP, anchor=W)
    scrollbarx21 = Scrollbar(LeftViewForm21, orient=HORIZONTAL)
    scrollbary21 = Scrollbar(LeftViewForm21, orient=VERTICAL)
    tree4= ttk.Treeview(LeftViewForm21, columns=("No","NPM","Nama Penulis","Program Studi","Nama Pembimbing","Kategori Penilitian","Judul Penilitian","Bidang Ilmu","Lembaga","Tahun"), selectmode="extended", height=100, yscrollcommand=scrollbary21.set, xscrollcommand=scrollbarx21.set)
    scrollbary21.config(command=tree4.yview)
    scrollbary21.pack(side=RIGHT, fill=Y)
    scrollbarx21.config(command=tree4.xview)
    scrollbarx21.pack(side=BOTTOM, fill=X)
    tree4.heading('No', text="No",anchor=W)#0
    tree4.heading('NPM', text="NPM",anchor=W)#1
    tree4.heading('Nama Penulis', text="Nama Penulis",anchor=W)#2
    tree4.heading('Program Studi', text="Program Studi",anchor=W)#3
    tree4.heading('Nama Pembimbing', text="Nama Pembimbing",anchor=W)#4
    tree4.heading('Kategori Penilitian', text="Kategori Penilitian",anchor=W)#5
    tree4.heading('Judul Penilitian', text="Judul Penilitian",anchor=W)#6
    tree4.heading('Bidang Ilmu', text="Bidang Ilmu",anchor=W)#7
    tree4.heading('Lembaga', text="Lembaga",anchor=W)#8
    tree4.heading('Tahun', text="Tahun",anchor=W)#9
    tree4.column('#0', stretch=NO, minwidth=0, width=0)
    tree4.column('#1', stretch=NO, minwidth=0, width=90)
    tree4.column('#2', stretch=NO, minwidth=0, width=90)
    tree4.column('#3', stretch=NO, minwidth=0, width=90)
    tree4.column('#4', stretch=NO, minwidth=0, width=90)
    tree4.column('#5', stretch=NO, minwidth=0, width=90)
    tree4.column('#6', stretch=NO, minwidth=0, width=90)
    tree4.column('#7', stretch=NO, minwidth=0, width=90)
    tree4.column('#8', stretch=NO, minwidth=0, width=90)
    tree4.column('#9', stretch=NO, minwidth=0, width=90)
    tree4.pack()
    DisplayData24()	

def DisplayData24():
    Database4()
    cursor.execute("SELECT Tabel_ProfillMAHASISWA.NO4,Tabel_ProfillMAHASISWA.NPM4,Tabel_ProfillMAHASISWA.NAMA4,Tabel_ProfillMAHASISWA.PRODI4,Tabel_Riwayat_Pendidkan.NAMA14,Tabel_Penilitian.KATEGORI_PENILITIAN17,Tabel_Penilitian.JUDUL_PENILITIAN17,Tabel_Penilitian.BIDANG_ILMU17,Tabel_Penilitian.LEMBAGA17,Tabel_Penilitian.TAHUN17 FROM Tabel_ProfillMAHASISWA INNER JOIN Tabel_Riwayat_Pendidkan ON Tabel_ProfillMAHASISWA.NO4=Tabel_Riwayat_Pendidkan.NO14 JOIN Tabel_Penilitian ON Tabel_Penilitian.NO17=Tabel_ProfillMAHASISWA.NO4")
    fetch = cursor.fetchall()
    for data in fetch:
        tree4.insert('', 'end', values=(data))
    cursor.close()
    conn.close()	
	
def ShowAddNew16():
    global addnewform16
    addnewform16 = Toplevel()
    addnewform16.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform16.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform16.resizable(0, 0)
    AddNewForm16()

#Membuat ikon
    addnewform16_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform16.tk.call('wm','iconphoto',addnewform16._w,addnewform16_icon)
def AddNewForm16():
#===============================Frame 14====================================================
     TopAddNew20 = Frame(addnewform16, width=300, height=400, bd=1, relief=SOLID)
     TopAddNew20.pack(side=TOP, pady=2)
     LeftAddNew20 = Frame(addnewform16, width=300, height=500, bd=8, relief="raise")
     LeftAddNew20.pack(side=LEFT)
     RightAddNew20 = Frame(addnewform16, width=300, height=600, bd=8, relief="raise")
     RightAddNew20.pack(side=RIGHT)
     Forms20 = Frame(LeftAddNew20, width=300, height=450)
     Forms20.pack(side=TOP)
     Buttons20 = Frame(LeftAddNew20,width=300, height=100, bd=8, relief="raise")
     Buttons20.pack(side=BOTTOM)
     searchframe20=Frame(RightAddNew20,bd=8,width=392,height=150,relief="raise")
     searchframe20.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
     lbl_text20 = Label(TopAddNew20, text="Data Penilitian", font=('arial', 12), width=900)
     lbl_text20.pack(fill=X)
     lbl_text20.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3) 
     lbl_NO17 = Label(Forms20, text="Nomor ", font=('arial', 12), bd=2)
     lbl_NO17.grid(row=0,column=0, sticky=W)
     lbl_NO17.config(foreground ="#00FFFF")
     NO_17 = Entry(Forms20, textvariable=NO17, font=('arial', 12), width=32,bd=2)
     NO_17.grid(row=0, column=1, sticky=W) 
     lbl_KATEGORI_PENILITIAN17 = Label(Forms20, text="Kategori Penilitian", font=('arial', 12), bd=2)
     lbl_KATEGORI_PENILITIAN17.grid(row=1,column=0, sticky=W)
     lbl_KATEGORI_PENILITIAN17.config(foreground ="#00FFFF")
     KATEGORIPENILITIAN17=ttk.Combobox(Forms20,font=('arial', 12),state ="readonly", textvariable=KATEGORI_PENILITIAN17, width=30)
     KATEGORIPENILITIAN17['values']= ("","KKP","Skripsi")
     KATEGORIPENILITIAN17.current(0) 
     KATEGORIPENILITIAN17.grid(column=1, row=1,sticky="W")
     lbl_JUDUL_PENILITIAN17 = Label(Forms20, text="Judul Penilitian", font=('arial', 12), bd=2)
     lbl_JUDUL_PENILITIAN17.grid(row=2,column=0, sticky=W)
     lbl_JUDUL_PENILITIAN17.config(foreground ="#00FFFF")	 
     JUDULPENILITIAN17 = Entry(Forms20, textvariable=JUDUL_PENILITIAN17, font=('arial', 12), width=32,bd=2)
     JUDULPENILITIAN17.grid(row=2, column=1, sticky=W)
     lbl_BIDANG_ILMU17 = Label(Forms20, text="Bidang Ilmu", font=('arial', 12), bd=2)
     lbl_BIDANG_ILMU17.grid(row=3,column=0, sticky=W)
     lbl_BIDANG_ILMU17.config(foreground ="#00FFFF")
     BIDANGILMU17 = Entry(Forms20, textvariable=BIDANG_ILMU17, font=('arial', 12), width=32,bd=2)
     BIDANGILMU17.grid(row=3, column=1, sticky=W)
     lbl_LEMBAGA17 = Label(Forms20, text="Lembaga", font=('arial', 12), bd=2)
     lbl_LEMBAGA17.grid(row=4,column=0, sticky=W)
     lbl_LEMBAGA17.config(foreground ="#00FFFF")
     LEMBAGA_17 = Entry(Forms20, textvariable=LEMBAGA17, font=('arial', 12), width=32,bd=2)
     LEMBAGA_17.grid(row=4, column=1, sticky=W)
     lbl_TAHUN17 = Label(Forms20, text="Tahun", font=('arial', 12), bd=2)
     lbl_TAHUN17.grid(row=5,column=0, sticky=W)
     lbl_TAHUN17.config(foreground ="#00FFFF")
     TAHUN_17= Spinbox(Forms20, from_=1900, to=9999, width=33,state ="readonly",textvariable=TAHUN17,bd=2)
     TAHUN_17.grid(row=5, column=1,sticky=W)
#==================================================================================================================
     btn_add16 = Button(Buttons20, text="Save",bg="#009ACD",foreground ="white", command=AddNew16,font=('arial', 12), width=30)
     btn_add16.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_search16 = Button(Buttons20, text="Pencarian", command=Search17,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_search16.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_reset16 = Button(Buttons20, text="Ulang", command=Reset17,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_reset16.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_delete16 = Button(Buttons20, text="Hapus",command=Delete17,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_delete16.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================	 
     global tree16
     lbl_txtsearch20 = Label(RightAddNew20, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
     lbl_txtsearch20.pack(side=TOP, anchor=W)
     temp17.set("NO")
     searchoptions20=OptionMenu(searchframe20,temp17,"NO","Kategori Penilitian","Tahun")
     searchoptions20.pack(side=LEFT)
     search16 = Entry(RightAddNew20, textvariable=SEARCH16, font=('arial', 15), width=10)
     search16.pack(side=TOP,  padx=10, fill=X)
     scrollbarx20 = Scrollbar(RightAddNew20, orient=HORIZONTAL)
     scrollbary20 = Scrollbar(RightAddNew20, orient=VERTICAL) 
     tree16= ttk.Treeview(RightAddNew20, columns=("NO","Kategori Penilitian","Judul Penilitian","Bidang Ilmu","Lembaga","Tahun"), selectmode="extended", height=100, yscrollcommand=scrollbary20.set, xscrollcommand=scrollbarx20.set)
     scrollbary20.config(command=tree16.yview)
     scrollbary20.pack(side=RIGHT, fill=Y)
     scrollbarx20.config(command=tree16.xview)
     scrollbarx20.pack(side=BOTTOM, fill=X)
     tree16.heading('NO', text="NO",anchor=W)#0
     tree16.heading('Kategori Penilitian', text="Kategori Penilitian",anchor=W)#1
     tree16.heading('Judul Penilitian', text="Judul Penilitian",anchor=W)#2
     tree16.heading('Bidang Ilmu', text="Bidang Ilmu",anchor=W)#3
     tree16.heading('Lembaga', text="Lembaga",anchor=W)#4
     tree16.heading('Tahun', text="Tahun",anchor=W)#5
     tree16.column('#0', stretch=NO, minwidth=0, width=0)
     tree16.column('#1', stretch=NO, minwidth=0, width=120)
     tree16.column('#2', stretch=NO, minwidth=0, width=120)
     tree16.column('#3', stretch=NO, minwidth=0, width=0)
     tree16.column('#4', stretch=NO, minwidth=0, width=120)
     tree16.column('#5', stretch=NO, minwidth=0, width=120)
     tree16.pack()
     DisplayData23() 

def AddNew16():
    Database16()
    cursor.execute("INSERT INTO `Tabel_Penilitian` (NO17,KATEGORI_PENILITIAN17,JUDUL_PENILITIAN17,BIDANG_ILMU17,LEMBAGA17,TAHUN17) VALUES(?,?,?,?,?,?)", (int(NO17.get()),str(KATEGORI_PENILITIAN17.get()),str(JUDUL_PENILITIAN17.get()),str(BIDANG_ILMU17.get()),str(LEMBAGA17.get()),str(TAHUN17.get())))
    conn.commit()
    NO17.set("")#0
    KATEGORI_PENILITIAN17.set("")#1
    JUDUL_PENILITIAN17.set("")#2
    BIDANG_ILMU17.set("")#3
    LEMBAGA17.set("")#4
    TAHUN17.set("")#5
    cursor.close()
    conn.close()
	 
def DisplayData23():
    Database16()
    cursor.execute("SELECT * FROM `Tabel_Penilitian`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree16.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search17():
    tree16.delete(*tree16.get_children())
    Database16()
    if(temp17.get()=="NO"):
      cursor.execute("SELECT * FROM 'Tabel_Penilitian' WHERE NO17 LIKE '%s' ORDER BY '' ASC" %SEARCH17.get())
    elif(temp17.get()=="Kategori Penilitian"):
      cursor.execute("SELECT * FROM 'Tabel_Penilitian' WHERE KATEGORI_PENILITIAN17 LIKE '%s' ORDER BY '' ASC" %SEARCH17.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_Penilitian' WHERE TAHUN17 LIKE '%s' ORDER BY '' ASC" %SEARCH17.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree16.insert('', 'end', values=(data))
    cursor.close()
    conn.close()	

def Delete17():
     if not tree16.selection():
        print("ERROR")
     else:
         result = tkMessageBox.askquestion('Data Penilitian', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
         if result == 'yes':
             curItem = tree16.focus()
             contents =(tree16.item(curItem))
             selecteditem = contents['values']
             tree16.delete(curItem)
             Database16()
             cursor.execute("DELETE FROM `Tabel_Penilitian` WHERE `N017` = %d" % selecteditem[0])
             conn.commit()
             cursor.close()
             conn.close()

def Reset17():
     tree16.delete(*tree16.get_children())
     DisplayData23()
     SEARCH17.set("")
	
def ShowView7():
    global viewshow7
    viewshow7 = Toplevel()
    viewshow7.title("SIAKAD")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewshow7.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewshow7.resizable(0, 0)
    ViewShow07()
#Membuat ikon
    viewshow7_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    viewshow7.tk.call('wm','iconphoto',viewshow7._w,viewshow7_icon)
#===================================================================================================
def ViewShow07() :
    global tree13
    TopViewForm19 = Frame(viewshow7, width=600, bd=1, relief=SOLID)
    TopViewForm19.pack(side=TOP, fill=X)
    LeftViewForm19 = Frame(viewshow7, width=800)
    LeftViewForm19.pack(side=LEFT, fill=Y)
    MidViewForm19 = Frame(viewshow7, width=800)
    MidViewForm19.pack(side=RIGHT)
    lbl_text19 = Label(TopViewForm19,font=('arial', 18), width=600)
    lbl_text19.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_text19.pack(fill=X)
    lbl_txtsearch19 = Label(LeftViewForm19, text="Gabungan Riwayat Pendidkan, Jadwal Mengajar,& Riwayat Mengajar", font=('arial', 10),foreground ="#FF00FF")
    lbl_txtsearch19.pack(side=TOP, anchor=W)
    scrollbarx19 = Scrollbar(LeftViewForm19, orient=HORIZONTAL)
    scrollbary19 = Scrollbar(LeftViewForm19, orient=VERTICAL)
    tree13= ttk.Treeview(LeftViewForm19, columns=("No","Nama","Hari","Jam","Kode Matkul","Matkul","Semester","Tahun"), selectmode="extended", height=100, yscrollcommand=scrollbary19.set, xscrollcommand=scrollbarx19.set)
    scrollbary19.config(command=tree13.yview)
    scrollbary19.pack(side=RIGHT, fill=Y)
    scrollbarx19.config(command=tree13.xview)
    scrollbarx19.pack(side=BOTTOM, fill=X)
    tree13.heading('No', text="No",anchor=W)#0
    tree13.heading('Nama', text="Nama",anchor=W)#1
    tree13.heading('Hari', text="Hari",anchor=W)#2
    tree13.heading('Jam', text="Jam",anchor=W)#3
    tree13.heading('Kode Matkul', text="Kode Matkul",anchor=W)#4
    tree13.heading('Matkul', text="Matkul",anchor=W)#5
    tree13.heading('Semester', text="Semester",anchor=W)#6
    tree13.heading('Tahun', text="Tahun",anchor=W)#7
    tree13.column('#0', stretch=NO, minwidth=0, width=0)
    tree13.column('#1', stretch=NO, minwidth=0, width=90)
    tree13.column('#2', stretch=NO, minwidth=0, width=90)
    tree13.column('#3', stretch=NO, minwidth=0, width=90)
    tree13.column('#4', stretch=NO, minwidth=0, width=90)
    tree13.column('#5', stretch=NO, minwidth=0, width=90)
    tree13.column('#6', stretch=NO, minwidth=0, width=90)
    tree13.column('#7', stretch=NO, minwidth=0, width=90)
    tree13.pack()
    DisplayData22()	

def DisplayData22():
    Database13()
    cursor.execute("SELECT Tabel_Riwayat_Pendidkan.NO14,Tabel_Riwayat_Pendidkan.NAMA14,Tabel_Jadwal_Mengajar.HARI15,Tabel_Jadwal_Mengajar.JAM15,Tabel_Jadwal_Mengajar.KODEMATKUL15,Tabel_Jadwal_Mengajar.MATKUL15,Tabel_Riwayat_Mengajar.SEMESTER16,Tabel_Riwayat_Mengajar.TAHUN16 FROM Tabel_Riwayat_Pendidkan INNER JOIN Tabel_Jadwal_Mengajar ON Tabel_Riwayat_Pendidkan.NO14=Tabel_Jadwal_Mengajar.NO15 JOIN Tabel_Riwayat_Mengajar ON Tabel_Riwayat_Mengajar.NO16=Tabel_Riwayat_Pendidkan.NO14")
    fetch = cursor.fetchall()
    for data in fetch:
        tree13.insert('', 'end', values=(data))
    cursor.close()
    conn.close()	
		
def ShowAddNew15():
    global addnewform15
    addnewform15 = Toplevel()
    addnewform15.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform15.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform15.resizable(0, 0)
    AddNewForm15()

#Membuat ikon
    addnewform15_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform15.tk.call('wm','iconphoto',addnewform15._w,addnewform15_icon)
def AddNewForm15():
#===============================Frame 14====================================================
     TopAddNew18 = Frame(addnewform15, width=300, height=400, bd=1, relief=SOLID)
     TopAddNew18.pack(side=TOP, pady=2)
     LeftAddNew18 = Frame(addnewform15, width=300, height=500, bd=8, relief="raise")
     LeftAddNew18.pack(side=LEFT)
     RightAddNew18 = Frame(addnewform15, width=300, height=600, bd=8, relief="raise")
     RightAddNew18.pack(side=RIGHT)
     Forms18 = Frame(LeftAddNew18, width=300, height=450)
     Forms18.pack(side=TOP)
     Buttons18 = Frame(LeftAddNew18,width=300, height=100, bd=8, relief="raise")
     Buttons18.pack(side=BOTTOM)
     searchframe18=Frame(RightAddNew18,bd=8,width=392,height=150,relief="raise")
     searchframe18.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
     lbl_text16 = Label(TopAddNew18, text="Data Riwayat Mengajar", font=('arial', 12), width=900)
     lbl_text16.pack(fill=X)
     lbl_text16.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3) 
     lbl_NO16 = Label(Forms18, text="Nomor ", font=('arial', 12), bd=2)
     lbl_NO16.grid(row=0,column=0, sticky=W)
     lbl_NO16.config(foreground ="#00FFFF")
     NO_16 = Entry(Forms18, textvariable=NO16, font=('arial', 12), width=32,bd=2)
     NO_16.grid(row=0, column=1, sticky=W) 
     lbl_SEMESTER16 = Label(Forms18, text="Semester", font=('arial', 12), bd=2)
     lbl_SEMESTER16.grid(row=1,column=0, sticky=W)
     lbl_SEMESTER16.config(foreground ="#00FFFF")
     SEMESTER_16= Spinbox(Forms18, from_=1, to=8, width=33,state ="readonly",textvariable=SEMESTER16,bd=2)
     SEMESTER_16.grid(row=1, column=1,sticky=W)
     lbl_TAHUN16 = Label(Forms18, text="Tahun", font=('arial', 12), bd=2)
     lbl_TAHUN16.grid(row=2,column=0, sticky=W)
     lbl_TAHUN16.config(foreground ="#00FFFF")
     TAHUN_16= Spinbox(Forms18, from_=2011, to=9999, width=33,state ="readonly",textvariable=TAHUN16,bd=2)
     TAHUN_16.grid(row=2, column=1,sticky=W)
#==================================================================================================================
     btn_add15 = Button(Buttons18, text="Save",bg="#009ACD",foreground ="white", command=AddNew15,font=('arial', 12), width=30)
     btn_add15.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_search15 = Button(Buttons18, text="Pencarian", command=Search16,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_search15.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_reset15 = Button(Buttons18, text="Ulang", command=Reset16,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_reset15.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_delete15 = Button(Buttons18, text="Hapus",command=Delete16,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_delete15.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================	 
     global tree15
     lbl_txtsearch15 = Label(RightAddNew18, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
     lbl_txtsearch15.pack(side=TOP, anchor=W)
     temp16.set("NO")
     searchoptions15=OptionMenu(searchframe18,temp16,"NO","Semester","Tahun")
     searchoptions15.pack(side=LEFT)
     search15 = Entry(RightAddNew18, textvariable=SEARCH16, font=('arial', 15), width=10)
     search15.pack(side=TOP,  padx=10, fill=X)
     scrollbarx18 = Scrollbar(RightAddNew18, orient=HORIZONTAL)
     scrollbary18 = Scrollbar(RightAddNew18, orient=VERTICAL)
     tree15= ttk.Treeview(RightAddNew18, columns=("NO","Semester","Tahun"), selectmode="extended", height=100, yscrollcommand=scrollbary18.set, xscrollcommand=scrollbarx18.set)
     scrollbary18.config(command=tree15.yview)
     scrollbary18.pack(side=RIGHT, fill=Y)
     scrollbarx18.config(command=tree15.xview)
     scrollbarx18.pack(side=BOTTOM, fill=X)
     tree15.heading('NO', text="NO",anchor=W)#0
     tree15.heading('Semester', text="Semester",anchor=W)#1
     tree15.heading('Tahun', text="Tahun",anchor=W)#2
     tree15.column('#0', stretch=NO, minwidth=0, width=0)
     tree15.column('#1', stretch=NO, minwidth=0, width=120)
     tree15.column('#2', stretch=NO, minwidth=0, width=120)
     tree15.pack()
     DisplayData21()  

def AddNew15():
    Database15()
    cursor.execute("INSERT INTO `Tabel_Riwayat_Mengajar` (NO16,SEMESTER16,TAHUN16 ) VALUES(?,?,?)", (int(NO16.get()),str(SEMESTER16.get()),str(TAHUN16.get())))
    conn.commit()
    NO16.set("")#0
    SEMESTER16.set("")#1
    TAHUN16.set("")#2
    cursor.close()
    conn.close()
	 
def DisplayData21():
    Database15()
    cursor.execute("SELECT * FROM `Tabel_Riwayat_Mengajar`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree15.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search16():
    tree15.delete(*tree15.get_children())
    Database15()
    if(temp16.get()=="NO"):
      cursor.execute("SELECT * FROM 'Tabel_Riwayat_Mengajar' WHERE NO16 LIKE '%s' ORDER BY '' ASC" %SEARCH16.get())
    elif(temp16.get()=="Semester"):
      cursor.execute("SELECT * FROM 'Tabel_Riwayat_Mengajar' WHERE SEMESTER16 LIKE '%s' ORDER BY '' ASC" %SEARCH16.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_Riwayat_Mengajar' WHERE TAHUN16 LIKE '%s' ORDER BY '' ASC" %SEARCH16.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree15.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
	
def Delete16():
     if not tree15.selection():
        print("ERROR")
     else:
         result = tkMessageBox.askquestion('Data Riwayat Mengajar', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
         if result == 'yes':
             curItem = tree14.focus()
             contents =(tree14.item(curItem))
             selecteditem = contents['values']
             tree15.delete(curItem)
             Database15()
             cursor.execute("DELETE FROM `Tabel_Riwayat_Mengajar` WHERE `N016` = %d" % selecteditem[0])
             conn.commit()
             cursor.close()
             conn.close()	

def Reset16():
     tree15.delete(*tree15.get_children())
     DisplayData21()
     SEARCH16.set("")
	
def ShowAddNew14():
    global addnewform14
    addnewform14 = Toplevel()
    addnewform14.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform14.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform14.resizable(0, 0)
    AddNewForm14()

#Membuat ikon
    addnewform14_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform14.tk.call('wm','iconphoto',addnewform14._w,addnewform14_icon)
def AddNewForm14():
#===============================Frame 14====================================================
     TopAddNew17 = Frame(addnewform14, width=300, height=400, bd=1, relief=SOLID)
     TopAddNew17.pack(side=TOP, pady=2)
     LeftAddNew17 = Frame(addnewform14, width=300, height=500, bd=8, relief="raise")
     LeftAddNew17.pack(side=LEFT)
     RightAddNew17 = Frame(addnewform14, width=300, height=600, bd=8, relief="raise")
     RightAddNew17.pack(side=RIGHT)
     Forms17 = Frame(LeftAddNew17, width=300, height=450)
     Forms17.pack(side=TOP)
     Buttons17 = Frame(LeftAddNew17,width=300, height=100, bd=8, relief="raise")
     Buttons17.pack(side=BOTTOM)
     searchframe17=Frame(RightAddNew17,bd=8,width=392,height=150,relief="raise")
     searchframe17.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
     lbl_text15 = Label(TopAddNew17, text="Data Jadwal Mengajar", font=('arial', 12), width=900)
     lbl_text15.pack(fill=X)
     lbl_text15.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3) 
     lbl_NO15 = Label(Forms17, text="Nomor ", font=('arial', 12), bd=2)
     lbl_NO15.grid(row=0,column=0, sticky=W)
     lbl_NO15.config(foreground ="#00FFFF")
     NO_15 = Entry(Forms17, textvariable=NO15, font=('arial', 12), width=32,bd=2)
     NO_15.grid(row=0, column=1, sticky=W) 
     lbl_HARI15= Label(Forms17, text="Hari", font=('arial', 12), bd=2)
     lbl_HARI15.grid(row=1,column=0, sticky=W)
     lbl_HARI15.config(foreground ="#00FFFF")
     HARI_15=ttk.Combobox(Forms17,font=('arial', 12),state ="readonly", textvariable=HARI15, width=30)
     HARI_15['values']= ("","Minggu","Senin","Selasa","Rabu","Kamis","Jumat","Sabtu")
     HARI_15.current(0) 
     HARI_15.grid(column=1, row=1,sticky="W")
     lbl_JAM15= Label(Forms17, text="Jam", font=('arial', 12), bd=2)
     lbl_JAM15.grid(row=2,column=0, sticky=W)
     lbl_JAM15.config(foreground ="#00FFFF")
     JAM_15=ttk.Combobox(Forms17,font=('arial', 12),state ="readonly", textvariable=JAM15, width=30)
     JAM_15['values']= ("","08.00","10.00","17.30","19.30")
     JAM_15.current(0) 
     JAM_15.grid(column=1, row=2,sticky="W")
     lbl_KODEMATKUL15= Label(Forms17, text="Kode Matkul", font=('arial', 12), bd=2)
     lbl_KODEMATKUL15.grid(row=3,column=0, sticky=W)
     lbl_KODEMATKUL15.config(foreground ="#00FFFF")
     KODE_MATKUL15 = Entry(Forms17, textvariable=KODEMATKUL15, font=('arial', 12), width=32,bd=2)
     KODE_MATKUL15.grid(row=3, column=1, sticky=W)
     lbl_MATKUL15= Label(Forms17, text="Matkul", font=('arial', 12), bd=2)
     lbl_MATKUL15.grid(row=4,column=0, sticky=W)
     lbl_MATKUL15.config(foreground ="#00FFFF")	 
     MATKUL_15 = Entry(Forms17, textvariable=MATKUL15, font=('arial', 12), width=32,bd=2)
     MATKUL_15.grid(row=4, column=1, sticky=W)
#==================================================================================================================
     btn_add14 = Button(Buttons17, text="Save",bg="#009ACD",foreground ="white", command=AddNew14,font=('arial', 12), width=30)
     btn_add14.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_search14 = Button(Buttons17, text="Pencarian", command=Search15,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_search14.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_reset14 = Button(Buttons17, text="Ulang", command=Reset15,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_reset14.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_delete14 = Button(Buttons17, text="Hapus",command=Delete15,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_delete14.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================	 
     global tree14
     lbl_txtsearch14 = Label(RightAddNew17, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
     lbl_txtsearch14.pack(side=TOP, anchor=W)
     temp15.set("NO")
     searchoptions14=OptionMenu(searchframe17,temp15,"NO","Hari","Matkul")
     searchoptions14.pack(side=LEFT)
     search14 = Entry(RightAddNew17, textvariable=SEARCH15, font=('arial', 15), width=10)
     search14.pack(side=TOP,  padx=10, fill=X)
     scrollbarx17 = Scrollbar(RightAddNew17, orient=HORIZONTAL)
     scrollbary17 = Scrollbar(RightAddNew17, orient=VERTICAL)
     tree14= ttk.Treeview(RightAddNew17, columns=("NO","Hari","Jam","Kode Matkul","Matkul"), selectmode="extended", height=100, yscrollcommand=scrollbary17.set, xscrollcommand=scrollbarx17.set)
     scrollbary17.config(command=tree14.yview)
     scrollbary17.pack(side=RIGHT, fill=Y)
     scrollbarx17.config(command=tree14.xview)
     scrollbarx17.pack(side=BOTTOM, fill=X)
     tree14.heading('NO', text="NO",anchor=W)#0
     tree14.heading('Hari', text="Hari",anchor=W)#1
     tree14.heading('Jam', text="Jam",anchor=W)#2
     tree14.heading('Kode Matkul', text="Kode Matkul",anchor=W)#3
     tree14.heading('Matkul', text="Matkul",anchor=W)#4
     tree14.column('#0', stretch=NO, minwidth=0, width=0)
     tree14.column('#1', stretch=NO, minwidth=0, width=120)
     tree14.column('#2', stretch=NO, minwidth=0, width=120)
     tree14.column('#3', stretch=NO, minwidth=0, width=120)
     tree14.column('#4', stretch=NO, minwidth=0, width=120)
     tree14.pack()
     DisplayData20()  

def AddNew14():
    Database14()
    cursor.execute("INSERT INTO `Tabel_Jadwal_Mengajar` (NO15,HARI15,JAM15,KODEMATKUL15,MATKUL15) VALUES(?,?,?,?,?)", (int(NO15.get()),str(HARI15.get()),str(JAM15.get()),str(KODEMATKUL15.get()),str(MATKUL15.get())))
    conn.commit()
    NO15.set("")#0
    HARI15.set("")#1
    JAM15.set("")#2
    KODEMATKUL15.set("")#3
    MATKUL15.set("")#4
    cursor.close()
    conn.close()

def DisplayData20():
    Database14()
    cursor.execute("SELECT * FROM `Tabel_Jadwal_Mengajar`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree14.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search15():
    tree14.delete(*tree14.get_children())
    Database14()
    if(temp15.get()=="NO"):
      cursor.execute("SELECT * FROM 'Tabel_Jadwal_Mengajar' WHERE NO15 LIKE '%s' ORDER BY '' ASC" %SEARCH15.get())
    elif(temp14.get()=="Hari"):
      cursor.execute("SELECT * FROM 'Tabel_Jadwal_Mengajar' WHERE HARI15 LIKE '%s' ORDER BY '' ASC" %SEARCH15.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_Jadwal_Mengajar' WHERE MATKUL15 LIKE '%s' ORDER BY '' ASC" %SEARCH15.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree14.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Delete15():
     if not tree14.selection():
        print("ERROR")
     else:
         result = tkMessageBox.askquestion('Data Jadwal Mengajar', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
         if result == 'yes':
             curItem = tree14.focus()
             contents =(tree14.item(curItem))
             selecteditem = contents['values']
             tree14.delete(curItem)
             Database14()
             cursor.execute("DELETE FROM `Tabel_Jadwal_Mengajar` WHERE `N015` = %d" % selecteditem[0])
             conn.commit()
             cursor.close()
             conn.close()

def Reset15():
     tree14.delete(*tree14.get_children())
     DisplayData20()
     SEARCH15.set("")

def ShowAddNew13():
    global addnewform13
    addnewform13 = Toplevel()
    addnewform13.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform13.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform13.resizable(0, 0)
    AddNewForm13()

#Membuat ikon
    addnewform13_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform13.tk.call('wm','iconphoto',addnewform13._w,addnewform13_icon)
def AddNewForm13():
#===============================Frame 13====================================================
     TopAddNew16 = Frame(addnewform13, width=300, height=400, bd=1, relief=SOLID)
     TopAddNew16.pack(side=TOP, pady=2)
     LeftAddNew16 = Frame(addnewform13, width=300, height=500, bd=8, relief="raise")
     LeftAddNew16.pack(side=LEFT)
     RightAddNew16 = Frame(addnewform13, width=300, height=600, bd=8, relief="raise")
     RightAddNew16.pack(side=RIGHT)
     Forms16 = Frame(LeftAddNew16, width=300, height=450)
     Forms16.pack(side=TOP)
     Buttons16 = Frame(LeftAddNew16,width=300, height=100, bd=8, relief="raise")
     Buttons16.pack(side=BOTTOM)
     searchframe16=Frame(RightAddNew16,bd=8,width=392,height=150,relief="raise")
     searchframe16.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
     lbl_text14 = Label(TopAddNew16, text="Data Riwayat Pendidikan", font=('arial', 12), width=900)
     lbl_text14.pack(fill=X)
     lbl_text14.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3) 
     lbl_NO14 = Label(Forms16, text="Nomor ", font=('arial', 12), bd=2)
     lbl_NO14.grid(row=0,column=0, sticky=W)
     lbl_NO14.config(foreground ="#00FFFF")
     NO_14 = Entry(Forms16, textvariable=NO14, font=('arial', 12), width=32,bd=2)
     NO_14.grid(row=0, column=1, sticky=W) 
     lbl_NAMA14 = Label(Forms16, text="Nama", font=('arial', 12), bd=2)
     lbl_NAMA14.grid(row=1,column=0, sticky=W)
     lbl_NAMA14.config(foreground ="#00FFFF")
     NAMA_14 = Entry(Forms16, textvariable=NAMA14, font=('arial', 12), width=32,bd=2)
     NAMA_14.grid(row=1, column=1, sticky=W)
     lbl_GELAR_AKADEMIK14 = Label(Forms16, text="Gelar Akademik", font=('arial', 12), bd=2)
     lbl_GELAR_AKADEMIK14.grid(row=2,column=0, sticky=W)
     lbl_GELAR_AKADEMIK14.config(foreground ="#00FFFF")	 
     GELARAKADEMIK14 = Entry(Forms16, textvariable=GELAR_AKADEMIK14, font=('arial', 12), width=32,bd=2)
     GELARAKADEMIK14.grid(row=2, column=1, sticky=W)
     lbl_TANGGAL_IJAZAH14 = Label(Forms16, text="Tahun Ijazah", font=('arial', 12), bd=2)
     lbl_TANGGAL_IJAZAH14.grid(row=3,column=0, sticky=W)
     lbl_TANGGAL_IJAZAH14.config(foreground ="#00FFFF")	 
     TANGGALIJAZAH14= Spinbox(Forms16, from_=1900, to=9999, width=33,state ="readonly",textvariable=TANGGAL_IJAZAH14,bd=2)
     TANGGALIJAZAH14.grid(row=3, column=1,sticky=W)
     lbl_JENJANG14 = Label(Forms16, text="Jenjang", font=('arial', 12), bd=2)
     lbl_JENJANG14.grid(row=4,column=0, sticky=W)
     lbl_JENJANG14.config(foreground ="#00FFFF")
     JENJANG_14=ttk.Combobox(Forms16,font=('arial', 12),state ="readonly", textvariable=JENJANG14, width=30)
     JENJANG_14['values']= ("","D3","D4","S1","S2","S3")
     JENJANG_14.current(0) 
     JENJANG_14.grid(column=1, row=4,sticky="W")
#====================================================================================================================
     btn_add13 = Button(Buttons16, text="Save",bg="#009ACD",foreground ="white", command=AddNew13,font=('arial', 12), width=30)
     btn_add13.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_search13 = Button(Buttons16, text="Pencarian", command=Search14,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_search13.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_reset13 = Button(Buttons16, text="Ulang", command=Reset14,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_reset13.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_delete13 = Button(Buttons16, text="Hapus",command=Delete14,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_delete13.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================	 
     global tree13
     lbl_txtsearch13 = Label(RightAddNew16, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
     lbl_txtsearch13.pack(side=TOP, anchor=W)
     temp14.set("NO")
     searchoptions13=OptionMenu(searchframe16,temp14,"NO","Gelar Akademik","Tahun Ijazah","Jenjang")
     searchoptions13.pack(side=LEFT)
     search13 = Entry(RightAddNew16, textvariable=SEARCH14, font=('arial', 15), width=10)
     search13.pack(side=TOP,  padx=10, fill=X)
     scrollbarx16 = Scrollbar(RightAddNew16, orient=HORIZONTAL)
     scrollbary16 = Scrollbar(RightAddNew16, orient=VERTICAL)
     tree13= ttk.Treeview(RightAddNew16, columns=("NO","Nama","Gelar Akademik","Tahun Ijazah","Jenjang"), selectmode="extended", height=100, yscrollcommand=scrollbary16.set, xscrollcommand=scrollbarx16.set)
     scrollbary16.config(command=tree13.yview)
     scrollbary16.pack(side=RIGHT, fill=Y)
     scrollbarx16.config(command=tree13.xview)
     scrollbarx16.pack(side=BOTTOM, fill=X)
     tree13.heading('NO', text="NO",anchor=W)#0
     tree13.heading('Nama', text="Nama",anchor=W)#1
     tree13.heading('Gelar Akademik', text="Gelar Akademik",anchor=W)#2
     tree13.heading('Tahun Ijazah', text="Tahun Ijazah",anchor=W)#3
     tree13.heading('Jenjang', text="Jenjang",anchor=W)#4
     tree13.column('#0', stretch=NO, minwidth=0, width=0)
     tree13.column('#1', stretch=NO, minwidth=0, width=120)
     tree13.column('#2', stretch=NO, minwidth=0, width=120)
     tree13.column('#3', stretch=NO, minwidth=0, width=120)
     tree13.column('#4', stretch=NO, minwidth=0, width=120)
     tree13.pack()
     DisplayData19()     
	 
def AddNew13():
    Database13()
    cursor.execute("INSERT INTO `Tabel_Riwayat_Pendidkan` (NO14,NAMA14,GELAR_AKADEMIK14,TANGGAL_IJAZAH14,JENJANG14 ) VALUES(?,?,?,?,?)", (int(NO14.get()),str(NAMA14.get()),str(GELAR_AKADEMIK14.get()),str(TANGGAL_IJAZAH14.get()),str(JENJANG14.get())))
    conn.commit()
    NO14.set("")#0
    NAMA14.set("")#1
    GELAR_AKADEMIK14.set("")#2
    TANGGAL_IJAZAH14.set("")#3
    JENJANG14.set("")#4
    cursor.close()
    conn.close()
	 
def DisplayData19():
    Database13()
    cursor.execute("SELECT * FROM `Tabel_Riwayat_Pendidkan`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree13.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search14():
    tree13.delete(*tree13.get_children())
    Database13()
    if(temp14.get()=="NO"):
      cursor.execute("SELECT * FROM 'Tabel_Riwayat_Pendidkan' WHERE NO14 LIKE '%s' ORDER BY '' ASC" %SEARCH14.get())
    elif(temp14.get()=="Gelar Akademik"):
      cursor.execute("SELECT * FROM 'Tabel_Riwayat_Pendidkan' WHERE GELARAKADEMIK14 LIKE '%s' ORDER BY '' ASC" %SEARCH14.get())
    elif(temp14.get()=="Tahun Ijazah"):
      cursor.execute("SELECT * FROM 'Tabel_Riwayat_Pendidkan' WHERE TANGGALIJAZAH14 LIKE '%s' ORDER BY '' ASC" %SEARCH14.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_Riwayat_Pendidkan' WHERE JENJANG14 LIKE '%s' ORDER BY '' ASC" %SEARCH14.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree13.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Delete14():
     if not tree13.selection():
        print("ERROR")
     else:
         result = tkMessageBox.askquestion('Data Riwayat Pendidikan', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
         if result == 'yes':
             curItem = tree13.focus()
             contents =(tree13.item(curItem))
             selecteditem = contents['values']
             tree13.delete(curItem)
             Database13()
             cursor.execute("DELETE FROM `Tabel_Riwayat_Pendidkan` WHERE `N014` = %d" % selecteditem[0])
             conn.commit()
             cursor.close()
             conn.close()

def Reset14():
     tree13.delete(*tree13.get_children())
     DisplayData19()
     SEARCH14.set("")

def ShowView6():
    global viewshow6
    viewshow6 = Toplevel()
    viewshow6.title("SIAKAD")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewshow6.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewshow6.resizable(0, 0)
    ViewShow06()
#Membuat ikon
    viewshow6_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    viewshow6.tk.call('wm','iconphoto',viewshow6._w,viewshow6_icon)
#===================================================================================================
def ViewShow06() :
    global tree12
    TopViewForm15 = Frame(viewshow6, width=600, bd=1, relief=SOLID)
    TopViewForm15.pack(side=TOP, fill=X)
    LeftViewForm15 = Frame(viewshow6, width=800)
    LeftViewForm15.pack(side=LEFT, fill=Y)
    MidViewForm15 = Frame(viewshow6, width=800)
    MidViewForm15.pack(side=RIGHT)
    lbl_text15 = Label(TopViewForm15,font=('arial', 18), width=600)
    lbl_text15.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_text15.pack(fill=X)
    lbl_txtsearch15 = Label(LeftViewForm15, text="Gabungan Tabel Dosen & Gelar", font=('arial', 10),foreground ="#FF00FF")
    lbl_txtsearch15.pack(side=TOP, anchor=W)
    scrollbarx15 = Scrollbar(LeftViewForm15, orient=HORIZONTAL)
    scrollbary15 = Scrollbar(LeftViewForm15, orient=VERTICAL)
    tree12= ttk.Treeview(LeftViewForm15, columns=("No","Nama","Gelar","Perguruan Tinggi","Status Keaktifan"), selectmode="extended", height=100, yscrollcommand=scrollbary15.set, xscrollcommand=scrollbarx15.set)
    scrollbary15.config(command=tree12.yview)
    scrollbary15.pack(side=RIGHT, fill=Y)
    scrollbarx15.config(command=tree12.xview)
    scrollbarx15.pack(side=BOTTOM, fill=X)
    tree12.heading('No', text="No",anchor=W)#0
    tree12.heading('Nama', text="Nama",anchor=W)#1
    tree12.heading('Gelar', text="Gelar",anchor=W)#2
    tree12.heading('Perguruan Tinggi', text="Perguruan Tinggi",anchor=W)#3
    tree12.heading('Status Keaktifan', text="Status Keaktifan",anchor=W)#4
    tree12.column('#0', stretch=NO, minwidth=0, width=0)
    tree12.column('#1', stretch=NO, minwidth=0, width=90)
    tree12.column('#2', stretch=NO, minwidth=0, width=90)
    tree12.column('#3', stretch=NO, minwidth=0, width=90)
    tree12.column('#4', stretch=NO, minwidth=0, width=90)
    tree12.pack()
    DisplayData18()	

def DisplayData18():
    Database12()
    cursor.execute("SELECT Tabel_Dosen.NO_12,Tabel_Dosen.NAMA12,Tabel_Pencarian_Gelar.GELAR13,Tabel_Dosen.PERGURUAN_TINGGI12,Tabel_Dosen.STATUS_AKTIVITAS12 FROM Tabel_Dosen INNER JOIN Tabel_Pencarian_Gelar ON Tabel_Dosen.NO_12=Tabel_Pencarian_Gelar.NO13")
    fetch = cursor.fetchall()
    for data in fetch:
        tree12.insert('', 'end', values=(data))
    cursor.close()
    conn.close()	

def ShowAddNew12():
    global addnewform12
    addnewform12 = Toplevel()
    addnewform12.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform12.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform12.resizable(0, 0)
    AddNewForm12()

#Membuat ikon
    addnewform12_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform12.tk.call('wm','iconphoto',addnewform12._w,addnewform12_icon)
def AddNewForm12():
#===============================Frame 12====================================================
     TopAddNew14 = Frame(addnewform12, width=300, height=400, bd=1, relief=SOLID)
     TopAddNew14.pack(side=TOP, pady=2)
     LeftAddNew14 = Frame(addnewform12, width=300, height=500, bd=8, relief="raise")
     LeftAddNew14.pack(side=LEFT)
     RightAddNew14 = Frame(addnewform12, width=300, height=600, bd=8, relief="raise")
     RightAddNew14.pack(side=RIGHT)
     Forms14 = Frame(LeftAddNew14, width=300, height=450)
     Forms14.pack(side=TOP)
     Buttons14 = Frame(LeftAddNew14,width=300, height=100, bd=8, relief="raise")
     Buttons14.pack(side=BOTTOM)
     searchframe14=Frame(RightAddNew14,bd=8,width=392,height=150,relief="raise")
     searchframe14.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
     lbl_text13 = Label(TopAddNew14, text="Data Gelar", font=('arial', 12), width=900)
     lbl_text13.pack(fill=X)
     lbl_text13.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3) 
     lbl_NO13 = Label(Forms14, text="Nomor ", font=('arial', 12), bd=2)
     lbl_NO13.grid(row=0,column=0, sticky=W)
     lbl_NO13.config(foreground ="#00FFFF")
     NO_13 = Entry(Forms14, textvariable=NO13, font=('arial', 12), width=32,bd=2)
     NO_13.grid(row=0, column=1, sticky=W) 
     lbl_GELAR13= Label(Forms14, text="Gelar", font=('arial', 12), bd=2)
     lbl_GELAR13.grid(row=1,column=0, sticky=W)
     lbl_GELAR13.config(foreground ="#00FFFF")
     GELAR_13 = Entry(Forms14, textvariable=GELAR13, font=('arial', 12), width=32,bd=2)
     GELAR_13.grid(row=1, column=1, sticky=W)
#=========================================================================================================
     btn_add12 = Button(Buttons14, text="Save",bg="#009ACD",foreground ="white", command=AddNew12,font=('arial', 12), width=30)
     btn_add12.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_search12 = Button(Buttons14, text="Pencarian", command=Search13,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_search12.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_reset12 = Button(Buttons14, text="Ulang", command=Reset13,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_reset12.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_delete12 = Button(Buttons14, text="Hapus",command=Delete13,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_delete12.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================	 
     global tree12
     lbl_txtsearch12 = Label(RightAddNew14, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
     lbl_txtsearch12.pack(side=TOP, anchor=W)
     temp13.set("NO")
     searchoptions12=OptionMenu(searchframe14,temp13,"NO")
     searchoptions12.pack(side=LEFT)  
     search12 = Entry(RightAddNew14, textvariable=SEARCH13, font=('arial', 15), width=10)
     search12.pack(side=TOP,  padx=10, fill=X)
     scrollbarx14 = Scrollbar(RightAddNew14, orient=HORIZONTAL)
     scrollbary14 = Scrollbar(RightAddNew14, orient=VERTICAL)
     tree12= ttk.Treeview(RightAddNew14, columns=("NO","Gelar"), selectmode="extended", height=100, yscrollcommand=scrollbary14.set, xscrollcommand=scrollbarx14.set)
     scrollbary14.config(command=tree12.yview)
     scrollbary14.pack(side=RIGHT, fill=Y)
     scrollbarx14.config(command=tree12.xview)
     scrollbarx14.pack(side=BOTTOM, fill=X)
     tree12.heading('NO', text="NO",anchor=W)#0
     tree12.heading('Gelar', text="Gelar",anchor=W)#1
     tree12.column('#0', stretch=NO, minwidth=0, width=0)
     tree12.column('#1', stretch=NO, minwidth=0, width=120)
     tree12.pack()
     DisplayData17()

def AddNew12():
    Database12()
    cursor.execute("INSERT INTO `Tabel_Pencarian_Gelar` (NO13,GELAR13) VALUES(?,?)", (int(NO13.get()),str(GELAR13.get())))
    conn.commit()
    NO13.set("")#0
    GELAR13.set("")#1
    cursor.close()
    conn.close()	 

def DisplayData17():
    Database12()
    cursor.execute("SELECT * FROM `Tabel_Pencarian_Gelar`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree12.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
	 
def Search13():
    tree12.delete(*tree12.get_children())
    Database11()
    if(temp13.get()=="NO"):
      cursor.execute("SELECT * FROM 'Tabel_Pencarian_Gelar' WHERE N013 LIKE '%s' ORDER BY '' ASC" %SEARCH13.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree12.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Delete13():
     if not tree12.selection():
        print("ERROR")
     else:
         result = tkMessageBox.askquestion('Data Pencarian Gelar', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
         if result == 'yes':
             curItem = tree12.focus()
             contents =(tree12.item(curItem))
             selecteditem = contents['values']
             tree12.delete(curItem)
             Database12()
             cursor.execute("DELETE FROM `Tabel_Pencarian_Gelar` WHERE `N013` = %d" % selecteditem[0])
             conn.commit()
             cursor.close()
             conn.close()
	 
def Reset13():
     tree12.delete(*tree12.get_children())
     DisplayData17()
     SEARCH13.set("")

	 
#Tabel_Dosen(Database11)
def ShowAddNew11():
    global addnewform11
    addnewform11 = Toplevel()
    addnewform11.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform11.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform11.resizable(0, 0)
    AddNewForm11()

#Membuat ikon
    addnewform11_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform11.tk.call('wm','iconphoto',addnewform11._w,addnewform11_icon)
def AddNewForm11():
#===============================Frame 11====================================================
     TopAddNew13 = Frame(addnewform11, width=300, height=400, bd=1, relief=SOLID)
     TopAddNew13.pack(side=TOP, pady=2)
     LeftAddNew13 = Frame(addnewform11, width=300, height=500, bd=8, relief="raise")
     LeftAddNew13.pack(side=LEFT)
     RightAddNew13 = Frame(addnewform11, width=300, height=600, bd=8, relief="raise")
     RightAddNew13.pack(side=RIGHT)
     Forms13 = Frame(LeftAddNew13, width=300, height=450)
     Forms13.pack(side=TOP)
     Buttons13 = Frame(LeftAddNew13,width=300, height=100, bd=8, relief="raise")
     Buttons13.pack(side=BOTTOM)
     searchframe13=Frame(RightAddNew13,bd=8,width=392,height=150,relief="raise")
     searchframe13.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
     lbl_text12 = Label(TopAddNew13, text="Data Dosen", font=('arial', 12), width=900)
     lbl_text12.pack(fill=X)
     lbl_text12.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)     
     lbl_N012 = Label(Forms13, text="Nomor ", font=('arial', 12), bd=2)
     lbl_N012.grid(row=0,column=0, sticky=W)
     lbl_N012.config(foreground ="#00FFFF")
     NO12 = Entry(Forms13, textvariable=NO_12, font=('arial', 12), width=32,bd=2)
     NO12.grid(row=0, column=1, sticky=W) 
     lbl_NAMA12= Label(Forms13, text="Nama", font=('arial', 12), bd=2)
     lbl_NAMA12.grid(row=1,column=0, sticky=W)
     lbl_NAMA12.config(foreground ="#00FFFF")
     NAMA_12 = Entry(Forms13, textvariable=NAMA12, font=('arial', 12), width=32,bd=2)
     NAMA_12.grid(row=1, column=1, sticky=W)
     lbl_PERGURUAN_TINGGI12= Label(Forms13, text="Perguruan Tinggi", font=('arial', 12), bd=2)
     lbl_PERGURUAN_TINGGI12.grid(row=2,column=0, sticky=W)
     lbl_PERGURUAN_TINGGI12.config(foreground ="#00FFFF")
     PERGURUANTINGGI12 = Entry(Forms13, textvariable=PERGURUAN_TINGGI12, font=('arial', 12), width=32,bd=2)
     PERGURUANTINGGI12.grid(row=2, column=1, sticky=W)
     lbl_JENKEL12= Label(Forms13, text="Jenkel", font=('arial', 12), bd=2)
     lbl_JENKEL12.grid(row=3,column=0, sticky=W)
     lbl_JENKEL12.config(foreground ="#00FFFF")
     JENKEL_12=ttk.Combobox(Forms13,font=('arial', 12),state ="readonly", textvariable=JENKEL12, width=30)
     JENKEL_12['values']= ("","P","L")
     JENKEL_12.current(0) 
     JENKEL_12.grid(column=1, row=3,sticky="W")
     lbl_PENDIDIKAN_TERTINGGI12= Label(Forms13, text="Pendidikan Tertinggi", font=('arial', 12), bd=2)
     lbl_PENDIDIKAN_TERTINGGI12.grid(row=4,column=0, sticky=W)
     lbl_PENDIDIKAN_TERTINGGI12.config(foreground ="#00FFFF")   
     PENDIDIKANTERTINGGI12=ttk.Combobox(Forms13,font=('arial', 12),state ="readonly", textvariable=PENDIDIKAN_TERTINGGI12, width=30)
     PENDIDIKANTERTINGGI12['values']= ("","D1","D2","D3","D4","S1","S2","S3")
     PENDIDIKANTERTINGGI12.current(0) 
     PENDIDIKANTERTINGGI12.grid(column=1, row=4,sticky="W")
     lbl_STATUS_IKATAN_KERJA12= Label(Forms13, text="Status Ikatan Kerja", font=('arial', 12), bd=2)
     lbl_STATUS_IKATAN_KERJA12.grid(row=5,column=0, sticky=W)
     lbl_STATUS_IKATAN_KERJA12.config(foreground ="#00FFFF") 	 
     STATUSIKATANKERJA12=ttk.Combobox(Forms13,font=('arial', 12),state ="readonly", textvariable=STATUS_IKATAN_KERJA12, width=30)
     STATUSIKATANKERJA12['values']= ("","Dosen Tetap","Dosen Tidak Tetap")
     STATUSIKATANKERJA12.current(0) 
     STATUSIKATANKERJA12.grid(column=1, row=5,sticky="W")
     lbl_STATUS_AKTIVITAS12= Label(Forms13, text="Status Aktivitas", font=('arial', 12), bd=2)
     lbl_STATUS_AKTIVITAS12.grid(row=6,column=0, sticky=W)
     lbl_STATUS_AKTIVITAS12.config(foreground ="#00FFFF") 
     STATUSAKTIVITAS12=ttk.Combobox(Forms13,font=('arial', 12),state ="readonly", textvariable=STATUS_AKTIVITAS12, width=30)
     STATUSAKTIVITAS12['values']= ("","Aktif","Tidak Aktif")
     STATUSAKTIVITAS12.current(0) 
     STATUSAKTIVITAS12.grid(column=1, row=6,sticky="W")
#=========================================================================================================
     btn_add11 = Button(Buttons13, text="Save",bg="#009ACD",foreground ="white", command=AddNew11,font=('arial', 12), width=30)
     btn_add11.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_search11 = Button(Buttons13, text="Pencarian", command=Search12,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_search11.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_reset11 = Button(Buttons13, text="Ulang", command=Reset12,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_reset11.pack(side=TOP, padx=10, pady=10, fill=X)
     btn_delete11 = Button(Buttons13, text="Hapus",command=Delete12,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
     btn_delete11.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================
     global tree11
     lbl_txtsearch11 = Label(RightAddNew13, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
     lbl_txtsearch11.pack(side=TOP, anchor=W)
     temp12.set("NO")
     searchoptions11=OptionMenu(searchframe13,temp12,"NO","Pendidikan Tertinggi","Status Ikatan Kerja","Jenkel","Status Aktivitas")
     searchoptions11.pack(side=LEFT)  
     search11 = Entry(RightAddNew13, textvariable=SEARCH12, font=('arial', 15), width=10)
     search11.pack(side=TOP,  padx=10, fill=X)
     scrollbarx13 = Scrollbar(RightAddNew13, orient=HORIZONTAL)
     scrollbary13 = Scrollbar(RightAddNew13, orient=VERTICAL)
     tree11= ttk.Treeview(RightAddNew13, columns=("NO","Nama","Perguruan Tinggi","Jenkel","Pendidikan Tertinggi","Status Ikatan Kerja","Status Aktivitas"), selectmode="extended", height=100, yscrollcommand=scrollbary13.set, xscrollcommand=scrollbarx13.set)
     scrollbary13.config(command=tree11.yview)
     scrollbary13.pack(side=RIGHT, fill=Y)
     scrollbarx13.config(command=tree11.xview)
     scrollbarx13.pack(side=BOTTOM, fill=X)
     tree11.heading('NO', text="NO",anchor=W)#0
     tree11.heading('Nama', text="Nama",anchor=W)#1
     tree11.heading('Perguruan Tinggi', text="Perguruan Tinggi",anchor=W)#2
     tree11.heading('Jenkel', text="Jenkel",anchor=W)#3
     tree11.heading('Pendidikan Tertinggi', text="Pendidikan Tertinggi",anchor=W)#4
     tree11.heading('Status Ikatan Kerja', text="Status Ikatan Kerja",anchor=W)#5
     tree11.heading('Status Aktivitas', text="Status Aktivitas",anchor=W)#6
     tree11.column('#0', stretch=NO, minwidth=0, width=0)
     tree11.column('#1', stretch=NO, minwidth=0, width=120)
     tree11.column('#2', stretch=NO, minwidth=0, width=120)
     tree11.column('#3', stretch=NO, minwidth=0, width=189)
     tree11.column('#4', stretch=NO, minwidth=0, width=120)
     tree11.column('#5', stretch=NO, minwidth=0, width=120)
     tree11.column('#6', stretch=NO, minwidth=0, width=120)
     tree11.pack()
     DisplayData16() 

def AddNew11():
    Database11()
    cursor.execute("INSERT INTO `Tabel_Dosen` (NO_12,NAMA12,PERGURUAN_TINGGI12,JENKEL12,PENDIDIKAN_TERTINGGI12,STATUS_IKATAN_KERJA12,STATUS_AKTIVITAS12) VALUES(?,?,?,?,?,?,?)", (int(NO_12.get()),str(NAMA12.get()), str(PERGURUAN_TINGGI12.get()), str(JENKEL12.get()), str(PENDIDIKAN_TERTINGGI12.get()), str(STATUS_IKATAN_KERJA12.get()),str(STATUS_AKTIVITAS12.get())))
    conn.commit()
    NO_12.set("")#0
    NAMA12.set("")#1
    PERGURUAN_TINGGI12.set("")#2
    JENKEL12.set("")#3
    PENDIDIKAN_TERTINGGI12.set("")#4
    STATUS_IKATAN_KERJA12.set("")#5
    STATUS_AKTIVITAS12.set("")#6
    cursor.close()
    conn.close()

def DisplayData16():
    Database11()
    cursor.execute("SELECT * FROM `Tabel_Dosen`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree11.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Search12():
    tree11.delete(*tree11.get_children())
    Database11()
    if(temp11.get()=="NO"):
      cursor.execute("SELECT * FROM 'Tabel_Dosen' WHERE N0_12 LIKE '%s' ORDER BY '' ASC" %SEARCH11.get())
    elif(temp11.get()=="Pendidikan Tertinggi"):
      cursor.execute("SELECT * FROM 'Tabel_Dosen' WHERE PENDIDIKAN_TERTINGGI12 LIKE '%s' ORDER BY '' ASC" %SEARCH11.get())
    elif(temp11.get()=="Status Ikatan Kerja"):
      cursor.execute("SELECT * FROM 'Tabel_Dosen' WHERE STATUS_IKATAN_KERJA12 LIKE '%s' ORDER BY '' ASC" %SEARCH11.get())
    elif(temp11.get()=="Jenkel"):
      cursor.execute("SELECT * FROM 'Tabel_Dosen' WHERE JENKEL12 LIKE '%s' ORDER BY '' ASC" %SEARCH11.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_Dosen' WHERE STATUS_AKTIVITAS12 LIKE '%s' ORDER BY '' ASC" %SEARCH11.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree11.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Delete12():
     if not tree11.selection():
        print("ERROR")
     else:
         result = tkMessageBox.askquestion('Data Dosen', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
         if result == 'yes':
             curItem = tree11.focus()
             contents =(tree11.item(curItem))
             selecteditem = contents['values']
             tree11.delete(curItem)
             Database11()
             cursor.execute("DELETE FROM `Tabel_Dosen` WHERE `NO_12` = %d" % selecteditem[0])
             conn.commit()
             cursor.close()
             conn.close()
			 
def Reset12():
     tree11.delete(*tree11.get_children())
     DisplayData16()
     SEARCH11.set("")
	 	 	
def ShowView5():
    global viewshow5
    viewshow5 = Toplevel()
    viewshow5.title("SIAKAD")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewshow5.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewshow5.resizable(0, 0)
    ViewShow05()
#Membuat ikon
    viewshow5_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    viewshow5.tk.call('wm','iconphoto',viewshow5._w,viewshow5_icon)
	
def ViewShow05() :
    global tree10
    TopViewForm12 = Frame(viewshow5, width=600, bd=1, relief=SOLID)
    TopViewForm12.pack(side=TOP, fill=X)
    LeftViewForm12 = Frame(viewshow5, width=800)
    LeftViewForm12.pack(side=LEFT, fill=Y)
    MidViewForm12 = Frame(viewshow5, width=800)
    MidViewForm12.pack(side=RIGHT)
    lbl_text12 = Label(TopViewForm12,font=('arial', 18), width=600)
    lbl_text12.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_text12.pack(fill=X)
    lbl_txtsearch12 = Label(LeftViewForm12, text="Hitung Nilai M", font=('arial', 10),foreground ="#FF00FF")
    lbl_txtsearch12.pack(side=TOP, anchor=W)
    scrollbarx12 = Scrollbar(LeftViewForm12, orient=HORIZONTAL)
    scrollbary12 = Scrollbar(LeftViewForm12, orient=VERTICAL)
    tree10= ttk.Treeview(LeftViewForm12, columns=("No","NPM","Nama","Kode Matkul","Matkul","HM","AM","K","M"), selectmode="extended", height=100, yscrollcommand=scrollbary12.set, xscrollcommand=scrollbarx12.set)
    scrollbary12.config(command=tree10.yview)
    scrollbary12.pack(side=RIGHT, fill=Y)
    scrollbarx12.config(command=tree10.xview)
    scrollbarx12.pack(side=BOTTOM, fill=X)
    tree10.heading('No', text="No",anchor=W)#0
    tree10.heading('NPM', text="NPM",anchor=W)#1
    tree10.heading('Nama', text="Nama",anchor=W)#2
    tree10.heading('Kode Matkul', text="Kode Matkul",anchor=W)#3
    tree10.heading('Matkul', text="Matkul",anchor=W)#4
    tree10.heading('HM', text="HM",anchor=W)#5
    tree10.heading('AM', text="AM",anchor=W)#6
    tree10.heading('K', text="K",anchor=W)#7
    tree10.heading('M', text="M",anchor=W)#8
    tree10.column('#0', stretch=NO, minwidth=0, width=0)
    tree10.column('#1', stretch=NO, minwidth=0, width=90)
    tree10.column('#2', stretch=NO, minwidth=0, width=90)
    tree10.column('#3', stretch=NO, minwidth=0, width=90)
    tree10.column('#4', stretch=NO, minwidth=0, width=90)
    tree10.column('#5', stretch=NO, minwidth=0, width=90)
    tree10.column('#6', stretch=NO, minwidth=0, width=90)
    tree10.column('#7', stretch=NO, minwidth=0, width=90)
    tree10.column('#8', stretch=NO, minwidth=0, width=90)
    tree10.pack()
    DisplayData15()	

def DisplayData15():
    Database10()
    cursor.execute("SELECT Tabel_Transkrip_Nilai.NO10,Tabel_Transkrip_Nilai.NPM10,Tabel_Transkrip_Nilai.NAMA10,Tabel_Transkrip_Nilai.KODEMATKUL10,Tabel_Transkrip_Nilai.MATKUL10,Tabel_Transkrip_Nilai.HM10,Tabel_Transkrip_Nilai.AM10,Tabel_Transkrip_Nilai.K10,(Tabel_Transkrip_Nilai.AM10*Tabel_Transkrip_Nilai.K10) FROM Tabel_Transkrip_Nilai")
    fetch = cursor.fetchall()
    for data in fetch:
        tree10.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

#Tabel_Transkrip_Nilai(Database10)
def ShowAddNew10():
    global addnewform10
    addnewform10 = Toplevel()
    addnewform10.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform10.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform10.resizable(0, 0)
    AddNewForm10()

#Membuat ikon
    addnewform10_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform10.tk.call('wm','iconphoto',addnewform10._w,addnewform10_icon)
def AddNewForm10():
#===============================Frame 10====================================================
    TopAddNew11 = Frame(addnewform10, width=300, height=400, bd=1, relief=SOLID)
    TopAddNew11.pack(side=TOP, pady=2)
    LeftAddNew11 = Frame(addnewform10, width=300, height=500, bd=8, relief="raise")
    LeftAddNew11.pack(side=LEFT)
    RightAddNew11 = Frame(addnewform10, width=300, height=600, bd=8, relief="raise")
    RightAddNew11.pack(side=RIGHT)
    Forms11 = Frame(LeftAddNew11, width=300, height=450)
    Forms11.pack(side=TOP)
    Buttons11 = Frame(LeftAddNew11,width=300, height=100, bd=8, relief="raise")
    Buttons11.pack(side=BOTTOM)
    searchframe11=Frame(RightAddNew11,bd=8,width=392,height=150,relief="raise")
    searchframe11.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
    lbl_text10 = Label(TopAddNew11, text="Data Nilai HM,AM & K", font=('arial', 12), width=900)
    lbl_text10.pack(fill=X)
    lbl_text10.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_NO10 = Label(Forms11, text="Nomor ", font=('arial', 12), bd=2)
    lbl_NO10.grid(row=0,column=0, sticky=W)
    lbl_NO10.config(foreground ="#00FFFF")
    NO_10 = Entry(Forms11, textvariable=NO10, font=('arial', 12), width=32,bd=2)
    NO_10.grid(row=0, column=1, sticky=W) 
    lbl_NPM10= Label(Forms11, text="NPM", font=('arial', 12), bd=2)
    lbl_NPM10.grid(row=1,column=0, sticky=W)
    lbl_NPM10.config(foreground ="#00FFFF")
    NPM_10 = Entry(Forms11, textvariable=NPM10, font=('arial', 12), width=32,bd=2)
    NPM_10.grid(row=1, column=1, sticky=W)
    lbl_NAMA10= Label(Forms11, text="Nama", font=('arial', 12), bd=2)
    lbl_NAMA10.grid(row=2,column=0, sticky=W)
    lbl_NAMA10.config(foreground ="#00FFFF")
    NAMA_10 = Entry(Forms11, textvariable=NAMA10, font=('arial', 12), width=32,bd=2)
    NAMA_10.grid(row=2, column=1, sticky=W)
    lbl_KODEMATKUL10= Label(Forms11, text="Kode Matkul", font=('arial', 12), bd=2)
    lbl_KODEMATKUL10.grid(row=3,column=0, sticky=W)
    lbl_KODEMATKUL10.config(foreground ="#00FFFF")
    KODEMATKUL_10 = Entry(Forms11, textvariable=KODEMATKUL10, font=('arial', 12), width=32,bd=2)
    KODEMATKUL_10.grid(row=3, column=1, sticky=W)
    lbl_MATKUL10= Label(Forms11, text="Matkul", font=('arial', 12), bd=2)
    lbl_MATKUL10.grid(row=4,column=0, sticky=W)
    lbl_MATKUL10.config(foreground ="#00FFFF")
    MATKUL_10 = Entry(Forms11, textvariable=MATKUL10, font=('arial', 12), width=32,bd=2)
    MATKUL_10.grid(row=4, column=1, sticky=W)
    lbl_HM10= Label(Forms11, text="HM", font=('arial', 12), bd=2)
    lbl_HM10.grid(row=5,column=0, sticky=W)
    lbl_HM10.config(foreground ="#00FFFF")
    HM_10=ttk.Combobox(Forms11,font=('arial', 12),state ="readonly", textvariable=HM10, width=30)
    HM_10['values']= ("","A","B","C","D","E")
    HM_10.current(0) 
    HM_10.grid(column=1, row=5,sticky="W")
    lbl_AM10= Label(Forms11, text="AM", font=('arial', 12), bd=2)
    lbl_AM10.grid(row=6,column=0, sticky=W)
    lbl_AM10.config(foreground ="#00FFFF")
    AM_10 = Spinbox(Forms11, from_=1, to=8, width=33,state ="readonly",textvariable=AM10,bd=2)
    AM_10.grid(row=6, column=1,sticky=W)	
    lbl_K10= Label(Forms11, text="K", font=('arial', 12), bd=2)
    lbl_K10.grid(row=7,column=0, sticky=W)
    lbl_K10.config(foreground ="#00FFFF")
    K_10 = Spinbox(Forms11, from_=1, to=8, width=33,state ="readonly",textvariable=K10,bd=2)
    K_10.grid(row=7, column=1,sticky=W)
#============================================================================================================
    btn_add10 = Button(Buttons11, text="Save",bg="#009ACD",foreground ="white", command=AddNew10,font=('arial', 12), width=30)
    btn_add10.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search10 = Button(Buttons11, text="Pencarian", command=Search10,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_search10.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset10 = Button(Buttons11, text="Ulang", command=Reset10,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_reset10.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete10 = Button(Buttons11, text="Hapus",command=Delete10,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_delete10.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================
    global tree10
    lbl_txtsearch10 = Label(RightAddNew11, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
    lbl_txtsearch10.pack(side=TOP, anchor=W)
    temp10.set("NPM")
    searchoptions10=OptionMenu(searchframe11,temp10,"NPM","HM","AM","K")
    searchoptions10.pack(side=LEFT)  
    search10 = Entry(RightAddNew11, textvariable=SEARCH10, font=('arial', 15), width=10)
    search10.pack(side=TOP,  padx=10, fill=X)
    scrollbarx11 = Scrollbar(RightAddNew11, orient=HORIZONTAL)
    scrollbary11 = Scrollbar(RightAddNew11, orient=VERTICAL)
    tree10= ttk.Treeview(RightAddNew11, columns=("NO","NPM","Nama","Kode Matkul","Matkul","HM","AM","K"), selectmode="extended", height=100, yscrollcommand=scrollbary11.set, xscrollcommand=scrollbarx11.set)
    scrollbary11.config(command=tree10.yview)
    scrollbary11.pack(side=RIGHT, fill=Y)
    scrollbarx11.config(command=tree10.xview)
    scrollbarx11.pack(side=BOTTOM, fill=X)
    tree10.heading('NO', text="NO",anchor=W)#0
    tree10.heading('NPM', text="NPM",anchor=W)#1
    tree10.heading('Nama', text="Nama",anchor=W)#2
    tree10.heading('Kode Matkul', text="Kode Matkul",anchor=W)#3
    tree10.heading('Matkul', text="Matkul",anchor=W)#4
    tree10.heading('HM', text="HM",anchor=W)#5
    tree10.heading('AM', text="AM",anchor=W)#6 
    tree10.heading('K', text="K",anchor=W)#7
    tree10.column('#0', stretch=NO, minwidth=0, width=0)
    tree10.column('#1', stretch=NO, minwidth=0, width=120)
    tree10.column('#2', stretch=NO, minwidth=0, width=120)
    tree10.column('#3', stretch=NO, minwidth=0, width=189)
    tree10.column('#4', stretch=NO, minwidth=0, width=120)
    tree10.column('#5', stretch=NO, minwidth=0, width=120)
    tree10.column('#6', stretch=NO, minwidth=0, width=189)
    tree10.column('#7', stretch=NO, minwidth=0, width=120)
    tree10.pack()
    DisplayData14() 

def AddNew10():
    Database10()
    cursor.execute("INSERT INTO `Tabel_Transkrip_Nilai` (NO10,NPM10,NAMA10,KODEMATKUL10,MATKUL10,HM10,AM10,K10) VALUES(?,?,?,?,?,?,?,?)", (int(NO10.get()),str(NPM10.get()), str(NAMA10.get()), str(KODEMATKUL10.get()), str(MATKUL10.get()), str(HM10.get()),str(AM10.get()),str(K10.get())))
    conn.commit()
    NO10.set("")#0
    NPM10.set("")#1
    NAMA10.set("")#2
    KODEMATKUL10.set("")#3
    MATKUL10.set("")#4
    HM10.set("")#5
    AM10.set("")#6
    K10.set("")#7
    cursor.close()
    conn.close()

def DisplayData14():
    Database10()
    cursor.execute("SELECT * FROM `Tabel_Transkrip_Nilai`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree10.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
			
def Search10():
    tree10.delete(*tree10.get_children())
    Database10()
    if(temp10.get()=="NPM"):
      cursor.execute("SELECT * FROM 'Tabel_Transkrip_Nilai' WHERE NPM10 LIKE '%s' ORDER BY '' ASC" %SEARCH10.get())
    elif(temp9.get()=="HM"):
      cursor.execute("SELECT * FROM 'Tabel_Transkrip_Nilai' WHERE HM10 LIKE '%s' ORDER BY '' ASC" %SEARCH10.get())
    elif(temp9.get()=="AM"):
      cursor.execute("SELECT * FROM 'Tabel_Transkrip_Nilai' WHERE AM10 LIKE '%s' ORDER BY '' ASC" %SEARCH10.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_Transkrip_Nilai' WHERE K10 LIKE '%s' ORDER BY '' ASC" %SEARCH10.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree10.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
	
def Delete10():
    if not tree10.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Data Transkrip Nilai', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
        if result == 'yes':
            curItem = tree10.focus()
            contents =(tree10.item(curItem))
            selecteditem = contents['values']
            tree10.delete(curItem)
            Database10()
            cursor.execute("DELETE FROM `Tabel_Transkrip_Nilai` WHERE `NO10` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def Reset10():
    tree10.delete(*tree10.get_children())
    DisplayData14()
    SEARCH10.set("")

def ShowView4():
    global viewshow4
    viewshow4 = Toplevel()
    viewshow4.title("SIAKAD")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewshow4.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewshow4.resizable(0, 0)
    ViewShow04()
#Membuat ikon
    viewshow4_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    viewshow4.tk.call('wm','iconphoto',viewshow4._w,viewshow4_icon)

def ViewShow04() :
    global tree6
    TopViewForm10 = Frame(viewshow4, width=600, bd=1, relief=SOLID)
    TopViewForm10.pack(side=TOP, fill=X)
    LeftViewForm10 = Frame(viewshow4, width=800)
    LeftViewForm10.pack(side=LEFT, fill=Y)
    MidViewForm10 = Frame(viewshow4, width=800)
    MidViewForm10.pack(side=RIGHT)
    lbl_text10 = Label(TopViewForm10,font=('arial', 18), width=600)
    lbl_text10.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_text10.pack(fill=X)
    lbl_txtsearch10 = Label(LeftViewForm10, text="Gabungan Tabel Status Studi & KRS", font=('arial', 10),foreground ="#FF00FF")
    lbl_txtsearch10.pack(side=TOP, anchor=W)
    scrollbarx10 = Scrollbar(LeftViewForm10, orient=HORIZONTAL)
    scrollbary10 = Scrollbar(LeftViewForm10, orient=VERTICAL)	
    tree6= ttk.Treeview(LeftViewForm10, columns=("No","NPM","Nama","Program Pendidikan","Program Studi","Semester","Kode Matkul","Matkul","SKS","Tahun Akademik"), selectmode="extended", height=100, yscrollcommand=scrollbary10.set, xscrollcommand=scrollbarx10.set)
    scrollbary10.config(command=tree6.yview)
    scrollbary10.pack(side=RIGHT, fill=Y)
    scrollbarx10.config(command=tree6.xview)
    scrollbarx10.pack(side=BOTTOM, fill=X)
    tree6.heading('No', text="No",anchor=W)#0
    tree6.heading('NPM', text="NPM",anchor=W)#1
    tree6.heading('Nama', text="Nama",anchor=W)#2
    tree6.heading('Program Pendidikan', text="Program Pendidikan",anchor=W)#3
    tree6.heading('Program Studi', text="Program Studi",anchor=W)#4
    tree6.heading('Semester', text="Semester",anchor=W)#5
    tree6.heading('Kode Matkul', text="Kode Matkul",anchor=W)#6
    tree6.heading('Matkul', text="Matkul",anchor=W)#7
    tree6.heading('SKS', text="SKS",anchor=W)#8
    tree6.heading('Tahun Akademik', text="Tahun Akademik",anchor=W)#9
    tree6.column('#0', stretch=NO, minwidth=0, width=0)
    tree6.column('#1', stretch=NO, minwidth=0, width=90)
    tree6.column('#2', stretch=NO, minwidth=0, width=90)
    tree6.column('#3', stretch=NO, minwidth=0, width=90)
    tree6.column('#4', stretch=NO, minwidth=0, width=90)
    tree6.column('#5', stretch=NO, minwidth=0, width=90)
    tree6.column('#6', stretch=NO, minwidth=0, width=90)
    tree6.column('#7', stretch=NO, minwidth=0, width=90)
    tree6.column('#8', stretch=NO, minwidth=0, width=90)
    tree6.column('#9', stretch=NO, minwidth=0, width=90)
    tree6.pack()
    DisplayData13()

def DisplayData13():
    Database6()
    cursor.execute("SELECT Tabel_RiwayatStudi.NO6,Tabel_RiwayatStudi.NPM6,Tabel_RiwayatStudi.NAMA6,Tabel_KRS.PRODI9,Tabel_KRS.PROPE9,Tabel_KRS.SEMESTER9,Tabel_RiwayatStudi.KODEMATKUL6,Tabel_RiwayatStudi.MATKUL6,Tabel_RiwayatStudi.SKS6,Tabel_KRS.TAHUNAKADEMIK9 FROM Tabel_KRS INNER JOIN Tabel_RiwayatStudi ON Tabel_KRS.NO9=Tabel_RiwayatStudi.NO6")
    fetch = cursor.fetchall()
    for data in fetch:
        tree6.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


#Tabel_KRS(Database9)
def ShowAddNew9():
    global addnewform9
    addnewform9 = Toplevel()
    addnewform9.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform9.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform9.resizable(0, 0)
    AddNewForm9()

#Membuat ikon
    addnewform9_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform9.tk.call('wm','iconphoto',addnewform9._w,addnewform9_icon)
def AddNewForm9():
#===============================Frame 09====================================================
    TopAddNew9 = Frame(addnewform9, width=300, height=400, bd=1, relief=SOLID)
    TopAddNew9.pack(side=TOP, pady=2)
    LeftAddNew9 = Frame(addnewform9, width=300, height=500, bd=8, relief="raise")
    LeftAddNew9.pack(side=LEFT)
    RightAddNew9 = Frame(addnewform9, width=300, height=600, bd=8, relief="raise")
    RightAddNew9.pack(side=RIGHT)
    Forms9 = Frame(LeftAddNew9, width=300, height=450)
    Forms9.pack(side=TOP)
    Buttons9 = Frame(LeftAddNew9,width=300, height=100, bd=8, relief="raise")
    Buttons9.pack(side=BOTTOM)
    searchframe9=Frame(RightAddNew9,bd=8,width=392,height=150,relief="raise")
    searchframe9.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
    lbl_text9 = Label(TopAddNew9, text="Data KRS", font=('arial', 12), width=900)
    lbl_text9.pack(fill=X)
    lbl_text9.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_NO9 = Label(Forms9, text="Nomor ", font=('arial', 12), bd=2)
    lbl_NO9.grid(row=0,column=0, sticky=W)
    lbl_NO9.config(foreground ="#00FFFF")
    NO_9 = Entry(Forms9, textvariable=NO9, font=('arial', 12), width=32,bd=2)
    NO_9.grid(row=0, column=1, sticky=W) 
    lbl_NPM9= Label(Forms9, text="NPM", font=('arial', 12), bd=2)
    lbl_NPM9.grid(row=1,column=0, sticky=W)
    lbl_NPM9.config(foreground ="#00FFFF")
    NPM_9 = Entry(Forms9, textvariable=NPM9, font=('arial', 12), width=32,bd=2)
    NPM_9.grid(row=1, column=1, sticky=W)
    lbl_NAMA9= Label(Forms9, text="Nama", font=('arial', 12), bd=2)
    lbl_NAMA9.grid(row=2,column=0, sticky=W)
    lbl_NAMA9.config(foreground ="#00FFFF")	
    NAMA_9 = Entry(Forms9, textvariable=NAMA9, font=('arial', 12), width=32,bd=2)
    NAMA_9.grid(row=2, column=1, sticky=W)
    lbl_MATKUL9= Label(Forms9, text="Matkul", font=('arial', 12), bd=2)
    lbl_MATKUL9.grid(row=3,column=0, sticky=W)
    lbl_MATKUL9.config(foreground ="#00FFFF")
    MATKUL_9 = Entry(Forms9, textvariable=MATKUL9, font=('arial', 12), width=32,bd=2)
    MATKUL_9.grid(row=3, column=1, sticky=W)
    lbl_SKS9= Label(Forms9, text="SKS", font=('arial', 12), bd=2)
    lbl_SKS9.grid(row=4,column=0, sticky=W)
    lbl_SKS9.config(foreground ="#00FFFF")
    SKS_9 = Spinbox(Forms9, from_=1, to=6, width=33,state ="readonly",textvariable=SKS9,bd=2)
    SKS_9.grid(row=4, column=1,sticky=W)
    lbl_SEMESTER9= Label(Forms9, text="Semester", font=('arial', 12), bd=2)
    lbl_SEMESTER9.grid(row=5,column=0, sticky=W)
    lbl_SEMESTER9.config(foreground ="#00FFFF")
    SEMESTER_9= Spinbox(Forms9, from_=1, to=8, width=33,state ="readonly",textvariable=SEMESTER9,bd=2)
    SEMESTER_9.grid(row=5, column=1,sticky=W)
    lbl_PRODI9= Label(Forms9, text="Program Studi", font=('arial', 12), bd=2)
    lbl_PRODI9.grid(row=6,column=0, sticky=W)
    lbl_PRODI9.config(foreground ="#00FFFF")
    PRODI_9=ttk.Combobox(Forms9,font=('arial', 12),state ="readonly", textvariable=PRODI9, width=30)
    PRODI_9['values']= ("","IT","SI")
    PRODI_9.current(0) 
    PRODI_9.grid(column=1, row=6,sticky="W")
    lbl_PROPE9= Label(Forms9, text="Program Pendidikan", font=('arial', 12), bd=2)
    lbl_PROPE9.grid(row=7,column=0, sticky=W)
    lbl_PROPE9.config(foreground ="#00FFFF")
    PROPE_9=ttk.Combobox(Forms9,font=('arial', 12),state ="readonly", textvariable=PROPE9, width=30)
    PROPE_9['values']= ("","S1","Profesi 2 tahun","D3")
    PROPE_9.current(0) 
    PROPE_9.grid(column=1, row=7,sticky="W")
    lbl_TAHUNAKADEMIK9= Label(Forms9, text="Tahun Akademik", font=('arial', 12), bd=2)
    lbl_TAHUNAKADEMIK9.grid(row=8,column=0, sticky=W)
    lbl_TAHUNAKADEMIK9.config(foreground ="#00FFFF")
    TAHUNAKADEMIK_9= Spinbox(Forms9, from_=2013, to=9999, width=33,state ="readonly",textvariable=TAHUNAKADEMIK9,bd=2)
    TAHUNAKADEMIK_9.grid(row=8, column=1,sticky=W)
#============================================================================================================
    btn_add9 = Button(Buttons9, text="Save",bg="#009ACD",foreground ="white", command=AddNew9,font=('arial', 12), width=30)
    btn_add9.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search9 = Button(Buttons9, text="Pencarian", command=Search9,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_search9.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset9 = Button(Buttons9, text="Ulang", command=Reset9,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_reset9.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete9 = Button(Buttons9, text="Hapus",command=Delete9,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_delete9.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================  
    global tree9
    lbl_txtsearch9 = Label(RightAddNew9, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
    lbl_txtsearch9.pack(side=TOP, anchor=W)
    temp9.set("NPM")
    searchoptions9=OptionMenu(searchframe9,temp9,"NPM","Semester","Tahun Akademik","Program Studi","Program Pendidikan")
    searchoptions9.pack(side=LEFT)
    search9 = Entry(RightAddNew9, textvariable=SEARCH9, font=('arial', 15), width=10)
    search9.pack(side=TOP,  padx=10, fill=X)
    scrollbarx9 = Scrollbar(RightAddNew9, orient=HORIZONTAL)
    scrollbary9 = Scrollbar(RightAddNew9, orient=VERTICAL)
    tree9= ttk.Treeview(RightAddNew9, columns=("NO","NPM","Nama","Matkul","SKS","Semester","Program Studi","Program Pendidikan","Tahun Akademik"), selectmode="extended", height=100, yscrollcommand=scrollbary9.set, xscrollcommand=scrollbarx9.set)
    scrollbary9.config(command=tree9.yview)
    scrollbary9.pack(side=RIGHT, fill=Y)
    scrollbarx9.config(command=tree9.xview)
    scrollbarx9.pack(side=BOTTOM, fill=X)
    tree9.heading('NO', text="NO",anchor=W)#0
    tree9.heading('NPM', text="NPM",anchor=W)#1
    tree9.heading('Nama', text="Nama",anchor=W)#2
    tree9.heading('Matkul', text="Matkul",anchor=W)#3
    tree9.heading('SKS', text="SKS",anchor=W)#4
    tree9.heading('Semester', text="Semester",anchor=W)#5
    tree9.heading('Program Studi', text="Program Studi",anchor=W)#6 
    tree9.heading('Program Pendidikan', text="Program Pendidikan",anchor=W)#7
    tree9.heading('Tahun Akademik', text="Tahun Akademik",anchor=W)#8 	
    tree9.column('#0', stretch=NO, minwidth=0, width=0)
    tree9.column('#1', stretch=NO, minwidth=0, width=120)
    tree9.column('#2', stretch=NO, minwidth=0, width=120)
    tree9.column('#3', stretch=NO, minwidth=0, width=189)
    tree9.column('#4', stretch=NO, minwidth=0, width=120)
    tree9.column('#5', stretch=NO, minwidth=0, width=120)
    tree9.column('#6', stretch=NO, minwidth=0, width=189)
    tree9.column('#7', stretch=NO, minwidth=0, width=120)
    tree9.column('#8', stretch=NO, minwidth=0, width=120)
    tree9.pack()
    DisplayData12() 

def AddNew9():
    Database9()
    cursor.execute("INSERT INTO `Tabel_KRS` (NO9,NPM9,NAMA9,MATKUL9,SKS9,SEMESTER9,PRODI9,PROPE9,TAHUNAKADEMIK9) VALUES(?,?,?,?,?,?,?,?,?)", (int(NO9.get()),str(NPM9.get()), str(NAMA9.get()), str(MATKUL9.get()), str(SKS9.get()), str(SEMESTER9.get()),str(PRODI9.get()),str(PROPE9.get()),str(TAHUNAKADEMIK9.get())))
    conn.commit()
    NO9.set("")#0
    NPM9.set("")#1
    NAMA9.set("")#2
    MATKUL9.set("")#3
    SKS9.set("")#4
    SEMESTER9.set("")#5
    PRODI9.set("")#6
    PROPE9.set("")#7
    TAHUNAKADEMIK9.set("")#8
    cursor.close()
    conn.close()

def DisplayData12():
    Database9()
    cursor.execute("SELECT * FROM `Tabel_KRS`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree9.insert('', 'end', values=(data))
    cursor.close()
    conn.close()	


def Search9():
    tree9.delete(*tree9.get_children())
    Database9()
    if(temp9.get()=="NPM"):
      cursor.execute("SELECT * FROM 'Tabel_KRS' WHERE NPM9 LIKE '%s' ORDER BY '' ASC" %SEARCH9.get())
    elif(temp9.get()=="Semester"):
      cursor.execute("SELECT * FROM 'Tabel_KRS' WHERE SEMESTER9 LIKE '%s' ORDER BY '' ASC" %SEARCH9.get())
    elif(temp9.get()=="Tahun Akademik"):
      cursor.execute("SELECT * FROM 'Tabel_KRS' WHERE TAHUNAKADEMIK9 LIKE '%s' ORDER BY '' ASC" %SEARCH9.get())
    elif(temp9.get()=="Program Studi"):
      cursor.execute("SELECT * FROM 'Tabel_KRS' WHERE PRODI9 LIKE '%s' ORDER BY '' ASC" %SEARCH9.get())  
    else:
      cursor.execute("SELECT * FROM 'Tabel_KRS' WHERE PROPE9 LIKE '%s' ORDER BY '' ASC" %SEARCH9.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree9.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Delete9():
    if not tree9.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Data KRS', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
        if result == 'yes':
            curItem = tree9.focus()
            contents =(tree9.item(curItem))
            selecteditem = contents['values']
            tree9.delete(curItem)
            Database9()
            cursor.execute("DELETE FROM `Tabel_KRS` WHERE `NO9` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def Reset9():
    tree9.delete(*tree9.get_children())
    DisplayData12()
    SEARCH9.set("")

#Tabel_Penjadwalan(Database8)
def ShowAddNew8():
    global addnewform8
    addnewform8 = Toplevel()
    addnewform8.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform8.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform8.resizable(0, 0)
    AddNewForm8()

#Membuat ikon
    addnewform8_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform8.tk.call('wm','iconphoto',addnewform8._w,addnewform8_icon)
def AddNewForm8():
#===============================Frame 08====================================================
    TopAddNew8 = Frame(addnewform8, width=300, height=400, bd=1, relief=SOLID)
    TopAddNew8.pack(side=TOP, pady=2)
    LeftAddNew8 = Frame(addnewform8, width=300, height=500, bd=8, relief="raise")
    LeftAddNew8.pack(side=LEFT)
    RightAddNew8 = Frame(addnewform8, width=300, height=600, bd=8, relief="raise")
    RightAddNew8.pack(side=RIGHT)
    Forms8 = Frame(LeftAddNew8, width=300, height=450)
    Forms8.pack(side=TOP)
    Buttons8 = Frame(LeftAddNew8,width=300, height=100, bd=8, relief="raise")
    Buttons8.pack(side=BOTTOM)
    searchframe8=Frame(RightAddNew8,bd=8,width=392,height=150,relief="raise")
    searchframe8.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
    lbl_text8 = Label(TopAddNew8, text="Data Penjadwalan", font=('arial', 12), width=900)
    lbl_text8.pack(fill=X)
    lbl_text8.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_NO8 = Label(Forms8, text="Nomor ", font=('arial', 12), bd=2)
    lbl_NO8.grid(row=0,column=0, sticky=W)
    lbl_NO8.config(foreground ="#00FFFF")
    NO_8 = Entry(Forms8, textvariable=NO8, font=('arial', 12), width=32,bd=2)
    NO_8.grid(row=0, column=1, sticky=W) 
    lbl_Penjadwalan8= Label(Forms8, text="Penjadwalan", font=('arial', 12), bd=2)
    lbl_Penjadwalan8.grid(row=1,column=0, sticky=W)
    lbl_Penjadwalan8.config(foreground ="#00FFFF") 
    Penjadwalan_8=ttk.Combobox(Forms8,font=('arial', 12),state ="readonly", textvariable=Penjadwalan8, width=30)
    Penjadwalan_8['values']= ("","Kuliah","UTS","UAS")
    Penjadwalan_8.current(0) 
    Penjadwalan_8.grid(column=1, row=1,sticky="W")
    lbl_HARI_TANGGAL_TAHUN8= Label(Forms8, text="Hari,Tanggal,Bulan & Tahun", font=('arial', 12), bd=2)
    lbl_HARI_TANGGAL_TAHUN8.grid(row=2,column=0, sticky=W)
    lbl_HARI_TANGGAL_TAHUN8.config(foreground ="#00FFFF")
    HARI_TANGGAL_TAHUN_8 = Entry(Forms8, textvariable=HARI_TANGGAL_TAHUN8, font=('arial', 12), width=32,bd=2)
    HARI_TANGGAL_TAHUN_8.grid(row=2, column=1, sticky=W)
    lbl_JAM8= Label(Forms8, text="Jam", font=('arial', 12), bd=2)
    lbl_JAM8.grid(row=3,column=0, sticky=W)
    lbl_JAM8.config(foreground ="#00FFFF")
    JAM_8=ttk.Combobox(Forms8,font=('arial', 12),state ="readonly", textvariable=JAM8, width=30)
    JAM_8['values']= ("","08.00","10.00","17.30","19.30")
    JAM_8.current(0) 
    JAM_8.grid(column=1, row=3,sticky="W")	
    lbl_KODEMATKUL8= Label(Forms8, text="Kode Matkul", font=('arial', 12), bd=2)
    lbl_KODEMATKUL8.grid(row=4,column=0, sticky=W)
    lbl_KODEMATKUL8.config(foreground ="#00FFFF")
    KODEMATKUL_8 = Entry(Forms8, textvariable=KODEMATKUL8, font=('arial', 12), width=32,bd=2)
    KODEMATKUL_8.grid(row=4, column=1, sticky=W)
    lbl_MATKUL8= Label(Forms8, text="Matkul", font=('arial', 12), bd=2)
    lbl_MATKUL8.grid(row=5,column=0, sticky=W)
    lbl_MATKUL8.config(foreground ="#00FFFF")
    MATKUL_8 = Entry(Forms8, textvariable=MATKUL8, font=('arial', 12), width=32,bd=2)
    MATKUL_8.grid(row=5, column=1, sticky=W)
    lbl_SEMESTER8= Label(Forms8, text="Semester", font=('arial', 12), bd=2)
    lbl_SEMESTER8.grid(row=6,column=0, sticky=W)
    lbl_SEMESTER8.config(foreground ="#00FFFF")
    SEMESTER_8 = Spinbox(Forms8, from_=1, to=8, width=33,state ="readonly",textvariable=SEMESTER8,bd=2)
    SEMESTER_8.grid(row=6, column=1,sticky=W)	
    lbl_PRODI8= Label(Forms8, text="Program Studi", font=('arial', 12), bd=2)
    lbl_PRODI8.grid(row=7,column=0, sticky=W)
    lbl_PRODI8.config(foreground ="#00FFFF")
    PRODI_8=ttk.Combobox(Forms8,font=('arial', 12),state ="readonly", textvariable=PRODI8, width=30)
    PRODI_8['values']= ("","IT","SI")
    PRODI_8.current(0) 
    PRODI_8.grid(column=1, row=7,sticky="W")
    lbl_PROPE8= Label(Forms8, text="Program Pendidikan", font=('arial', 12), bd=2)
    lbl_PROPE8.grid(row=8,column=0, sticky=W)
    lbl_PROPE8.config(foreground ="#00FFFF")
    PROPE_8=ttk.Combobox(Forms8,font=('arial', 12),state ="readonly", textvariable=PROPE8, width=30)
    PROPE_8['values']= ("","S1","Profesi 2 tahun","D3")
    PROPE_8.current(0) 
    PROPE_8.grid(column=1, row=8,sticky="W")
#============================================================================================================
    btn_add8 = Button(Buttons8, text="Save",bg="#009ACD",foreground ="white", command=AddNew8,font=('arial', 12), width=30)
    btn_add8.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search8 = Button(Buttons8, text="Pencarian", command=Search8,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_search8.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset8 = Button(Buttons8, text="Ulang", command=Reset8,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_reset8.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete8 = Button(Buttons8, text="Hapus",command=Delete8,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_delete8.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================    
    global tree8
    lbl_txtsearch8 = Label(RightAddNew8, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
    lbl_txtsearch8.pack(side=TOP, anchor=W)
    temp8.set("Penjadwalan")
    searchoptions8=OptionMenu(searchframe8,temp8,"Penjadwalan","Program Studi","Program Studi")
    searchoptions8.pack(side=LEFT)
    search8 = Entry(RightAddNew8, textvariable=SEARCH8, font=('arial', 15), width=10)
    search8.pack(side=TOP,  padx=10, fill=X)
    scrollbarx8 = Scrollbar(RightAddNew8, orient=HORIZONTAL)
    scrollbary8 = Scrollbar(RightAddNew8, orient=VERTICAL)
    tree8= ttk.Treeview(RightAddNew8, columns=("NO","Penjadwalan","Hari,Tanggal,Bulan & Tahun","Jam","Kode Matkul","Matkul","Semester","Program Studi","Program Pendidikan"), selectmode="extended", height=100, yscrollcommand=scrollbary8.set, xscrollcommand=scrollbarx8.set)
    scrollbary8.config(command=tree8.yview)
    scrollbary8.pack(side=RIGHT, fill=Y)
    scrollbarx8.config(command=tree8.xview)
    scrollbarx8.pack(side=BOTTOM, fill=X)
    tree8.heading('NO', text="NO",anchor=W)#0
    tree8.heading('Penjadwalan', text="Penjadwalan",anchor=W)#1
    tree8.heading('Hari,Tanggal,Bulan & Tahun', text="Hari,Tanggal,Bulan & Tahun",anchor=W)#2
    tree8.heading('Jam', text="Jam",anchor=W)#3
    tree8.heading('Kode Matkul', text="Kode Matkul",anchor=W)#4
    tree8.heading('Matkul', text="Matkul",anchor=W)#5
    tree8.heading('Semester', text="Semester",anchor=W)#6 
    tree8.heading('Program Studi', text="Program Studi",anchor=W)#7
    tree8.heading('Program Pendidikan', text="Program Pendidikan",anchor=W)#8 
    tree8.column('#0', stretch=NO, minwidth=0, width=0)
    tree8.column('#1', stretch=NO, minwidth=0, width=120)
    tree8.column('#2', stretch=NO, minwidth=0, width=120)
    tree8.column('#3', stretch=NO, minwidth=0, width=189)
    tree8.column('#4', stretch=NO, minwidth=0, width=120)
    tree8.column('#5', stretch=NO, minwidth=0, width=120)
    tree8.column('#6', stretch=NO, minwidth=0, width=189)
    tree8.column('#7', stretch=NO, minwidth=0, width=120)
    tree8.column('#8', stretch=NO, minwidth=0, width=120)
    tree8.pack()
    DisplayData11() 
	
def AddNew8():
    Database8()
    cursor.execute("INSERT INTO `Tabel_Penjadwalan` (NO8,Penjadwalan8,HARI_TANGGAL_TAHUN8,JAM8,KODEMATKUL8,MATKUL8,SEMESTER8,PRODI8,PROPE8) VALUES(?,?,?,?,?,?,?,?,?)", (int(NO8.get()),str(Penjadwalan8.get()), str(HARI_TANGGAL_TAHUN8.get()), str(JAM8.get()), str(KODEMATKUL8.get()), str(MATKUL8.get()),str(SEMESTER8.get()),str(PRODI8.get()),str(PROPE8.get())))
    conn.commit()
    NO8.set("")#0
    Penjadwalan8.set("")#1
    HARI_TANGGAL_TAHUN8.set("")#2
    JAM8.set("")#3
    KODEMATKUL8.set("")#4
    MATKUL8.set("")#5
    SEMESTER8.set("")#6
    PRODI8.set("")#7
    PROPE8.set("")#8
    cursor.close()
    conn.close()

def DisplayData11():
    Database8()
    cursor.execute("SELECT * FROM `Tabel_Penjadwalan`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree8.insert('', 'end', values=(data))
    cursor.close()
    conn.close()	
	 
def Search8():
    tree8.delete(*tree8.get_children())
    Database8()
    if(temp8.get()=="Penjadwalan"):
      cursor.execute("SELECT * FROM 'Tabel_Penjadwalan' WHERE Penjadwalan8 LIKE '%s' ORDER BY '' ASC" %SEARCH8.get())
    elif(temp8.get()=="Program Studi"):
      cursor.execute("SELECT * FROM 'Tabel_Penjadwalan' WHERE PRODI8 LIKE '%s' ORDER BY '' ASC" %SEARCH8.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_Penjadwalan' WHERE PROPE8 LIKE '%s' ORDER BY '' ASC" %SEARCH8.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree8.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Delete8():
    if not tree8.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Data Penjadwalan', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
        if result == 'yes':
            curItem = tree8.focus()
            contents =(tree8.item(curItem))
            selecteditem = contents['values']
            tree8.delete(curItem)
            Database8()
            cursor.execute("DELETE FROM `Tabel_Penjadwalan` WHERE `NO8` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def Reset8():
    tree8.delete(*tree8.get_children())
    DisplayData11()
    SEARCH8.set("")

#Tabel_Keuangan(Database7)
def ShowAddNew7():
    global addnewform7
    addnewform7 = Toplevel()
    addnewform7.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform7.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform7.resizable(0, 0)
    AddNewForm7()

#Membuat ikon
    addnewform7_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform7.tk.call('wm','iconphoto',addnewform7._w,addnewform7_icon)
def AddNewForm7():
#===============================Frame 07====================================================
    TopAddNew7 = Frame(addnewform7, width=300, height=400, bd=1, relief=SOLID)
    TopAddNew7.pack(side=TOP, pady=2)
    LeftAddNew7 = Frame(addnewform7, width=300, height=500, bd=8, relief="raise")
    LeftAddNew7.pack(side=LEFT)
    RightAddNew7 = Frame(addnewform7, width=300, height=600, bd=8, relief="raise")
    RightAddNew7.pack(side=RIGHT)
    Forms7 = Frame(LeftAddNew7, width=300, height=450)
    Forms7.pack(side=TOP)
    Buttons7 = Frame(LeftAddNew7,width=300, height=100, bd=8, relief="raise")
    Buttons7.pack(side=BOTTOM)
    searchframe7=Frame(RightAddNew7,bd=8,width=392,height=150,relief="raise")
    searchframe7.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
    lbl_text7 = Label(TopAddNew7, text="Data Keuangan", font=('arial', 12), width=900)
    lbl_text7.pack(fill=X)
    lbl_text7.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_NO7 = Label(Forms7, text="Nomor ", font=('arial', 12), bd=2)
    lbl_NO7.grid(row=0,column=0, sticky=W)
    lbl_NO7.config(foreground ="#00FFFF")
    NO_7 = Entry(Forms7, textvariable=NO7, font=('arial', 12), width=32,bd=2)
    NO_7.grid(row=0, column=1, sticky=W)
    lbl_NPM7 = Label(Forms7, text="NPM ", font=('arial', 12), bd=2)
    lbl_NPM7.grid(row=1,column=0, sticky=W)
    lbl_NPM7.config(foreground ="#00FFFF")
    NPM_7 = Entry(Forms7, textvariable=NPM7, font=('arial', 12), width=32,bd=2)
    NPM_7.grid(row=1, column=1, sticky=W)
    lbl_NAMA7 = Label(Forms7, text="Nama ", font=('arial', 12), bd=2)
    lbl_NAMA7.grid(row=2,column=0, sticky=W)
    lbl_NAMA7.config(foreground ="#00FFFF")
    NAMA_7= Entry(Forms7, textvariable=NAMA7, font=('arial', 12), width=32,bd=2)
    NAMA_7.grid(row=2, column=1, sticky=W)	
    lbl_WAKTU7= Label(Forms7, text="Waktu", font=('arial', 12), bd=2)
    lbl_WAKTU7.grid(row=3,column=0, sticky=W)
    lbl_WAKTU7.config(foreground ="#00FFFF")
    WAKTU_7= Entry(Forms7, textvariable=WAKTU7, font=('arial', 12), width=32,bd=2)
    WAKTU_7.grid(row=3, column=1, sticky=W)
    lbl_URAIAN7= Label(Forms7, text="Uraian", font=('arial', 12), bd=2)
    lbl_URAIAN7.grid(row=4,column=0, sticky=W)
    lbl_URAIAN7.config(foreground ="#00FFFF")
    URAIAN_7=ttk.Combobox(Forms7,font=('arial', 12),state ="readonly", textvariable=URAIAN7, width=30)
    URAIAN_7['values']= ("","Uang Pangkal","Anggsuran Semester 1","Anggsuran Semester 2","Anggsuran Semester 3","Anggsuran Semester 4","Anggsuran Semester 5","Anggsuran Semester 6","Anggsuran Semester 7","Anggsuran Semester 8","Pembayaran Semester 1","Pembayaran Semester 2","Pembayaran Semester 3","Pembayaran Semester 4","Pembayaran Semester 5","Pembayaran Semester 6","Pembayaran Semester 7","Pembayaran Semester 8","Penulasan Semester 1","Penulasan Semester 2","Penulasan Semester 3","Penulasan Semester 4","Penulasan Semester 5","Penulasan Semester 6","Penulasan Semester 7","Penulasan Semester 8")
    URAIAN_7.current(0) 
    URAIAN_7.grid(column=1, row=4,sticky="W")
    lbl_JUMLAHDIBAYAR7= Label(Forms7, text="Jumlah Dibayar", font=('arial', 12), bd=2)
    lbl_JUMLAHDIBAYAR7.grid(row=5,column=0, sticky=W)
    lbl_JUMLAHDIBAYAR7.config(foreground ="#00FFFF")
    JUMLAHDIBAYAR_7= Entry(Forms7, textvariable=JUMLAHDIBAYAR7, font=('arial', 12), width=32,bd=2)
    JUMLAHDIBAYAR_7.grid(row=5, column=1, sticky=W)
    lbl_SISA7= Label(Forms7, text="Sisa", font=('arial', 12), bd=2)
    lbl_SISA7.grid(row=6,column=0, sticky=W)
    lbl_SISA7.config(foreground ="#00FFFF")
    SISA_7= Entry(Forms7, textvariable=SISA7, font=('arial', 12), width=32,bd=2)
    SISA_7.grid(row=6, column=1, sticky=W)
#============================================================================================================
    btn_add7 = Button(Buttons7, text="Save",bg="#009ACD",foreground ="white", command=AddNew7,font=('arial', 12), width=30)
    btn_add7.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search7 = Button(Buttons7, text="Pencarian", command=Search7,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_search7.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset7 = Button(Buttons7, text="Ulang", command=Reset7,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_reset7.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete7 = Button(Buttons7, text="Hapus",command=Delete7,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_delete7.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================
    global tree7
    lbl_txtsearch7 = Label(RightAddNew7, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
    lbl_txtsearch7.pack(side=TOP, anchor=W)
    temp7.set("NO")
    searchoptions7=OptionMenu(searchframe7,temp7,"NO","NPM")
    searchoptions7.pack(side=LEFT)
    search7 = Entry(RightAddNew7, textvariable=SEARCH7, font=('arial', 15), width=10)
    search7.pack(side=TOP,  padx=10, fill=X)
    scrollbarx7 = Scrollbar(RightAddNew7, orient=HORIZONTAL)
    scrollbary7 = Scrollbar(RightAddNew7, orient=VERTICAL)
    tree7= ttk.Treeview(RightAddNew7, columns=("NO","NPM","Nama","Waktu","Uraian","Jumlah Dibayar","Sisa"), selectmode="extended", height=100, yscrollcommand=scrollbary7.set, xscrollcommand=scrollbarx7.set)
    scrollbary7.config(command=tree7.yview)
    scrollbary7.pack(side=RIGHT, fill=Y)
    scrollbarx7.config(command=tree7.xview)
    scrollbarx7.pack(side=BOTTOM, fill=X)
    tree7.heading('NO', text="NO",anchor=W)#0
    tree7.heading('NPM', text="NPM",anchor=W)#1
    tree7.heading('Nama', text="Nama",anchor=W)#2
    tree7.heading('Waktu', text="Waktu",anchor=W)#3
    tree7.heading('Uraian', text="Uraian",anchor=W)#4
    tree7.heading('Jumlah Dibayar', text="Jumlah Dibayar",anchor=W)#5
    tree7.heading('Sisa', text="Sisa",anchor=W)#6
    tree7.column('#0', stretch=NO, minwidth=0, width=0)
    tree7.column('#1', stretch=NO, minwidth=0, width=120)
    tree7.column('#2', stretch=NO, minwidth=0, width=120)
    tree7.column('#3', stretch=NO, minwidth=0, width=189)
    tree7.column('#4', stretch=NO, minwidth=0, width=120)
    tree7.column('#5', stretch=NO, minwidth=0, width=120)
    tree7.column('#6', stretch=NO, minwidth=0, width=189)
    tree7.pack()
    DisplayData10()
	
def AddNew7():
    Database7()
    cursor.execute("INSERT INTO `Tabel_Keuangan` ( NO7,NPM7,NAMA7,WAKTU7,URAIAN7,JUMLAHDIBAYAR7,SISA7) VALUES(?,?,?,?,?,?,?)", (int(NO7.get()),str(NPM7.get()), str(NAMA7.get()), str(WAKTU7.get()), str(URAIAN7.get()), str(JUMLAHDIBAYAR7.get()),str(SISA7.get())))
    conn.commit()
    NO7.set("")#0
    NPM7.set("")#1
    NAMA7.set("")#2
    WAKTU7.set("")#3
    URAIAN7.set("")#4
    JUMLAHDIBAYAR7.set("")#5
    SISA7.set("")#6
    cursor.close()
    conn.close()
	
def DisplayData10():
    Database7()
    cursor.execute("SELECT * FROM `Tabel_Keuangan`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree7.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search7():
    tree7.delete(*tree7.get_children())
    Database7()
    if(temp7.get()=="NO"):
      cursor.execute("SELECT * FROM 'Tabel_Keuangan' WHERE NO7 LIKE '%s' ORDER BY '' ASC" %SEARCH7.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_Keuangan' WHERE NPM7 LIKE '%s' ORDER BY '' ASC" %SEARCH7.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree7.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Delete7():
    if not tree7.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Data Keuangan', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
        if result == 'yes':
            curItem = tree7.focus()
            contents =(tree7.item(curItem))
            selecteditem = contents['values']
            tree7.delete(curItem)
            Database7()
            cursor.execute("DELETE FROM `Tabel_Keuangan` WHERE `NO7` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def Reset7():
    tree7.delete(*tree7.get_children())
    DisplayData10()
    SEARCH7.set("")

#Tabel_RiwayatStudi(Databas6)
def ShowAddNew6():
    global addnewform6
    addnewform6 = Toplevel()
    addnewform6.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform6.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform6.resizable(0, 0)
    AddNewForm6()

#Membuat ikon
    addnewform6_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform6.tk.call('wm','iconphoto',addnewform6._w,addnewform6_icon)
def AddNewForm6():
#===============================Frame 06====================================================
    TopAddNew6 = Frame(addnewform6, width=300, height=400, bd=1, relief=SOLID)
    TopAddNew6.pack(side=TOP, pady=2)
    LeftAddNew6 = Frame(addnewform6, width=300, height=500, bd=8, relief="raise")
    LeftAddNew6.pack(side=LEFT)
    RightAddNew6 = Frame(addnewform6, width=300, height=600, bd=8, relief="raise")
    RightAddNew6.pack(side=RIGHT)
    Forms6 = Frame(LeftAddNew6, width=300, height=450)
    Forms6.pack(side=TOP)
    Buttons6 = Frame(LeftAddNew6,width=300, height=100, bd=8, relief="raise")
    Buttons6.pack(side=BOTTOM)
    searchframe6=Frame(RightAddNew6,bd=8,width=392,height=150,relief="raise")
    searchframe6.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
    lbl_text6 = Label(TopAddNew6, text="Data Riwayat Studi", font=('arial', 12), width=900)
    lbl_text6.pack(fill=X)
    lbl_text6.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_NO6 = Label(Forms6, text="Nomor ", font=('arial', 12), bd=2)
    lbl_NO6.grid(row=0,column=0, sticky=W)
    lbl_NO6.config(foreground ="#00FFFF")
    NO_6 = Entry(Forms6, textvariable=NO6, font=('arial', 12), width=32,bd=2)
    NO_6.grid(row=0, column=1, sticky=W)
    lbl_NPM6 = Label(Forms6, text="NPM ", font=('arial', 12), bd=2)
    lbl_NPM6.grid(row=1,column=0, sticky=W)
    lbl_NPM6.config(foreground ="#00FFFF")
    NPM_6 = Entry(Forms6, textvariable=NPM6, font=('arial', 12), width=32,bd=2)
    NPM_6.grid(row=1, column=1, sticky=W)
    lbl_NAMA6 = Label(Forms6, text="Nama ", font=('arial', 12), bd=2)
    lbl_NAMA6.grid(row=2,column=0, sticky=W)
    lbl_NAMA6.config(foreground ="#00FFFF")
    NAMA_6= Entry(Forms6, textvariable=NAMA6, font=('arial', 12), width=32,bd=2)
    NAMA_6.grid(row=2, column=1, sticky=W)	
    lbl_SEMESTER6= Label(Forms6, text="Semester", font=('arial', 12), bd=2)
    lbl_SEMESTER6.grid(row=3,column=0, sticky=W)
    lbl_SEMESTER6.config(foreground ="#00FFFF")
    SEMESTER_6= Entry(Forms6, textvariable=SEMESTER6, font=('arial', 12), width=32,bd=2)
    SEMESTER_6.grid(row=3, column=1, sticky=W)
    lbl_KODEMATKUL6= Label(Forms6, text="Kode Matkul", font=('arial', 12), bd=2)
    lbl_KODEMATKUL6.grid(row=4,column=0, sticky=W)
    lbl_KODEMATKUL6.config(foreground ="#00FFFF")	
    KODEMATKUL_6= Entry(Forms6, textvariable=KODEMATKUL6, font=('arial', 12), width=32,bd=2)
    KODEMATKUL_6.grid(row=4, column=1, sticky=W)
    lbl_MATKUL6= Label(Forms6, text="Matkul", font=('arial', 12), bd=2)
    lbl_MATKUL6.grid(row=5,column=0, sticky=W)
    lbl_MATKUL6.config(foreground ="#00FFFF")
    MATKUL_6= Entry(Forms6, textvariable=MATKUL6, font=('arial', 12), width=32,bd=2)
    MATKUL_6.grid(row=5, column=1, sticky=W)
    lbl_SKS6= Label(Forms6, text="SKS", font=('arial', 12), bd=2)
    lbl_SKS6.grid(row=6,column=0, sticky=W)
    lbl_SKS6.config(foreground ="#00FFFF")	
    SKS_6 = Spinbox(Forms6, from_=1, to=6, width=33,state ="readonly",textvariable=SKS6,bd=2)
    SKS_6.grid(row=6, column=1,sticky=W)
#=================================================================================================
    btn_add6 = Button(Buttons6, text="Save",bg="#009ACD",foreground ="white", command=AddNew6,font=('arial', 12), width=30)
    btn_add6.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search6 = Button(Buttons6, text="Pencarian", command=Search6,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_search6.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset6 = Button(Buttons6, text="Ulang", command=Reset6,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_reset6.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete6 = Button(Buttons6, text="Hapus",command=Delete6,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_delete6.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================		
    global tree6
    lbl_txtsearch6 = Label(RightAddNew6, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
    lbl_txtsearch6.pack(side=TOP, anchor=W)
    temp6.set("NO")
    searchoptions6=OptionMenu(searchframe6,temp6,"NO","NPM")
    searchoptions6.pack(side=LEFT)
    search6 = Entry(RightAddNew6, textvariable=SEARCH6, font=('arial', 15), width=10)
    search6.pack(side=TOP,  padx=10, fill=X)
    scrollbarx6 = Scrollbar(RightAddNew6, orient=HORIZONTAL)
    scrollbary6 = Scrollbar(RightAddNew6, orient=VERTICAL)
    tree6= ttk.Treeview(RightAddNew6, columns=("NO","NPM","Nama","Semester","Kode Matkul","Matkul","SKS"), selectmode="extended", height=100, yscrollcommand=scrollbary6.set, xscrollcommand=scrollbarx6.set)
    scrollbary6.config(command=tree6.yview)
    scrollbary6.pack(side=RIGHT, fill=Y)
    scrollbarx6.config(command=tree6.xview)
    scrollbarx6.pack(side=BOTTOM, fill=X)
    tree6.heading('NO', text="NO",anchor=W)#0
    tree6.heading('NPM', text="NPM",anchor=W)#1
    tree6.heading('Nama', text="Nama",anchor=W)#2
    tree6.heading('Semester', text="Semester",anchor=W)#3
    tree6.heading('Kode Matkul', text="Kode Matkul",anchor=W)#4
    tree6.heading('Matkul', text="Matkul",anchor=W)#5
    tree6.heading('SKS', text="SKS",anchor=W)#6
    tree6.column('#0', stretch=NO, minwidth=0, width=0)
    tree6.column('#1', stretch=NO, minwidth=0, width=120)
    tree6.column('#2', stretch=NO, minwidth=0, width=120)
    tree6.column('#3', stretch=NO, minwidth=0, width=189)
    tree6.column('#4', stretch=NO, minwidth=0, width=120)
    tree6.column('#5', stretch=NO, minwidth=0, width=120)
    tree6.column('#6', stretch=NO, minwidth=0, width=189)
    tree6.pack()
    DisplayData9()


def AddNew6():
    Database6()
    cursor.execute("INSERT INTO `Tabel_RiwayatStudi` (NO6,NPM6,NAMA6,SEMESTER6,KODEMATKUL6,MATKUL6,SKS6) VALUES(?,?,?,?,?,?,?)", (int(NO6.get()),str(NPM6.get()), str(NAMA6.get()), str(SEMESTER6.get()), str(KODEMATKUL6.get()), str(MATKUL6.get()),str(SKS6.get())))
    conn.commit()
    NO6.set("")#0
    NPM6.set("")#1
    NAMA6.set("")#2
    SEMESTER6.set("")#3
    KODEMATKUL6.set("")#4
    MATKUL6.set("")#5
    SKS6.set("")#6
    cursor.close()
    conn.close()

def DisplayData9():
    Database6()
    cursor.execute("SELECT * FROM `Tabel_RiwayatStudi`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree6.insert('', 'end', values=(data))
    cursor.close()
    conn.close()	

def Search6():
    tree6.delete(*tree6.get_children())
    Database6()
    if(temp6.get()=="NO"):
      cursor.execute("SELECT * FROM 'Tabel_RiwayatStudi' WHERE NO6 LIKE '%s' ORDER BY '' ASC" %SEARCH6.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_RiwayatStudi' WHERE NPM6 LIKE '%s' ORDER BY '' ASC" %SEARCH6.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree6.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
	
def Delete6():
    if not tree6.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Data Riwayat Studi', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
        if result == 'yes':
            curItem = tree6.focus()
            contents =(tree6.item(curItem))
            selecteditem = contents['values']
            tree6.delete(curItem)
            Database6()
            cursor.execute("DELETE FROM `Tabel_RiwayatStudi` WHERE `NO6` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
	
def Reset6():
    tree6.delete(*tree6.get_children())
    DisplayData9()
    SEARCH6.set("")

def ShowView3():
    global viewshow3
    viewshow3 = Toplevel()
    viewshow3.title("SIAKAD")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewshow3.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewshow3.resizable(0, 0)
    ViewShow03()
#Membuat ikon
    viewshow3_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    viewshow3.tk.call('wm','iconphoto',viewshow3._w,viewshow3_icon)

def ViewShow03() :
    global tree4
    TopViewForm6 = Frame(viewshow3, width=600, bd=1, relief=SOLID)
    TopViewForm6.pack(side=TOP, fill=X)
    LeftViewForm6 = Frame(viewshow3, width=800)
    LeftViewForm6.pack(side=LEFT, fill=Y)
    MidViewForm6 = Frame(viewshow3, width=800)
    MidViewForm6.pack(side=RIGHT)
    lbl_text6 = Label(TopViewForm6,font=('arial', 18), width=600)
    lbl_text6.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_text6.pack(fill=X)
    lbl_txtsearch6 = Label(LeftViewForm6, text="Gabungan Tabel Profil Mahasiswa & Riwayat Status Kuliah", font=('arial', 10),foreground ="#FF00FF")
    lbl_txtsearch6.pack(side=TOP, anchor=W)
    scrollbarx6 = Scrollbar(LeftViewForm6, orient=HORIZONTAL)
    scrollbary6 = Scrollbar(LeftViewForm6, orient=VERTICAL)	
    tree4= ttk.Treeview(LeftViewForm6, columns=("No","NPM","Nama","Jenkel","Perguruan Tinggi","Perodi","Semester","Status","Status Awal Mahasiswa","SKS"), selectmode="extended", height=100, yscrollcommand=scrollbary6.set, xscrollcommand=scrollbarx6.set)
    scrollbary6.config(command=tree4.yview)
    scrollbary6.pack(side=RIGHT, fill=Y)
    scrollbarx6.config(command=tree4.xview)
    scrollbarx6.pack(side=BOTTOM, fill=X)
    tree4.heading('No', text="No",anchor=W)#0
    tree4.heading('NPM', text="NPM",anchor=W)#1
    tree4.heading('Nama', text="Nama",anchor=W)#2
    tree4.heading('Jenkel', text="Jenkel",anchor=W)#3
    tree4.heading('Perguruan Tinggi', text="Perguruan Tinggi",anchor=W)#4
    tree4.heading('Perodi', text="Perodi",anchor=W)#5
    tree4.heading('Semester', text="Semester",anchor=W)#6
    tree4.heading('Status', text="Status",anchor=W)#7
    tree4.heading('Status Awal Mahasiswa', text="Status Awal Mahasiswa",anchor=W)#8
    tree4.heading('SKS', text="SKS",anchor=W)#9
    tree4.column('#0', stretch=NO, minwidth=0, width=0)
    tree4.column('#1', stretch=NO, minwidth=0, width=90)
    tree4.column('#2', stretch=NO, minwidth=0, width=90)
    tree4.column('#3', stretch=NO, minwidth=0, width=90)
    tree4.column('#4', stretch=NO, minwidth=0, width=90)
    tree4.column('#5', stretch=NO, minwidth=0, width=90)
    tree4.column('#6', stretch=NO, minwidth=0, width=90)
    tree4.column('#7', stretch=NO, minwidth=0, width=90)
    tree4.column('#8', stretch=NO, minwidth=0, width=90)
    tree4.column('#9', stretch=NO, minwidth=0, width=90)
    tree4.pack()
    DisplayData8()

def DisplayData8():
    Database4()
    cursor.execute("SELECT Tabel_ProfillMAHASISWA.NO4,Tabel_ProfillMAHASISWA.NPM4,Tabel_ProfillMAHASISWA.NAMA4,Tabel_ProfillMAHASISWA.JENKEL4,Tabel_ProfillMAHASISWA.PERGURUAN_TINGGI4,Tabel_ProfillMAHASISWA.PRODI4,Tabel_RiwayatStatusKuliah.SEMESTER5,Tabel_RiwayatStatusKuliah.STATUS5,Tabel_ProfillMAHASISWA.STATUSAWALMAHASIWA4,Tabel_RiwayatStatusKuliah.SKS5 FROM Tabel_ProfillMAHASISWA INNER JOIN Tabel_RiwayatStatusKuliah on Tabel_ProfillMAHASISWA.NO4=Tabel_RiwayatStatusKuliah.NO5")
    fetch = cursor.fetchall()
    for data in fetch:
        tree4.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
	
#Tabel_RiwayatStatusKuliah(Database5)
def ShowAddNew5():
    global addnewform5
    addnewform5 = Toplevel()
    addnewform5.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform5.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform5.resizable(0, 0)
    AddNewForm5()

#Membuat ikon
    addnewform5_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform5.tk.call('wm','iconphoto',addnewform5._w,addnewform5_icon)
def AddNewForm5():
#===============================Frame 05====================================================
    TopAddNew5 = Frame(addnewform5, width=300, height=400, bd=1, relief=SOLID)
    TopAddNew5.pack(side=TOP, pady=2)
    LeftAddNew5 = Frame(addnewform5, width=300, height=500, bd=8, relief="raise")
    LeftAddNew5.pack(side=LEFT)
    RightAddNew5 = Frame(addnewform5, width=300, height=600, bd=8, relief="raise")
    RightAddNew5.pack(side=RIGHT)
    Forms5 = Frame(LeftAddNew5, width=300, height=450)
    Forms5.pack(side=TOP)
    Buttons5 = Frame(LeftAddNew5,width=300, height=100, bd=8, relief="raise")
    Buttons5.pack(side=BOTTOM)
    searchframe5=Frame(RightAddNew5,bd=8,width=392,height=150,relief="raise")
    searchframe5.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
    lbl_text5 = Label(TopAddNew5, text="Data Riwayat Status Kuliah", font=('arial', 12), width=900)
    lbl_text5.pack(fill=X)
    lbl_text5.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_NO5 = Label(Forms5, text="Nomor ", font=('arial', 12), bd=2)
    lbl_NO5.grid(row=0,column=0, sticky=W)
    lbl_NO5.config(foreground ="#00FFFF")
    NO_5 = Entry(Forms5, textvariable=NO5, font=('arial', 12), width=32,bd=2)
    NO_5.grid(row=0, column=1, sticky=W)
    lbl_SEMESTER5 = Label(Forms5, text="Semester", font=('arial', 12), bd=2)
    lbl_SEMESTER5.grid(row=1,column=0, sticky=W)
    lbl_SEMESTER5.config(foreground ="#00FFFF")
    SEMESTER_5 = Entry(Forms5, textvariable=SEMESTER5, font=('arial', 12), width=32,bd=2)
    SEMESTER_5.grid(row=1, column=1, sticky=W)
    lbl_STATUS5 = Label(Forms5, text="Status", font=('arial', 12), bd=2)
    lbl_STATUS5.grid(row=2,column=0, sticky=W)
    lbl_STATUS5.config(foreground ="#00FFFF")
    STATUS_5=ttk.Combobox(Forms5,font=('arial', 12),state ="readonly", textvariable=STATUS5, width=30)
    STATUS_5['values']= ("","Aktif","Tidak Aktif","Cuti","Mengundurkan Diri")
    STATUS_5.current(0) 
    STATUS_5.grid(column=1, row=2,sticky="W")
    lbl_SKS5 = Label(Forms5, text="SKS", font=('arial', 12), bd=2)
    lbl_SKS5.grid(row=3,column=0, sticky=W)
    lbl_SKS5.config(foreground ="#00FFFF")
    SKS_5 = Spinbox(Forms5, from_=1, to=60, width=33,state ="readonly",textvariable=SKS5,bd=2)
    SKS_5.grid(row=3, column=1,sticky=W)
#==========================================================================================================
    btn_add5 = Button(Buttons5, text="Save",bg="#009ACD",foreground ="white", command=AddNew5,font=('arial', 12), width=30)
    btn_add5.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search5 = Button(Buttons5, text="Pencarian", command=Search5,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_search5.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset5 = Button(Buttons5, text="Ulang", command=Reset5,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_reset5.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete5 = Button(Buttons5, text="Hapus",command=Delete5,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_delete5.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================	
    global tree5
    lbl_txtsearch5 = Label(RightAddNew5, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
    lbl_txtsearch5.pack(side=TOP, anchor=W)
    temp5.set("NO")
    searchoptions5=OptionMenu(searchframe5,temp5,"NO","Status")
    searchoptions5.pack(side=LEFT)
    search5 = Entry(RightAddNew5, textvariable=SEARCH5, font=('arial', 15), width=10)
    search5.pack(side=TOP,  padx=10, fill=X)
    scrollbarx5 = Scrollbar(RightAddNew5, orient=HORIZONTAL)
    scrollbary5 = Scrollbar(RightAddNew5, orient=VERTICAL)
    tree5= ttk.Treeview(RightAddNew5, columns=("NO","Semester","Status","SKS"), selectmode="extended", height=100, yscrollcommand=scrollbary5.set, xscrollcommand=scrollbarx5.set)
    scrollbary5.config(command=tree5.yview)
    scrollbary5.pack(side=RIGHT, fill=Y)
    scrollbarx5.config(command=tree5.xview)
    scrollbarx5.pack(side=BOTTOM, fill=X)
    tree5.heading('NO', text="NO",anchor=W)#0
    tree5.heading('Semester', text="Semester",anchor=W)#1
    tree5.heading('Status', text="Status",anchor=W)#2
    tree5.heading('SKS', text="SKS",anchor=W)#3
    tree5.column('#0', stretch=NO, minwidth=0, width=0)
    tree5.column('#1', stretch=NO, minwidth=0, width=120)
    tree5.column('#2', stretch=NO, minwidth=0, width=120)
    tree5.column('#3', stretch=NO, minwidth=0, width=189)
    tree5.pack()
    DisplayData7()

def AddNew5():
    Database5()
    cursor.execute("INSERT INTO `Tabel_RiwayatStatusKuliah` (NO5,SEMESTER5,STATUS5,SKS5) VALUES(?,?,?,?)", (int(NO5.get()),str(SEMESTER5.get()), str(STATUS5.get()),str(SKS5.get())))
    conn.commit()
    NO5.set("")#0
    SEMESTER5.set("")#1
    STATUS5.set("")#2
    SKS5.set("")#3
    cursor.close()
    conn.close()
	
def DisplayData7():
    Database5()
    cursor.execute("SELECT * FROM `Tabel_RiwayatStatusKuliah`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree5.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search5():
    tree5.delete(*tree5.get_children())
    Database4()
    if(temp4.get()=="NO"):
      cursor.execute("SELECT * FROM 'Tabel_RiwayatStatusKuliah' WHERE NO5 LIKE '%s' ORDER BY '' ASC" %SEARCH5.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_RiwayatStatusKuliah' WHERE STATUS5 LIKE '%s' ORDER BY '' ASC" %SEARCH5.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree5.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Delete5():
    if not tree5.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Data Riwayat Status Kuliah', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
        if result == 'yes':
            curItem = tree5.focus()
            contents =(tree5.item(curItem))
            selecteditem = contents['values']
            tree5.delete(curItem)
            Database5()
            cursor.execute("DELETE FROM `Tabel_RiwayatStatusKuliah` WHERE `NO5` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def Reset5():
    tree5.delete(*tree5.get_children())
    DisplayData7()
    SEARCH5.set("")

#Tabel_ProfillMAHASISWA(Database4)
def ShowAddNew4():
    global addnewform4
    addnewform4 = Toplevel()
    addnewform4.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform4.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform4.resizable(0, 0)
    AddNewForm4()

#Membuat ikon
    addnewform4_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform4.tk.call('wm','iconphoto',addnewform4._w,addnewform4_icon)
def AddNewForm4():
#===============================Frame 04====================================================
    TopAddNew4 = Frame(addnewform4, width=300, height=400, bd=1, relief=SOLID)
    TopAddNew4.pack(side=TOP, pady=2)
    LeftAddNew4 = Frame(addnewform4, width=300, height=500, bd=8, relief="raise")
    LeftAddNew4.pack(side=LEFT)
    RightAddNew4 = Frame(addnewform4, width=300, height=600, bd=8, relief="raise")
    RightAddNew4.pack(side=RIGHT)
    Forms4 = Frame(LeftAddNew4, width=300, height=450)
    Forms4.pack(side=TOP)
    Buttons4 = Frame(LeftAddNew4,width=300, height=100, bd=8, relief="raise")
    Buttons4.pack(side=BOTTOM)
    searchframe4=Frame(RightAddNew4,bd=8,width=392,height=150,relief="raise")
    searchframe4.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
    lbl_text4 = Label(TopAddNew4, text="Data Profil Mahasiswa", font=('arial', 12), width=900)
    lbl_text4.pack(fill=X)
    lbl_text4.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_NO4 = Label(Forms4, text="Nomor ", font=('arial', 12), bd=2)
    lbl_NO4.grid(row=0,column=0, sticky=W)
    lbl_NO4.config(foreground ="#00FFFF")
    NO_4 = Entry(Forms4, textvariable=NO4, font=('arial', 12), width=32,bd=2)
    NO_4.grid(row=0, column=1, sticky=W)
    lbl_NPM4 = Label(Forms4, text="NPM ", font=('arial', 12), bd=2)
    lbl_NPM4.grid(row=1,column=0, sticky=W)
    lbl_NPM4.config(foreground ="#00FFFF")
    NPM_4 = Entry(Forms4, textvariable=NPM4, font=('arial', 12), width=32,bd=2)
    NPM_4.grid(row=1, column=1, sticky=W)
    lbl_NAMA4 = Label(Forms4, text="Nama", font=('arial', 12), bd=2)
    lbl_NAMA4.grid(row=2,column=0, sticky=W)
    lbl_NAMA4.config(foreground ="#00FFFF")
    NAMA_4 = Entry(Forms4, textvariable=NAMA4, font=('arial', 12), width=32,bd=2)
    NAMA_4.grid(row=2, column=1, sticky=W)
    lbl_JENKEL4 = Label(Forms4, text="Jenis Kelamin", font=('arial', 12), bd=2)
    lbl_JENKEL4.grid(row=3,column=0, sticky=W)
    lbl_JENKEL4.config(foreground ="#00FFFF")
    JENKEL04=ttk.Combobox(Forms4,font=('arial', 12),state ="readonly", textvariable=JENKEL4, width=30)
    JENKEL04['values']= ("","P","L")
    JENKEL04.current(0) 
    JENKEL04.grid(column=1, row=3,sticky="W")	
    lbl_PERGURUAN_TINGGI4 = Label(Forms4, text="Perguruan Tinggi", font=('arial', 12), bd=2)
    lbl_PERGURUAN_TINGGI4.grid(row=4,column=0, sticky=W)
    lbl_PERGURUAN_TINGGI4.config(foreground ="#00FFFF")
    PERGURUAN_TINGGI_4 = Entry(Forms4, textvariable=PERGURUAN_TINGGI4, font=('arial', 12), width=32,bd=2)
    PERGURUAN_TINGGI_4.grid(row=4, column=1, sticky=W)
    lbl_PRODI4 = Label(Forms4, text="Program Studi", font=('arial', 12), bd=2)
    lbl_PRODI4.grid(row=5,column=0, sticky=W)
    lbl_PRODI4.config(foreground ="#00FFFF")
    PRODI_4=ttk.Combobox(Forms4,font=('arial', 12),state ="readonly", textvariable=PRODI4, width=30)
    PRODI_4['values']= ("","IT (S1)","SI (S1)","IT (D3)","IT (Profesi 2 Tahun)")
    PRODI_4.current(0) 
    PRODI_4.grid(column=1, row=5,sticky="W")
    lbl_SEMESTERAWAL4 = Label(Forms4, text="Semester Awal", font=('arial', 12), bd=2)
    lbl_SEMESTERAWAL4.grid(row=6,column=0, sticky=W)
    lbl_SEMESTERAWAL4.config(foreground ="#00FFFF")
    SEMESTERAWAL_4 = Entry(Forms4, textvariable=SEMESTERAWAL4, font=('arial', 12), width=32,bd=2)
    SEMESTERAWAL_4.grid(row=6, column=1, sticky=W)
    lbl_STATUSAWALMAHASIWA4 = Label(Forms4, text="Semester Awal Mahasiswa", font=('arial', 12), bd=2)
    lbl_STATUSAWALMAHASIWA4.grid(row=7,column=0, sticky=W)
    lbl_STATUSAWALMAHASIWA4.config(foreground ="#00FFFF")
    STATUSAWALMAHASIWA_4=ttk.Combobox(Forms4,font=('arial', 12),state ="readonly", textvariable=STATUSAWALMAHASIWA4, width=30)
    STATUSAWALMAHASIWA_4['values']= ("","Alih Jenjang","Peserta didik Baru")
    STATUSAWALMAHASIWA_4.current(0) 
    STATUSAWALMAHASIWA_4.grid(column=1, row=7,sticky="W")    	
    lbl_STATUSMAHASISWAINI4 = Label(Forms4, text="Status Mahasiswa Saat ini", font=('arial', 12), bd=2)
    lbl_STATUSMAHASISWAINI4.grid(row=8,column=0, sticky=W)
    lbl_STATUSMAHASISWAINI4.config(foreground ="#00FFFF")
    STATUSMAHASISWAINI_4=ttk.Combobox(Forms4,font=('arial', 12),state ="readonly", textvariable=STATUSMAHASISWAINI4, width=30)
    STATUSMAHASISWAINI_4['values']= ("","Aktif","Tidak Aktif","Mengundurkan Diri","Lulus","Cuti","Tidak Lulus")
    STATUSMAHASISWAINI_4.current(0) 
    STATUSMAHASISWAINI_4.grid(column=1, row=8,sticky="W")
    lbl_TANGGALLULUS4 = Label(Forms4, text="Tanggal Lulus", font=('arial', 12), bd=2)
    lbl_TANGGALLULUS4.grid(row=9,column=0, sticky=W)
    lbl_TANGGALLULUS4.config(foreground ="#00FFFF")
    TANGGALLULUS_4 = Entry(Forms4, textvariable=TANGGALLULUS4, font=('arial', 12), width=32,bd=2)
    TANGGALLULUS_4.grid(row=9, column=1, sticky=W)
    lbl_NOMORIJAZAH4 = Label(Forms4, text="Nomor Ijazah", font=('arial', 12), bd=2)
    lbl_NOMORIJAZAH4.grid(row=10,column=0, sticky=W)
    lbl_NOMORIJAZAH4.config(foreground ="#00FFFF")
    NOMORIJAZAH_4 = Entry(Forms4, textvariable=NOMORIJAZAH4, font=('arial', 12), width=32,bd=2)
    NOMORIJAZAH_4.grid(row=10, column=1, sticky=W)
#==========================================================================================================
    btn_add4 = Button(Buttons4, text="Save",bg="#009ACD",foreground ="white", command=AddNew4,font=('arial', 12), width=30)
    btn_add4.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search4 = Button(Buttons4, text="Pencarian", command=Search4,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_search4.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset4 = Button(Buttons4, text="Ulang", command=Reset4,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_reset4.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete4 = Button(Buttons4, text="Hapus",command=Delete4,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_delete4.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================	
    global tree4
    lbl_txtsearch4 = Label(RightAddNew4, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
    lbl_txtsearch4.pack(side=TOP, anchor=W)
    temp4.set("NPM")
    searchoptions4=OptionMenu(searchframe4,temp4,"NPM","Program Studi","Status Mahasiswa Saat ini")
    searchoptions4.pack(side=LEFT)
    search4 = Entry(RightAddNew4, textvariable=SEARCH4, font=('arial', 15), width=10)
    search4.pack(side=TOP,  padx=10, fill=X)
    scrollbarx4 = Scrollbar(RightAddNew4, orient=HORIZONTAL)
    scrollbary4 = Scrollbar(RightAddNew4, orient=VERTICAL)
    tree4= ttk.Treeview(RightAddNew4, columns=("NO","NPM", "Nama", "Jenkel", "Perguruan Tinggi","Program Studi", "Semester Awal", "Semester Awal Mahasiswa","Status Mahasiswa Saat ini","Tanggal Lulus","Nomor Ijazah"), selectmode="extended", height=100, yscrollcommand=scrollbary4.set, xscrollcommand=scrollbarx4.set)
    scrollbary4.config(command=tree4.yview)
    scrollbary4.pack(side=RIGHT, fill=Y)
    scrollbarx4.config(command=tree4.xview)
    scrollbarx4.pack(side=BOTTOM, fill=X)
    tree4.heading('NO', text="NO",anchor=W)#0
    tree4.heading('NPM', text="NPM",anchor=W)#1
    tree4.heading('Nama', text="Nama",anchor=W)#2
    tree4.heading('Jenkel', text="Jenkel",anchor=W)#3
    tree4.heading('Perguruan Tinggi', text="Perguruan Tinggi",anchor=W)#4
    tree4.heading('Program Studi', text="Program Studi",anchor=W)#5
    tree4.heading('Semester Awal', text="Semester Awal",anchor=W)#6
    tree4.heading('Semester Awal Mahasiswa', text="Semester Awal Mahasiswa",anchor=W)#7    
    tree4.heading('Status Mahasiswa Saat ini', text="Status Mahasiswa Saat ini",anchor=W)#8
    tree4.heading('Tanggal Lulus', text="Tanggal Lulus",anchor=W)#9
    tree4.heading('Nomor Ijazah', text="Nomor Ijazah",anchor=W)#10
    tree4.column('#0', stretch=NO, minwidth=0, width=0)
    tree4.column('#1', stretch=NO, minwidth=0, width=120)
    tree4.column('#2', stretch=NO, minwidth=0, width=120)
    tree4.column('#3', stretch=NO, minwidth=0, width=189)
    tree4.column('#4', stretch=NO, minwidth=0, width=189)
    tree4.column('#5', stretch=NO, minwidth=0, width=189)
    tree4.column('#6', stretch=NO, minwidth=0, width=189)
    tree4.column('#7', stretch=NO, minwidth=0, width=189)
    tree4.column('#8', stretch=NO, minwidth=0, width=189)
    tree4.column('#9', stretch=NO, minwidth=0, width=189)
    tree4.column('#10', stretch=NO, minwidth=0, width=189)
    tree4.pack()
    DisplayData6()
	
def AddNew4():
    Database4()
    cursor.execute("INSERT INTO `Tabel_ProfillMAHASISWA` (NO4,NPM4,NAMA4,JENKEL4,PERGURUAN_TINGGI4,PRODI4,SEMESTERAWAL4,STATUSAWALMAHASIWA4,STATUSMAHASISWAINI4,TANGGALLULUS4,NOMORIJAZAH4) VALUES(?,?,?,?,?,?,?,?,?,?,?)", (int(NO4.get()),str(NPM4.get()), str(NAMA4.get()), str(JENKEL4.get()),str(PERGURUAN_TINGGI4.get()),str(PRODI4.get()),str(SEMESTERAWAL4.get()),str(STATUSAWALMAHASIWA4.get()),str(STATUSMAHASISWAINI4.get()),str(TANGGALLULUS4.get()),str(NOMORIJAZAH4.get())))
    conn.commit()
    NO4.set("")#0
    NPM4.set("")#1
    NAMA4.set("")#2
    JENKEL4.set("")#3
    PERGURUAN_TINGGI4.set("")#4
    PRODI4.set("")#5
    SEMESTERAWAL4.set("")#6
    STATUSAWALMAHASIWA4.set("")#7
    STATUSMAHASISWAINI4.set("")#8
    TANGGALLULUS4.set("")#9
    NOMORIJAZAH4.set("")#10
    cursor.close()
    conn.close()

def DisplayData6():
    Database4()
    cursor.execute("SELECT * FROM `Tabel_ProfillMAHASISWA`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree4.insert('', 'end', values=(data))
    cursor.close()
    conn.close()	

def Search4():
    tree4.delete(*tree4.get_children())
    Database4()
    if(temp4.get()=="PM"):
      cursor.execute("SELECT * FROM 'Tabel_ProfillMAHASISWA' WHERE NPM4 LIKE '%s' ORDER BY '' ASC" %SEARCH4.get())
    elif(temp4.get()=="Program Studi"):
      cursor.execute("SELECT * FROM 'Tabel_ProfillMAHASISWA' WHERE PRODI4 LIKE '%s' ORDER BY '' ASC" %SEARCH4.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_ProfillMAHASISWA' WHERE STATUSMAHASISWAINI4 LIKE '%s' ORDER BY '' ASC" %SEARCH4.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree4.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
	
def Delete4():
    if not tree4.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Data Profil Mahasiswa', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
        if result == 'yes':
            curItem = tree4.focus()
            contents =(tree4.item(curItem))
            selecteditem = contents['values']
            tree4.delete(curItem)
            Database4()
            cursor.execute("DELETE FROM `Tabel_ProfillMAHASISWA` WHERE `NO4` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()	
			
def Reset4():
    tree4.delete(*tree4.get_children())
    DisplayData6()
    SEARCH4.set("")

def ShowView2():
    global viewshow2
    viewshow2 = Toplevel()
    viewshow2.title("SIAKAD")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewshow2.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewshow2.resizable(0, 0)
    ViewShow02()
#Membuat ikon
    viewshow2_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    viewshow2.tk.call('wm','iconphoto',viewshow2._w,viewshow2_icon)

def ViewShow02() :
    global tree3
    TopViewForm4 = Frame(viewshow2, width=600, bd=1, relief=SOLID)
    TopViewForm4.pack(side=TOP, fill=X)
    LeftViewForm4 = Frame(viewshow2, width=800)
    LeftViewForm4.pack(side=LEFT, fill=Y)
    MidViewForm4 = Frame(viewshow2, width=800)
    MidViewForm4.pack(side=RIGHT)
    lbl_text4 = Label(TopViewForm4,font=('arial', 18), width=600)
    lbl_text4.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_text4.pack(fill=X)
    lbl_txtsearch4 = Label(LeftViewForm4, text="Gabungan Tabel Registrasi & KTP", font=('arial', 10),foreground ="#FF00FF")
    lbl_txtsearch4.pack(side=TOP, anchor=W)		
    scrollbarx4 = Scrollbar(LeftViewForm4, orient=HORIZONTAL)
    scrollbary4 = Scrollbar(LeftViewForm4, orient=VERTICAL)
    tree3= ttk.Treeview(LeftViewForm4, columns=("No","Nik","Nama","Jenkel","Golongan Darah","Alamat","Rt / Rw","Desa","Kecamatan","Agama","Status Perkawinan","Kewarganegaraan","Berlaku Hingga"), selectmode="extended", height=100, yscrollcommand=scrollbary4.set, xscrollcommand=scrollbarx4.set)
    scrollbary4.config(command=tree3.yview)
    scrollbary4.pack(side=RIGHT, fill=Y)
    scrollbarx4.config(command=tree3.xview)
    scrollbarx4.pack(side=BOTTOM, fill=X)
    tree3.heading('No', text="No",anchor=W)#0
    tree3.heading('Nik', text="Nik",anchor=W)#1
    tree3.heading('Nama', text="Nama",anchor=W)#2
    tree3.heading('Nik', text="Nik",anchor=W)#3
    tree3.heading('Jenkel', text="Jenkel",anchor=W)#4
    tree3.heading('Golongan Darah', text="Golongan Darah",anchor=W)#5
    tree3.heading('Alamat', text="Alamat",anchor=W)#6
    tree3.heading('Rt / Rw', text="Rt / Rw",anchor=W)#7
    tree3.heading('Desa', text="Desa",anchor=W)#8
    tree3.heading('Kecamatan', text="Kecamatan",anchor=W)#9
    tree3.heading('Agama', text="Agama",anchor=W)#10
    tree3.heading('Status Perkawinan', text="Status Perkawinan",anchor=W)#11
    tree3.heading('Kewarganegaraan', text="Kewarganegaraan",anchor=W)#12	
    tree3.heading('Berlaku Hingga', text="Berlaku Hingga",anchor=W)#13	
    tree3.column('#0', stretch=NO, minwidth=0, width=0)
    tree3.column('#1', stretch=NO, minwidth=0, width=90)
    tree3.column('#2', stretch=NO, minwidth=0, width=90)
    tree3.column('#3', stretch=NO, minwidth=0, width=90)
    tree3.column('#4', stretch=NO, minwidth=0, width=90)
    tree3.column('#5', stretch=NO, minwidth=0, width=90)
    tree3.column('#6', stretch=NO, minwidth=0, width=90)
    tree3.column('#7', stretch=NO, minwidth=0, width=90)
    tree3.column('#8', stretch=NO, minwidth=0, width=90)
    tree3.column('#9', stretch=NO, minwidth=0, width=90)
    tree3.column('#10', stretch=NO, minwidth=0, width=90)
    tree3.column('#11', stretch=NO, minwidth=0, width=90)
    tree3.column('#12', stretch=NO, minwidth=0, width=90)	
    tree3.column('#13', stretch=NO, minwidth=0, width=90)
    tree3.pack()
    DisplayData5()
	
def DisplayData5():
    Database3()
    cursor.execute("SELECT Tabel_KTP.NO3, Tabel_KTP.NIK3 ,Tabel_Registrasi.NAMA1,Tabel_Registrasi.JENKEL1,Tabel_KTP.GOLDARAH3,Tabel_Registrasi.ALAMAT1, Tabel_KTP.RTRW3,Tabel_KTP.DESA3,Tabel_KTP.KECAMATAN3,Tabel_Registrasi.AGAMA1,Tabel_KTP.SP3,Tabel_KTP.KEWARGANEGARAAN3,Tabel_KTP.BERLAKUHINGGA3 FROM Tabel_Registrasi INNER JOIN Tabel_KTP ON Tabel_Registrasi.NO1=Tabel_KTP.NO3")
    fetch = cursor.fetchall()
    for data in fetch:
        tree3.insert('', 'end', values=(data))
    cursor.close()
    conn.close()	

#KTP (Database3)
def ShowAddNew3():
    global addnewform3
    addnewform3 = Toplevel()
    addnewform3.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform3.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform3.resizable(0, 0)
    AddNewForm3()

#Membuat ikon
    addnewform3_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform3.tk.call('wm','iconphoto',addnewform3._w,addnewform3_icon)
def AddNewForm3():
#===============================Frame 03====================================================
    TopAddNew3 = Frame(addnewform3, width=300, height=400, bd=1, relief=SOLID)
    TopAddNew3.pack(side=TOP, pady=2)
    LeftAddNew3 = Frame(addnewform3, width=300, height=500, bd=8, relief="raise")
    LeftAddNew3.pack(side=LEFT)
    RightAddNew3 = Frame(addnewform3, width=300, height=600, bd=8, relief="raise")
    RightAddNew3.pack(side=RIGHT)
    Forms3 = Frame(LeftAddNew3, width=300, height=450)
    Forms3.pack(side=TOP)
    Buttons3 = Frame(LeftAddNew3,width=300, height=100, bd=8, relief="raise")
    Buttons3.pack(side=BOTTOM)
    searchframe3=Frame(RightAddNew3,bd=8,width=392,height=150,relief="raise")
    searchframe3.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
    lbl_text3 = Label(TopAddNew3, text="Data KTP", font=('arial', 12), width=900)
    lbl_text3.pack(fill=X)
    lbl_text3.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_NO3 = Label(Forms3, text="Nomor ", font=('arial', 12), bd=2)
    lbl_NO3.grid(row=0,column=0, sticky=W)
    lbl_NO3.config(foreground ="#00FFFF")
    NO_3 = Entry(Forms3, textvariable=NO3, font=('arial', 12), width=32,bd=2)
    NO_3.grid(row=0, column=1, sticky=W)
    lbl_NIK3 = Label(Forms3, text="NIK ", font=('arial', 12), bd=2)
    lbl_NIK3.grid(row=1,column=0, sticky=W)
    lbl_NIK3.config(foreground ="#00FFFF")
    NIK_3 = Entry(Forms3, textvariable=NIK3, font=('arial', 12), width=32,bd=2)
    NIK_3.grid(row=1, column=1, sticky=W)
    lbl_GOLDARAH3 = Label(Forms3, text="Golongan Darah ", font=('arial', 12), bd=2)
    lbl_GOLDARAH3.grid(row=2,column=0, sticky=W)
    lbl_GOLDARAH3.config(foreground ="#00FFFF")
    GOLDARAH_3 = ttk.Combobox(Forms3,font=('arial', 12),state ="readonly", textvariable=GOLDARAH3, width=30)
    GOLDARAH_3 ['values']= ("","-","A","B","AB","O")
    GOLDARAH_3.current(0) 
    GOLDARAH_3.grid(column=1, row=2,sticky="W")
    lbl_RTRW3 = Label(Forms3, text="RT / RW ", font=('arial', 12), bd=2)
    lbl_RTRW3.grid(row=3,column=0, sticky=W)
    lbl_RTRW3.config(foreground ="#00FFFF")
    RTRW_3 = Entry(Forms3, textvariable=RTRW3, font=('arial', 12), width=32,bd=2)
    RTRW_3.grid(row=3, column=1, sticky=W)
    lbl_DESA3 = Label(Forms3, text="Kel / Desa ", font=('arial', 12), bd=2)
    lbl_DESA3.grid(row=4,column=0, sticky=W)
    lbl_DESA3.config(foreground ="#00FFFF")
    DESA_3 = Entry(Forms3, textvariable=DESA3, font=('arial', 12), width=32,bd=2)
    DESA_3.grid(row=4, column=1, sticky=W)
    lbl_KECAMATAN3 = Label(Forms3, text="Kecamatan ", font=('arial', 12), bd=2)
    lbl_KECAMATAN3.grid(row=5,column=0, sticky=W)
    lbl_KECAMATAN3.config(foreground ="#00FFFF")
    KECAMATAN_3 = Entry(Forms3, textvariable=KECAMATAN3, font=('arial', 12), width=32,bd=2)
    KECAMATAN_3.grid(row=5, column=1, sticky=W)
    lbl_SP3 = Label(Forms3, text="Status Perkawinan ", font=('arial', 12), bd=2)
    lbl_SP3.grid(row=6,column=0, sticky=W)
    lbl_SP3.config(foreground ="#00FFFF")
    SP_3 = ttk.Combobox(Forms3,font=('arial', 12),state ="readonly", textvariable=SP3 , width=30)
    SP_3 ['values']= ("","Sudah Kawin","Belum Kawin","Janda","Duda")
    SP_3.current(0) 
    SP_3.grid(column=1, row=6,sticky="W") 
    lbl_PEKERJAAN3 = Label(Forms3, text="Pekerjaan", font=('arial', 12), bd=2)
    lbl_PEKERJAAN3.grid(row=7,column=0, sticky=W)
    lbl_PEKERJAAN3.config(foreground ="#00FFFF")
    PEKERJAAN_3 = Entry(Forms3, textvariable=PEKERJAAN3, font=('arial', 12), width=32,bd=2)
    PEKERJAAN_3.grid(row=7, column=1, sticky=W)
    lbl_KEWARGANEGARAAN3 = Label(Forms3, text="Kewarganegaraan", font=('arial', 12), bd=2)
    lbl_KEWARGANEGARAAN3.grid(row=8,column=0, sticky=W)
    lbl_KEWARGANEGARAAN3.config(foreground ="#00FFFF")
    KEWARGANEGARAAN_3 = ttk.Combobox(Forms3,font=('arial', 12),state ="readonly", textvariable=KEWARGANEGARAAN3, width=30)
    KEWARGANEGARAAN_3 ['values']= ("","WNA","WNI")
    KEWARGANEGARAAN_3.current(0) 
    KEWARGANEGARAAN_3.grid(column=1, row=8,sticky="W") 
    lbl_BERLAKUHINGGA3 = Label(Forms3, text="Berlaku Hingga", font=('arial', 12), bd=2)
    lbl_BERLAKUHINGGA3.grid(row=9,column=0, sticky=W)
    lbl_BERLAKUHINGGA3.config(foreground ="#00FFFF")
    BERLAKUHINGGA_3 = Entry(Forms3, textvariable=BERLAKUHINGGA3, font=('arial', 12), width=32,bd=2)
    BERLAKUHINGGA_3.grid(row=9, column=1, sticky=W)
#==========================================================================================================
    btn_add3 = Button(Buttons3, text="Save",bg="#009ACD",foreground ="white", command=AddNew3,font=('arial', 12), width=30)
    btn_add3.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search3 = Button(Buttons3, text="Pencarian", command=Search3,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_search3.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset3 = Button(Buttons3, text="Ulang", command=Reset3,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_reset3.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete3 = Button(Buttons3, text="Hapus",command=Delete3,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_delete3.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================	
    global tree3
    lbl_txtsearch3 = Label(RightAddNew3, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
    lbl_txtsearch3.pack(side=TOP, anchor=W)
    temp3.set("No")
    searchoptions3=OptionMenu(searchframe3,temp3,"No","Status Perkawinan","Kewarganegaraan")
    searchoptions3.pack(side=LEFT)
    search3 = Entry(RightAddNew3, textvariable=SEARCH3, font=('arial', 15), width=10)
    search3.pack(side=TOP,  padx=10, fill=X)
    scrollbarx3 = Scrollbar(RightAddNew3, orient=HORIZONTAL)
    scrollbary3 = Scrollbar(RightAddNew3, orient=VERTICAL)
    tree3= ttk.Treeview(RightAddNew3, columns=("NO","Nik", "Golongan Darah", "Rt / RW", "Desa","Kecamatan", "Status Perkawinan", "Pekerjaan","Kewarganegaraan","Berlaku Hingga"), selectmode="extended", height=100, yscrollcommand=scrollbary3.set, xscrollcommand=scrollbarx3.set)
    scrollbary3.config(command=tree3.yview)
    scrollbary3.pack(side=RIGHT, fill=Y)
    scrollbarx3.config(command=tree3.xview)
    scrollbarx3.pack(side=BOTTOM, fill=X)
    tree3.heading('NO', text="NO",anchor=W)#0
    tree3.heading('Nik', text="Nik",anchor=W)#1
    tree3.heading('Golongan Darah', text="Golongan Darah",anchor=W)#2
    tree3.heading('Rt / RW', text="Rt / RW",anchor=W)#3
    tree3.heading('Desa', text="Desa",anchor=W)#4
    tree3.heading('Kecamatan', text="Kecamatan",anchor=W)#5
    tree3.heading('Status Perkawinan', text="Status Perkawinan",anchor=W)#6
    tree3.heading('Pekerjaan', text="Pekerjaan",anchor=W)#7    
    tree3.heading('Kewarganegaraan', text="Kewarganegaraan",anchor=W)#8
    tree3.heading('Berlaku Hingga', text="Berlaku Hingga",anchor=W)#9
    tree3.column('#0', stretch=NO, minwidth=0, width=0)
    tree3.column('#1', stretch=NO, minwidth=0, width=120)
    tree3.column('#2', stretch=NO, minwidth=0, width=120)
    tree3.column('#3', stretch=NO, minwidth=0, width=189)
    tree3.column('#4', stretch=NO, minwidth=0, width=189)
    tree3.column('#5', stretch=NO, minwidth=0, width=189)
    tree3.column('#6', stretch=NO, minwidth=0, width=189)
    tree3.column('#7', stretch=NO, minwidth=0, width=189)
    tree3.column('#8', stretch=NO, minwidth=0, width=189)
    tree3.column('#9', stretch=NO, minwidth=0, width=189)	
    tree3.pack()
    DisplayData4()

def AddNew3():
    Database3()
    cursor.execute("INSERT INTO `Tabel_KTP` (NO3,NIK3,GOLDARAH3,RTRW3,DESA3,KECAMATAN3,SP3,PEKERJAAN3,KEWARGANEGARAAN3,BERLAKUHINGGA3) VALUES(?,?,?,?,?,?,?,?,?,?)", (int(NO3.get()),str(NIK3.get()), str(GOLDARAH3.get()), str(RTRW3.get()),str(DESA3.get()),str(KECAMATAN3.get()),str(SP3.get()),str(PEKERJAAN3.get()),str(KEWARGANEGARAAN3.get()),str(BERLAKUHINGGA3.get())))
    conn.commit()
    NO3.set("")#0
    NIK3.set("")#1
    GOLDARAH3.set("")#2
    RTRW3.set("")#3
    DESA3.set("")#4
    KECAMATAN3.set("")#5
    SP3.set("")#6
    PEKERJAAN3.set("")#7
    KEWARGANEGARAAN3.set("")#8
    BERLAKUHINGGA3.set("")#9
    cursor.close()
    conn.close()

def DisplayData4():
    Database3()
    cursor.execute("SELECT * FROM `Tabel_KTP`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree3.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
	
def Search3():
    tree3.delete(*tree3.get_children())
    Database3()
    if(temp3.get()=="No"):
      cursor.execute("SELECT * FROM 'Tabel_KTP' WHERE NO3 LIKE '%s' ORDER BY '' ASC" %SEARCH3.get())
    elif(temp3.get()=="Status Perkawinan"):
      cursor.execute("SELECT * FROM 'Tabel_KTP' WHERE SP3 LIKE '%s' ORDER BY '' ASC" %SEARCH3.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_KTP' WHERE KEWARGANEGARAAN3 LIKE '%s' ORDER BY '' ASC" %SEARCH3.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree3.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Delete3():
    if not tree3.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Data KTP', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
        if result == 'yes':
            curItem = tree3.focus()
            contents =(tree3.item(curItem))
            selecteditem = contents['values']
            tree3.delete(curItem)
            Database3()
            cursor.execute("DELETE FROM `Tabel_KTP` WHERE `NO3` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def Reset3():
    tree3.delete(*tree3.get_children())
    DisplayData4()
    SEARCH3.set("")

def ShowView1():
    global viewshow1
    viewshow1 = Toplevel()
    viewshow1.title("SIAKAD")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewshow1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewshow1.resizable(0, 0)
    ViewShow01()
#Membuat ikon
    viewshow1_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    viewshow1.tk.call('wm','iconphoto',viewshow1._w,viewshow1_icon)
        
def ViewShow01() :
    global tree2
    TopViewForm3 = Frame(viewshow1, width=600, bd=1, relief=SOLID)
    TopViewForm3.pack(side=TOP, fill=X)
    LeftViewForm3 = Frame(viewshow1, width=800)
    LeftViewForm3.pack(side=LEFT, fill=Y)
    MidViewForm3 = Frame(viewshow1, width=800)
    MidViewForm3.pack(side=RIGHT)
    lbl_text3 = Label(TopViewForm3,font=('arial', 18), width=600)
    lbl_text3.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_text3.pack(fill=X)
    lbl_txtsearch3 = Label(LeftViewForm3, text="Gabungan Tabel Registrasi & Ijazah", font=('arial', 10),foreground ="#FF00FF")
    lbl_txtsearch3.pack(side=TOP, anchor=W)		
    scrollbarx3 = Scrollbar(LeftViewForm3, orient=HORIZONTAL)
    scrollbary3 = Scrollbar(LeftViewForm3, orient=VERTICAL)
    tree2= ttk.Treeview(LeftViewForm3, columns=("No","Nama","Nomor Peserta","Nomor Induk","TTL","Nama Ortu","Asal Sekolah","Tahun Lulus","DN"), selectmode="extended", height=100, yscrollcommand=scrollbary3.set, xscrollcommand=scrollbarx3.set)
    scrollbary3.config(command=tree2.yview)
    scrollbary3.pack(side=RIGHT, fill=Y)
    scrollbarx3.config(command=tree2.xview)
    scrollbarx3.pack(side=BOTTOM, fill=X)
    tree2.heading('No', text="No",anchor=W)#0
    tree2.heading('Nama', text="Nama",anchor=W)#1
    tree2.heading('Nomor Peserta', text="Nomor Peserta",anchor=W)#2
    tree2.heading('Nomor Induk', text="Nomor Induk",anchor=W)#3
    tree2.heading('TTL', text="TTL",anchor=W)#4
    tree2.heading('Nama Ortu', text="Nama Ortu",anchor=W)#5
    tree2.heading('Asal Sekolah', text="Asal Sekolah",anchor=W)#6
    tree2.heading('Tahun Lulus', text="Tahun Lulus",anchor=W)#7
    tree2.heading('DN', text="DN",anchor=W)#8
    tree2.column('#0', stretch=NO, minwidth=0, width=0)
    tree2.column('#1', stretch=NO, minwidth=0, width=90)
    tree2.column('#2', stretch=NO, minwidth=0, width=90)
    tree2.column('#3', stretch=NO, minwidth=0, width=90)
    tree2.column('#4', stretch=NO, minwidth=0, width=90)
    tree2.column('#5', stretch=NO, minwidth=0, width=90)
    tree2.column('#6', stretch=NO, minwidth=0, width=90)
    tree2.column('#7', stretch=NO, minwidth=0, width=90)
    tree2.column('#8', stretch=NO, minwidth=0, width=90)
    tree2.column('#9', stretch=NO, minwidth=0, width=90)
    tree2.pack()
    DisplayData3()
	
def DisplayData3():
    Database2()
    cursor.execute("SELECT Tabel_Ijazah.NO2 ,Tabel_Registrasi.NAMA1,Tabel_Ijazah.NOMORPESERTA2,Tabel_Ijazah.NOMORINDUK2,Tabel_Ijazah.TTL2,Tabel_Ijazah.NAMAORTU2,Tabel_Ijazah.ASALSEKOLAH2,Tabel_Ijazah.TAHUNLULUS2,Tabel_Ijazah.DN2 FROM Tabel_Registrasi INNER JOIN Tabel_Ijazah ON Tabel_Registrasi.NO1=Tabel_Ijazah.NO2")
    fetch = cursor.fetchall()
    for data in fetch:
        tree2.insert('', 'end', values=(data))
    cursor.close()
    conn.close()	
	

#Ijazah (Database2)
def ShowAddNew2():
    global addnewform2
    addnewform2 = Toplevel()
    addnewform2.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform2.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform2.resizable(0, 0)
    AddNewForm2()

#Membuat ikon
    addnewform2_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform2.tk.call('wm','iconphoto',addnewform2._w,addnewform2_icon)

def AddNewForm2():
#===============================Frame 02====================================================
    TopAddNew2 = Frame(addnewform2, width=300, height=400, bd=1, relief=SOLID)
    TopAddNew2.pack(side=TOP, pady=2)
    LeftAddNew2 = Frame(addnewform2, width=300, height=500, bd=8, relief="raise")
    LeftAddNew2.pack(side=LEFT)
    RightAddNew2 = Frame(addnewform2, width=300, height=600, bd=8, relief="raise")
    RightAddNew2.pack(side=RIGHT)
    Forms2 = Frame(LeftAddNew2, width=300, height=450)
    Forms2.pack(side=TOP)
    Buttons2 = Frame(LeftAddNew2,width=300, height=100, bd=8, relief="raise")
    Buttons2.pack(side=BOTTOM)
    searchframe2=Frame(RightAddNew2,bd=8,width=392,height=150,relief="raise")
    searchframe2.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
    lbl_text2 = Label(TopAddNew2, text="Data Ijazah SMA/SMK/MA", font=('arial', 12), width=900)
    lbl_text2.pack(fill=X)
    lbl_text2.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_NO2 = Label(Forms2, text="Nomor ", font=('arial', 12), bd=2)
    lbl_NO2.grid(row=0,column=0, sticky=W)
    lbl_NO2.config(foreground ="#00FFFF")    
    NO_2 = Entry(Forms2, textvariable=NO2, font=('arial', 12), width=32,bd=2)
    NO_2.grid(row=0, column=1, sticky=W)
    lbl_NOMORPESERTA_2 = Label(Forms2, text="Nomor Peserta", font=('arial', 12), bd=2)
    lbl_NOMORPESERTA_2.grid(row=1,column=0, sticky=W)
    lbl_NOMORPESERTA_2.config(foreground ="#00FFFF") 
    NOMORPESERTA_2= Entry(Forms2, textvariable=NOMORPESERTA2, font=('arial', 12), width=32,bd=2)
    NOMORPESERTA_2.grid(row=1, column=1, sticky=W)
    lbl_NOMORINDUK_2 = Label(Forms2, text="Nomor Induk", font=('arial', 12), bd=2)
    lbl_NOMORINDUK_2.grid(row=2,column=0, sticky=W)
    lbl_NOMORINDUK_2.config(foreground ="#00FFFF") 
    NOMORINDUK_2= Entry(Forms2, textvariable=NOMORINDUK2, font=('arial', 12), width=32,bd=2)
    NOMORINDUK_2.grid(row=2, column=1, sticky=W)	
    lbl_TTL_2 = Label(Forms2, text="Tempat dan Tanggal Lahir", font=('arial', 12), bd=2)
    lbl_TTL_2.grid(row=3,column=0, sticky=W)
    lbl_TTL_2.config(foreground ="#00FFFF")
    TTL_2= Entry(Forms2, textvariable=TTL2, font=('arial', 12), width=32,bd=2)
    TTL_2.grid(row=3, column=1, sticky=W)	
    lbl_NAMAORTU_2 = Label(Forms2, text="Nama Orang Tua", font=('arial', 12), bd=2)
    lbl_NAMAORTU_2.grid(row=4,column=0, sticky=W)
    lbl_NAMAORTU_2.config(foreground ="#00FFFF")
    NAMAORTU_2= Entry(Forms2, textvariable=NAMAORTU2, font=('arial', 12), width=32,bd=2)
    NAMAORTU_2.grid(row=4, column=1, sticky=W)
    lbl_ASALSEKOLAH_2 = Label(Forms2, text="Asal Sekolah", font=('arial', 12), bd=2)
    lbl_ASALSEKOLAH_2.grid(row=5,column=0, sticky=W)
    lbl_ASALSEKOLAH_2.config(foreground ="#00FFFF")
    ASALSEKOLAH_2= Entry(Forms2, textvariable=ASALSEKOLAH2, font=('arial', 12), width=32,bd=2)
    ASALSEKOLAH_2.grid(row=5, column=1, sticky=W)
    lbl_TAHUNLULUS_2 = Label(Forms2, text="Tahun Lulus", font=('arial', 12), bd=2)
    lbl_TAHUNLULUS_2.grid(row=6,column=0, sticky=W)
    lbl_TAHUNLULUS_2.config(foreground ="#00FFFF")	
    TAHUNLULUS_2 = Spinbox(Forms2, from_=2013, to=9999, width=33,state ="readonly",textvariable=TAHUNLULUS2,bd=2)
    TAHUNLULUS_2.grid(row=6, column=1,sticky=W)
    lbl_DN_2 = Label(Forms2, text="DN", font=('arial', 12), bd=2)
    lbl_DN_2.grid(row=7,column=0, sticky=W)
    lbl_DN_2.config(foreground ="#00FFFF")
    DN_2= Entry(Forms2, textvariable=DN2, font=('arial', 12), width=32,bd=2)
    DN_2.grid(row=7, column=1, sticky=W)	
#====================BUTTONS WIDGET===========================================================================
    btn_add2 = Button(Buttons2, text="Save",bg="#009ACD",foreground ="white", command=AddNew2,font=('arial', 12), width=30)
    btn_add2.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search2 = Button(Buttons2, text="Pencarian", command=Search2,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_search2.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset2 = Button(Buttons2, text="Ulang", command=Reset2,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_reset2.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete2 = Button(Buttons2, text="Hapus",command=Delete2,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_delete2.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================	
    global tree2
    lbl_txtsearch2 = Label(RightAddNew2, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
    lbl_txtsearch2.pack(side=TOP, anchor=W)
    temp2.set("Nomor Peserta")
    searchoptions2=OptionMenu(searchframe2,temp2,"Nomor Peserta","Nomor Induk","Tahun Lulus")
    searchoptions2.pack(side=LEFT)
    search2 = Entry(RightAddNew2, textvariable=SEARCH2, font=('arial', 15), width=10)
    search2.pack(side=TOP,  padx=10, fill=X)
    scrollbarx2 = Scrollbar(RightAddNew2, orient=HORIZONTAL)
    scrollbary2 = Scrollbar(RightAddNew2, orient=VERTICAL)
    tree2= ttk.Treeview(RightAddNew2, columns=("NO","Nomor Peserta", "Nomor Induk", "TTL", "Nama Ortu","Asal Sekolah", "Tahun Lulus", "DN"), selectmode="extended", height=100, yscrollcommand=scrollbary2.set, xscrollcommand=scrollbarx2.set)
    scrollbary2.config(command=tree2.yview)
    scrollbary2.pack(side=RIGHT, fill=Y)
    scrollbarx2.config(command=tree2.xview)
    scrollbarx2.pack(side=BOTTOM, fill=X)
    tree2.heading('NO', text="NO",anchor=W)#0
    tree2.heading('Nomor Peserta', text="Nomor Peserta",anchor=W)#1
    tree2.heading('Nomor Induk', text="Nomor Induk",anchor=W)#2
    tree2.heading('TTL', text="TTL",anchor=W)#3
    tree2.heading('Nama Ortu', text="Nama Ortu",anchor=W)#4
    tree2.heading('Asal Sekolah', text="Asal Sekolah",anchor=W)#5
    tree2.heading('Tahun Lulus', text="Tahun Lulus",anchor=W)#6
    tree2.heading('DN', text="DN",anchor=W)#7
    tree2.column('#0', stretch=NO, minwidth=0, width=0)
    tree2.column('#1', stretch=NO, minwidth=0, width=120)
    tree2.column('#2', stretch=NO, minwidth=0, width=120)
    tree2.column('#3', stretch=NO, minwidth=0, width=189)
    tree2.column('#4', stretch=NO, minwidth=0, width=189)
    tree2.column('#5', stretch=NO, minwidth=0, width=189)
    tree2.column('#6', stretch=NO, minwidth=0, width=189)
    tree2.column('#7', stretch=NO, minwidth=0, width=189)
    tree2.pack()
    DisplayData2()

def AddNew2():
    Database2()
    cursor.execute("INSERT INTO `Tabel_Ijazah` (NO2,NOMORPESERTA2,NOMORINDUK2,TTL2,NAMAORTU2,ASALSEKOLAH2,TAHUNLULUS2,DN2) VALUES(?,?,?,?,?,?,?,?)", (str(NO2.get()),str(NOMORPESERTA2.get()), str(NOMORINDUK2.get()), str(TTL2.get()),str(NAMAORTU2.get()),str(ASALSEKOLAH2.get()),str(TAHUNLULUS2.get()),str(DN2.get())))
    conn.commit()
    NO2.set("")#0
    NOMORPESERTA2.set("")#1
    NOMORINDUK2.set("")#2
    TTL2.set("")#3
    NAMAORTU2.set("")#4
    ASALSEKOLAH2.set("")#5
    TAHUNLULUS2.set("")#6
    DN2.set("")#7
    cursor.close()
    conn.close()
	
def DisplayData2():
    Database2()
    cursor.execute("SELECT * FROM `Tabel_Ijazah`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree2.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search2():
    tree2.delete(*tree2.get_children())
    Database2()
    if(temp2.get()=="Nomor Peserta"):
      cursor.execute("SELECT * FROM 'Tabel_Ijazah' WHERE NOMORPESERTA2 LIKE '%s' ORDER BY '' ASC" %SEARCH2.get())
    elif(temp2.get()=="Nomor Induk"):
      cursor.execute("SELECT * FROM 'Tabel_Ijazah' WHERE NOMORINDUK2 LIKE '%s' ORDER BY '' ASC" %SEARCH2.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_Ijazah' WHERE TAHUNLULUS2 LIKE '%s' ORDER BY '' ASC" %SEARCH2.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree2.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Delete2():
    if not tree2.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Data Ijazah', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
        if result == 'yes':
            curItem = tree2.focus()
            contents =(tree2.item(curItem))
            selecteditem = contents['values']
            tree2.delete(curItem)
            Database2()
            cursor.execute("DELETE FROM `Tabel_Ijazah` WHERE `NO2` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#Tabel_Registrasi
def Reset2():
    tree2.delete(*tree2.get_children())
    DisplayData2()
    SEARCH2.set("")

#Registrasi
def ShowAddNew1():
    global addnewform1
    addnewform1 = Toplevel()
    addnewform1.title("SIAKAD")
    width = 1200
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform1.resizable(0, 0)
    AddNewForm1()

#Membuat ikon
    addnewform1_icon = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")
    addnewform1.tk.call('wm','iconphoto',addnewform1._w,addnewform1_icon)

def AddNewForm1():
#===============================Frame 01====================================================
    TopAddNew1 = Frame(addnewform1, width=300, height=400, bd=1, relief=SOLID)
    TopAddNew1.pack(side=TOP, pady=2)
    LeftAddNew1 = Frame(addnewform1, width=300, height=500, bd=8, relief="raise")
    LeftAddNew1.pack(side=LEFT)
    RightAddNew1 = Frame(addnewform1, width=300, height=600, bd=8, relief="raise")
    RightAddNew1.pack(side=RIGHT)
    Forms1 = Frame(LeftAddNew1, width=300, height=450)
    Forms1.pack(side=TOP)
    Buttons1 = Frame(LeftAddNew1,width=300, height=100, bd=8, relief="raise")
    Buttons1.pack(side=BOTTOM)
    searchframe1=Frame(RightAddNew1,bd=8,width=392,height=150,relief="raise")
    searchframe1.pack(side=TOP)
#=========================================LABEL  & ENTRY WIDGET ===========================================
    lbl_text1 = Label(TopAddNew1, text="Data Registrasi", font=('arial', 12), width=900)
    lbl_text1.pack(fill=X)
    lbl_text1.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
    lbl_N01 = Label(Forms1, text="Nomor ", font=('arial', 12), bd=2)
    lbl_N01.grid(row=0,column=0, sticky=W)
    lbl_N01.config(foreground ="#00FFFF")
    lbl_NAMA1 = Label(Forms1, text="Nama", font=('arial', 12), bd=2)
    lbl_NAMA1.grid(row=1,column=0, sticky=W)
    lbl_NAMA1.config(foreground ="#00FFFF")
    lbl_PRODI1 = Label(Forms1, text="Program Studi ", font=('arial', 12), bd=2)
    lbl_PRODI1.grid(row=2,column=0, sticky=W)
    lbl_PRODI1.config(foreground ="#00FFFF")
    lbl_PROPE1 = Label(Forms1, text="Program Pendidikan ", font=('arial', 12), bd=2)
    lbl_PROPE1.grid(row=3,column=0, sticky=W)
    lbl_PROPE1.config(foreground ="#00FFFF")
    lbl_AGAMA1 = Label(Forms1, text="Agama ", font=('arial', 12), bd=2)
    lbl_AGAMA1.grid(row=4,column=0, sticky=W)
    lbl_AGAMA1.config(foreground ="#00FFFF")
    lbl_NOHP1 = Label(Forms1, text="No Hp ", font=('arial', 12), bd=2)
    lbl_NOHP1.grid(row=5,column=0, sticky=W)
    lbl_NOHP1.config(foreground ="#00FFFF")
    lbl_ALAMAT1 = Label(Forms1, text="Alamat ", font=('arial', 12), bd=2)
    lbl_ALAMAT1.grid(row=6,column=0, sticky=W)
    lbl_ALAMAT1.config(foreground ="#00FFFF")
    lbl_EMAIL1 = Label(Forms1, text="Email ", font=('arial', 12), bd=2)
    lbl_EMAIL1.grid(row=7,column=0, sticky=W)
    lbl_EMAIL1.config(foreground ="#00FFFF")
    lbl_JENKEL1 = Label(Forms1, text="Jenisn Kelamin ", font=('arial', 12), bd=2)
    lbl_JENKEL1.grid(row=8,column=0, sticky=W)
    lbl_JENKEL1.config(foreground ="#00FFFF")
    NO01 = Entry(Forms1, textvariable=NO1, font=('arial', 12), width=32,bd=2)
    NO01.grid(row=0, column=1, sticky=W)
    NAMA01= Entry(Forms1, textvariable=NAMA1, font=('arial', 12), width=32,bd=2)
    NAMA01.grid(row=1, column=1, sticky=W)
    PRODI01=ttk.Combobox(Forms1,font=('arial', 12),state ="readonly", textvariable=PRODI1, width=30)
    PRODI01['values']= ("","IT","SI")
    PRODI01.current(0) 
    PRODI01.grid(column=1, row=2,sticky="W")
    PROPE01=ttk.Combobox(Forms1,font=('arial', 12),state ="readonly", textvariable=PROPE1, width=30)
    PROPE01['values']= ("","S1","Profesi 2 tahun","D3")
    PROPE01.current(0) 
    PROPE01.grid(column=1, row=3,sticky="W")
    AGAMA01=ttk.Combobox(Forms1,font=('arial', 12),state ="readonly", textvariable=AGAMA1, width=30)
    AGAMA01['values']= ("","Kristen Protestan","Katolik","Islam","Budha","Hindu")
    AGAMA01.current(0) 
    AGAMA01.grid(column=1, row=4,sticky="W")
    NOHP01= Entry(Forms1, textvariable=NOHP1, font=('arial', 12), width=32,bd=2)
    NOHP01.grid(row=5, column=1, sticky=W)
    ALAMAT01= Entry(Forms1, textvariable=ALAMAT1, font=('arial', 12), width=32,bd=2)
    ALAMAT01.grid(row=6, column=1, sticky=W)
    EMAIL01= Entry(Forms1, textvariable=EMAIL1, font=('arial', 12), width=32,bd=2)
    EMAIL01.grid(row=7, column=1, sticky=W)
    JENKEL01=ttk.Combobox(Forms1,font=('arial', 12),state ="readonly", textvariable=JENKEL1, width=30)
    JENKEL01['values']= ("","P","L")
    JENKEL01.current(0) 
    JENKEL01.grid(column=1, row=8,sticky="W")	
#====================BUTTONS WIDGET===========================================================================
    btn_add1 = Button(Buttons1, text="Save",bg="#009ACD",foreground ="white", command=AddNew1,font=('arial', 12), width=30)
    btn_add1.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search1 = Button(Buttons1, text="Pencarian", command=Search1,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_search1.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset1 = Button(Buttons1, text="Ulang", command=Reset1,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_reset1.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete1 = Button(Buttons1, text="Hapus",command=Delete1,bg="#009ACD",foreground ="white",font=('arial', 12), width=30)
    btn_delete1.pack(side=TOP, padx=10, pady=10, fill=X) 
#===============================================LIST WIDGET================================================	
    global tree1
    lbl_txtsearch1 = Label(RightAddNew1, text="Pencarian", font=('arial', 15),foreground ="#FF00FF")
    lbl_txtsearch1.pack(side=TOP, anchor=W)
    temp1.set("NO")
    searchoptions1=OptionMenu(searchframe1,temp1,"NO","Program Studi","Program Pendidikan")
    searchoptions1.pack(side=LEFT)
    search1 = Entry(RightAddNew1, textvariable=SEARCH1, font=('arial', 15), width=10)
    search1.pack(side=TOP,  padx=10, fill=X)
    scrollbarx1 = Scrollbar(RightAddNew1, orient=HORIZONTAL)
    scrollbary1 = Scrollbar(RightAddNew1, orient=VERTICAL)
    tree1= ttk.Treeview(RightAddNew1, columns=("NO","Nama", "Program Studi", "Program Pendidikan", "Agama", "No Hp", "Alamat","Email","Jenis Kelamin"), selectmode="extended", height=100, yscrollcommand=scrollbary1.set, xscrollcommand=scrollbarx1.set)
    scrollbary1.config(command=tree1.yview)
    scrollbary1.pack(side=RIGHT, fill=Y)
    scrollbarx1.config(command=tree1.xview)
    scrollbarx1.pack(side=BOTTOM, fill=X)
    tree1.heading('NO', text="NO",anchor=W)#0
    tree1.heading('Nama', text="Nama",anchor=W)#1
    tree1.heading('Program Studi', text="Program Studi",anchor=W)#2
    tree1.heading('Program Pendidikan', text="Program Pendidikan",anchor=W)#3
    tree1.heading('Agama', text="Agama",anchor=W)#4
    tree1.heading('No Hp', text="No Hp",anchor=W)#5
    tree1.heading('Alamat', text="Alamat",anchor=W)#6
    tree1.heading('Email', text="Email",anchor=W)#7
    tree1.heading('Jenis Kelamin', text="Jenis Kelamin",anchor=W)#8
    tree1.column('#0', stretch=NO, minwidth=0, width=0)
    tree1.column('#1', stretch=NO, minwidth=0, width=120)
    tree1.column('#2', stretch=NO, minwidth=0, width=120)
    tree1.column('#3', stretch=NO, minwidth=0, width=189)
    tree1.column('#4', stretch=NO, minwidth=0, width=189)
    tree1.column('#5', stretch=NO, minwidth=0, width=189)
    tree1.column('#6', stretch=NO, minwidth=0, width=189)
    tree1.column('#7', stretch=NO, minwidth=0, width=189)
    tree1.column('#8', stretch=NO, minwidth=0, width=189)
    tree1.pack()
    DisplayData1()

def AddNew1():
    Database1()
    cursor.execute("INSERT INTO `Tabel_Registrasi` (NO1,NAMA1,PRODI1 ,PROPE1,AGAMA1,NOHP1,ALAMAT1,EMAIL1,JENKEL1) VALUES(?,?,?,?,?,?,?,?,?)", (int(NO1.get()),str(NAMA1.get()), str(PRODI1.get()), str(PROPE1.get()),str(AGAMA1.get()),str(NOHP1.get()),str(ALAMAT1.get()),str(EMAIL1.get()),str(JENKEL1.get())))
    conn.commit()
    NO1.set("")#1
    NAMA1.set("")#2
    PRODI1.set("")#3
    PROPE1.set("")#4
    AGAMA1.set("")#5
    NOHP1.set("")#6
    AGAMA1.set("")#7
    EMAIL1.set("")#8
    JENKEL1.set("")#9
    cursor.close()
    conn.close()

def DisplayData1():
    Database1()
    cursor.execute("SELECT * FROM `Tabel_Registrasi`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree1.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
	
def Search1():
    tree1.delete(*tree1.get_children())
    Database1()
    if(temp1.get()=="NO"):
      cursor.execute("SELECT * FROM 'Tabel_Registrasi' WHERE NO1 LIKE '%s' ORDER BY '' ASC" %SEARCH1.get())
    elif(temp1.get()=="Program Studi"):
      cursor.execute("SELECT * FROM 'Tabel_Registrasi' WHERE PRODI1 LIKE '%s' ORDER BY '' ASC" %SEARCH1.get())
    else:
      cursor.execute("SELECT * FROM 'Tabel_Registrasi' WHERE PROPE1 LIKE '%s' ORDER BY '' ASC" %SEARCH1.get())
    fetch=cursor.fetchall()
    for data in fetch:
        tree1.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Delete1():
    if not tree1.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Data Registrasi', 'Anda yakin ingin menghapus rekaman ini?', icon="warning")
        if result == 'yes':
            curItem = tree1.focus()
            contents =(tree1.item(curItem))
            selecteditem = contents['values']
            tree1.delete(curItem)
            Database1()
            cursor.execute("DELETE FROM `Tabel_Registrasi` WHERE `NO1` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#Registrasi
def Reset1():
    tree1.delete(*tree1.get_children())
    DisplayData1()
    SEARCH1.set("")

def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Harap lengkapi nama pengguna dan kata sandi yang wajib diisi!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="nama pengguna dan kata sandi salah", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close() 			

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()
	
#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
#Membuat ikon
masuk_png = PhotoImage(file="J:\SIAKAD\Gambar\masuk1.png")
filemenu.add_command(image=masuk_png,command=ShowLoginForm,foreground ="#00FFFF",background ="purple4")
filemenu.add_separator()
keluar_png = PhotoImage(file="J:\SIAKAD\Gambar\keluar1.png") 
filemenu.add_command(image=keluar_png, command=Exit,foreground ="#00FFFF",background ="purple4")
menubar.add_cascade(label="Admin Masuk", menu=filemenu,foreground ="#00FFFF",background ="purple4")
root.config(menu=menubar)
#========================================FRAME============================================
Title = Frame(root, bd=0,relief="flat")
Title.pack(pady=10)
canvas = Canvas(root, width = 380, height =210,background ="purple4")      
canvas.pack()
#========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="SIAKAD", font=('arial', 26))
lbl_display.pack()
lbl_display.config(foreground ="#00FFFF",background ="purple4",highlightthickness=3)
img = PhotoImage(file="J:\SIAKAD\Gambar\logo.png")      
canvas.create_image(50,50, anchor=NW, image=img) 
#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
