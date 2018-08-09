from tkinter import *
import random
import time

root = Tk()
root.geometry ("1600x800+0+0")
root.title("Sunshine Pub System")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width = 1600,height=50,bg="#ef7575",relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800,height=700,relief=SUNKEN)
f1.pack(side=RIGHT)

#f2 = Frame(root, width = 300,height=700,relief=SUNKEN)
#f2.pack(side=RIGHT)

#f3 = Frame(root, width = 1000,height=900,relief=SUNKEN)
#f3.pack(side=LEFT)
#====================Time=======================================================
localtime=time.asctime(time.localtime(time.time()))
#======================Info=====================================================
lblInfo = Label(Tops, font=('Cooper Black',25),text = "Sunshine Pub System"
                , fg="Black",bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblDateTime = Label(Tops, font=('Times New Roman',10,'bold'),text = localtime, fg="Black",bd=10, anchor='w')
lblDateTime.grid(row=1,column=0)
#======================Calculator================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Receipt_Number():
    x = random.randint(101, 19999)
    randomReceipt_Number = str(x)
    rand.set(randomReceipt_Number)

    CoBeer = float(Beer.get())
    CoUdv = float(Udv.get())
    CoCans = float(Cans.get())
    CoLiquors = float(Liquors.get())

    CostofBeer = CoBeer * 80
    CostofUdv = CoUdv * 20
    CostofCans = CoCans * 30
    CostofLiquors = CoLiquors * 100

    CostofDrinks = "Ksh", str('%.2f' % (CostofBeer + CostofUdv + CostofCans + CostofLiquors))

    TotalCost = (CostofBeer + CostofUdv + CostofCans + CostofLiquors)

    Vat = ((CostofBeer + CostofUdv + CostofCans + CostofLiquors) * 0.16)

    Ser_Charge = ((CostofBeer + CostofUdv + CostofCans + CostofLiquors)/99)

    Service = "Ksh", str('%.2f' % Ser_Charge)
    OverallCost = "Ksh", str('%.2f' % (Vat + TotalCost + Ser_Charge))
    Vat = "Ksh", str('%.2f' % Vat)
    Service_Charge.set(Service)
    Cost.set(CostofDrinks)
    VAT.set(Vat)
    SubTotal.set(CostofDrinks)
    Total.set(OverallCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Udv.set("")
    Cans.set("")
    Liquors.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    VAT.set("")
    Cost.set("")
    Beer.set("")

#txtDisplay = Entry(f2,font=('Arial',20), textvariable=text_Input, bd=30, insertwidth=6,
#                   bg="#eddcdc", justify='right')
#txtDisplay.grid(columnspan=6)

#btn7=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="7", bg="#ef7575",command=lambda: btnClick(7)).grid(row=2, column=0)

#btn8=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="8", bg="#ef7575",command=lambda: btnClick(8)).grid(row=2, column=1)

#btn9=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="9", bg="#ef7575",command=lambda: btnClick(9)).grid(row=2, column=2)

#Addition=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="+", bg="#ef7575",command=lambda: btnClick("+")).grid(row=2, column=3)
#============================================================================================
#btn4=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="4", bg="#ef7575",command=lambda: btnClick(4)).grid(row=3, column=0)

#btn5=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="5", bg="#ef7575",command=lambda: btnClick(5)).grid(row=3, column=1)

#btn6=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="6", bg="#ef7575",command=lambda: btnClick(6)).grid(row=3, column=2)

#Subtraction=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="-", bg="#ef7575",command=lambda: btnClick("-")).grid(row=3, column=3)
#============================================================================================
#btn1=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="1", bg="#ef7575",command=lambda: btnClick(1)).grid(row=4, column=0)

#btn2=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="2", bg="#ef7575",command=lambda: btnClick(2)).grid(row=4, column=1)

#btn3=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#           text="3", bg="#ef7575",command=lambda: btnClick(3)).grid(row=4, column=2)

#Multiply=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="*", bg="#ef7575",command=lambda: btnClick("*")).grid(row=4, column=3)
#========================================================================================
#btn0=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="0", bg="#ef7575",command=lambda: btnClick(0)).grid(row=5, column=0)

#btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="C", bg="#ef7575", command=btnClearDisplay).grid(row=5, column=1)

#btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#            text="=", bg="#ef7575", command=btnEqualsInput).grid(row=5, column=2)

#Division=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
#           text="/", bg="#ef7575",command=lambda: btnClick("/")).grid(row=5, column=3)
#===============================Sunshine Hotel Info 1======================================
rand=StringVar()
Beer=StringVar()
Udv=StringVar()
Cans=StringVar()
Liquors=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
VAT=StringVar()
Cost=StringVar()
CostofDrinks=StringVar()

lblReceipt_Number = Label(f1, font =('arial',16,'bold'), text="Receipt Number", bd=10, anchor='w')
lblReceipt_Number.grid(row=0,column=2)
txtReceipt_Number=Entry(f1, font =('arial',16,'bold'), textvariable=rand, bd=10, insertwidth=4,
                   bg="#f26060",justify='right')
txtReceipt_Number.grid(row=0,column=3)

#===================Dropdown=======================================

def Choose_Brand():
    print("")

root = Tk("Sunshine Brand Mix")

menu=Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Beer",menu=subMenu)
subMenu.add_command(label="Tusker Lite",command=Choose_Brand)
subMenu.add_command(label="Tusker Lager", command=Choose_Brand)

udvMenu=Menu(menu)
menu.add_cascade(label="UDV",menu=udvMenu)
udvMenu.add_command(label="Popov",command=Choose_Brand)
udvMenu.add_command(label="Richot", command=Choose_Brand)

cansMenu=Menu(menu)
menu.add_cascade(label="Cans",menu=cansMenu)
cansMenu.add_command(label="Guarana",command=Choose_Brand)
cansMenu.add_command(label="Faxe", command=Choose_Brand)


lblBeer = Label(f1, font =('arial',16,'bold'), text="Beer",bd=10, anchor='w')
lblBeer.grid(row=1,column=0)
txtBeer=Entry(f1, font =('arial',16,'bold'), textvariable=Beer, bd=10, insertwidth=4,
                   bg="#ef7575",justify='right')
txtBeer.grid(row=1,column=1)
list1=Listbox(height=6,width=35)
sb1=Scrollbar()
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

lblUdv = Label(f1, font =('arial',16,'bold'), text="UDV", bd=16, anchor='w')
lblUdv.grid(row=2,column=0)
txtUdv=Entry(f1, font =('arial',16,'bold'), textvariable=Udv, bd=10, insertwidth=4,
                   bg="#ef7575",justify='right')
txtUdv.grid(row=2,column=1)

lblCans = Label(f1, font =('arial',16,'bold'), text="Cans", bd=16, anchor='w')
lblCans.grid(row=3,column=0)
txtCans=Entry(f1, font =('arial',16,'bold'), textvariable=Cans, bd=10, insertwidth=4,
                   bg="#ef7575",justify='right')
txtCans.grid(row=3,column=1)

lblLiquors = Label(f1, font =('arial',16,'bold'), text="Liquors", bd=16, anchor='w')
lblLiquors.grid(row=4,column=0)
txtLiquors=Entry(f1, font =('arial',16,'bold'), textvariable=Liquors, bd=10, insertwidth=4,
                   bg="#ef7575",justify='right')
txtLiquors.grid(row=4,column=1)

#lblFish = Label(f1, font =('arial',16,'bold'), text="Fish", bd=16, anchor='w')
#lblFish.grid(row=5,column=0)
#txtFish=Entry(f1, font =('arial',16,'bold'), textvariable=Fish, bd=10, insertwidth=4,
#                   bg="#ef7575",justify='right')
#txtFish.grid(row=5,column=1)

#===============================Sunshine Hotel Info 2======================================
#lblDrinks = Label(f1, font =('arial',16,'bold'), text="Drinks", bd=16, anchor='w')
#lblDrinks.grid(row=0,column=0)
#txtDrinks=Entry(f1, font =('arial',16,'bold'), textvariable=Drinks, bd=10, insertwidth=4,
#                   bg="#ef7575",justify='right')
#txtDrinks.grid(row=0,column=1)

#=============Temporary Removal of Cost of Meal========================================
#lblCost = Label(f1, font =('arial',16,'bold'), text="Cost of Meal", bd=16, anchor='w')
#lblCost.grid(row=1,column=2)
#txtCost=Entry(f1, font =('arial',16,'bold'), textvariable=CostofMeal, bd=10, insertwidth=4,
#                   bg="palegreen1",justify='right')
#txtCost.grid(row=1,column=3)

lblService = Label(f1, font =('arial',16,'bold'), text="Service Charge", bd=16, anchor='w')
lblService.grid(row=2,column=2)
txtService=Entry(f1, font =('arial',16,'bold'), textvariable=Service_Charge, bd=10, insertwidth=2,
                   bg="#f26060",justify='right')
txtService.grid(row=2,column=3)


lblVat = Label(f1, font =('arial',16,'bold'), text="VAT", bd=16, anchor='w')
lblVat.grid(row=3,column=2)
txtVat=Entry(f1, font =('arial',16,'bold'), textvariable=VAT, bd=10, insertwidth=4,
                         bg="#f26060",justify='right')
txtVat.grid(row=3,column=3)

lblSubTotal = Label(f1, font =('arial',16,'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1, font =('arial',16,'bold'), textvariable=SubTotal, bd=10, insertwidth=4,
                   bg="#f26060",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost = Label(f1, font =('arial',16,'bold'), text="Total Cost", bd=16, anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1, font =('arial',16,'bold'), textvariable=Total, bd=10, insertwidth=4,
                   bg="#f26060",justify='right')
txtTotalCost.grid(row=5,column=3)

#=======================================Buttons=========================================
btnPrint_Receipt=Button(f1,padx=8,pady=6,bd=3, fg="black",font=('arial',18,'bold'), width=9,
                           text="Print Receipt", bg="#bcadad", command= Receipt_Number).grid(row=7, column=1)

btnReset=Button(f1,padx=8,pady=6,bd=3, fg="black",font=('arial',18,'bold'), width=9,
                           text="Reset", bg="#bcadad", command= Reset).grid(row=7, column=2)

btnExit=Button(f1,padx=8,pady=6,bd=3, fg="black",font=('arial',18,'bold'), width=9,
                           text="Exit", bg="#bcadad", command= qExit).grid(row=7, column=3)

root.mainloop()


