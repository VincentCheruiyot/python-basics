from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

root = Tk()
root.title("Python: Pro Tennis Academy")

width = 512
height = 360
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#ea62dc")

# ========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
CLIENT_NAME = StringVar()
GENDER = IntVar()
DATE_OF_BIRTH = IntVar()
PARENT_CONTACTS = IntVar()
PACKAGE_PRICE = IntVar()
CLIENT_PACKAGE = IntVar()
TIME = IntVar()
SEARCH = StringVar()


# ========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `client` (client_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, client_name TEXT, client_package TEXT, package_price TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()


def Exit():
    result = tkMessageBox.askquestion('Pro Tennis Academy', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Exit2():
    result = tkMessageBox.askquestion('Pro Tennis Academy', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()


def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Pro Tennis Academy/Account Login")
    width = 300
    height = 250
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()


def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=800, height=200, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Account Login", font=('Cooper Black', 20), width=150)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=150)
    MidLoginForm.pack(side=TOP, pady=25)
    lbl_username = Label(MidLoginForm, text="Username:", font=('Cooper Black', 13), bd=8)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('Cooper Black', 13), bd=8)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('Cooper Black', 15))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 15), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 15), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('Cooper Black', 12), width=8, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=10)
    btn_login.bind('<Return>', Login)


def Home():
    global Home
    Home = Tk()
    Home.title("Pro Tennis Academy/Home")
    width = 400
    height = 300
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Pro Tennis Academy", font=('Cooper Black', 25))
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label= "Register new client", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Client", menu=filemenu2)
    Home.config(menu=menubar)
    Home.config(bg="#99ff99")


def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Pro Tennis Academy/Register New Client")
    width = 800
    height = 600
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()


def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=50, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=10)
    lbl_text = Label(TopAddNew, text="Register New Client", font=('Cooper Black', 25), width=1000)
    lbl_text.pack(fill=X)
    LeftAddNew = Frame(addnewform, width=600)
    LeftAddNew.pack(side=LEFT, pady=50)
    lbl_clientname = Label(LeftAddNew, text="Client Name:", font=('Cooper Black', 15), bd=7)
    lbl_clientname.grid(row=0, sticky=W)
    lbl_gender = Label(LeftAddNew, text="Gender:", font=('Cooper Black', 15), bd=7)
    lbl_gender.grid(row=1, sticky=W)
    lbl_dateofbirth = Label(LeftAddNew, text="Date of Birth:", font=('Cooper Black', 15), bd=7)
    lbl_dateofbirth.grid(row=2, sticky=W)
    lbl_parentcontacts = Label(LeftAddNew, text="Parent Contacts:", font=('Cooper Black', 15), bd=7)
    lbl_parentcontacts.grid(row=3, sticky=W)
    lbl_package = Label(LeftAddNew, text="Package:", font=('Cooper Black', 15), bd=7)
    lbl_package.grid(row=4, sticky=W)
    lbl_price = Label(LeftAddNew, text="Package Price:", font=('Cooper Black', 15), bd=7)
    lbl_price.grid(row=5, sticky=W)
    lbl_time = Label(LeftAddNew, text="Time:", font=('Cooper Black', 15), bd=7)
    lbl_time.grid(row=6, sticky=W)
    clientname = Entry(LeftAddNew, textvariable=CLIENT_NAME, font=('Arial', 15), width=30)
    clientname.grid(row=0, column=1)
    gender = Entry(LeftAddNew, textvariable=GENDER, font=('Arial', 15), width=30)
    gender.grid(row=1, column=1)
    dateofbirth = Entry(LeftAddNew, textvariable=DATE_OF_BIRTH, font=('Arial', 15), width=30)
    dateofbirth.grid(row=2, column=1)
    parentcontacts = Entry(LeftAddNew, textvariable=PARENT_CONTACTS, font=('Arial', 15), width=30)
    parentcontacts.grid(row=3, column=1)
    clientpackage = Entry(LeftAddNew, textvariable=CLIENT_PACKAGE, font=('Arial', 15), width=30)
    clientpackage.grid(row=4, column=1)
    packageprice = Entry(LeftAddNew, textvariable=PACKAGE_PRICE, font=('Arial', 15), width=30)
    packageprice.grid(row=5, column=1)
    time = Entry(LeftAddNew, textvariable=TIME, font=('Arial', 15), width=30)
    time.grid(row=6, column=1)
    btn_add = Button(LeftAddNew, text="Save Details", font=('Cooper Black', 12), width=10, bg="#99ff99", command=AddNew)
    btn_add.grid(row=7, columnspan=2, pady=25)


def AddNew():
    Database()
    cursor.execute("INSERT INTO `client` (client_name, gender, date_of_birth, parent_contacts, client_package, package_price, time) VALUES(?, ?, ?)",
                   (str(CLIENT_NAME.get()),str(GENDER.get()), int(DATE_OF_BIRTH.get()), int(PARENT_CONTACTS.get()),int(CLIENT_PACKAGE.get()), int(PACKAGE_PRICE.get()), int(TIME.get())))
    conn.commit()
    CLIENT_NAME.set("")
    GENDER.set("")
    DATE_OF_BIRTH.set("")
    PARENT_CONTACTS.set("")
    PACKAGE_PRICE.set("")
    CLIENT_PACKAGE.set("")
    TIME.set("")
    cursor.close()
    conn.close()


def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Client Details", font=('Cooper Black', 18), width=900)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Client ID", "Client Name", "Gender","Date of Birth", "Parent Contacts",
                                              "Client Package", "Package Price", "Time"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Client ID', text="#", anchor=W)
    tree.heading('Client Name', text="Client Name", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('Date of Birth', text="Date of Birth", anchor=W)
    tree.heading('Parent Contacts', text="Parent Contacts", anchor=W)
    tree.heading('Client Package', text="Client Package", anchor=W)
    tree.heading('Package Price', text="Package Price", anchor=W)
    tree.heading('Time', text="Time", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
    tree.column('#7', stretch=NO, minwidth=0, width=100)
    tree.pack()
    DisplayData()


def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `client`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `client` WHERE `client_name` LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")


def Delete():
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion('Pro Tennis Academy', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `client` WHERE `client_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Pro Tennis Academy/View Clients")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()


def Logout():
    result = tkMessageBox.askquestion('Pro Tennis Academy', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        Home.destroy()


def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()


# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# ========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

# ========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="Pro Tennis Academy", font=('Cooper Black', 36))
lbl_display.pack()

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()



