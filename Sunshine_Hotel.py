from tkinter import *
import random
import time

root = Tk()
root.geometry ("1600x800+0+0")
root.title("Sunshine Hotel System")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width = 1600,height=50,bg="palegreen1",relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#====================Time=======================================================
localtime=time.asctime(time.localtime(time.time()))#Date Time Function
#======================Info=====================================================
lblInfo = Label(Tops, font=('Cooper Black',25),text = "Sunshine Hotel System" "P.O. Box 142-20200, Kericho" "PIN: A006065436T"
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

    CoChips = float(Chips.get())
    CoChapati = float(Chapati.get())
    CoUgali = float(Ugali.get())
    CoPilau = float(Pilau.get())
    CoFish = float(Fish.get())
    CoDrinks = float(Drinks.get())

    CostofChips = CoChips * 80
    CostofChapati = CoChapati * 20
    CostofUgali = CoUgali * 30
    CostofPilau = CoPilau * 100
    CostofFish = CoFish * 130
    CostofDrinks = CoDrinks * 50

    CostofMeal = "Ksh", str('%.2f' % (CostofChips + CostofChapati + CostofUgali +
                                      CostofPilau + CostofFish + CostofDrinks))

    Vat = ((CostofChips + CostofChapati + CostofUgali
            + CostofPilau + CostofFish + CostofDrinks)*0.16)

    TotalCost = (CostofChips + CostofChapati + CostofUgali
            + CostofPilau + CostofFish + CostofDrinks)

    Ser_Charge = ((CostofChips + CostofChapati + CostofUgali
            + CostofPilau + CostofFish + CostofDrinks)/99)

    Service = "Ksh", str('%.2f' % Ser_Charge)
    OverallCost = "Ksh", str('%.2f' % (Vat + TotalCost + Ser_Charge))
    PaidVAT = "Ksh", str('%.2f' % Vat)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    VAT.set(Vat)
    SubTotal.set(CostofMeal)
    Total.set(OverallCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Chapati.set("")
    Ugali.set("")
    Pilau.set("")
    Fish.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    VAT.set("")
    Cost.set("")
    Chips.set("")

txtDisplay = Entry(f2,font=('Arial',20), textvariable=text_Input, bd=30, insertwidth=6,
                   bg="#eddcdc", justify='right')
txtDisplay.grid(columnspan=6)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="7", bg="palegreen1",command=lambda: btnClick(7)).grid(row=2, column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="8", bg="palegreen1",command=lambda: btnClick(8)).grid(row=2, column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="9", bg="palegreen1",command=lambda: btnClick(9)).grid(row=2, column=2)

Addition=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="+", bg="palegreen1",command=lambda: btnClick("+")).grid(row=2, column=3)
#============================================================================================
btn4=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="4", bg="palegreen1",command=lambda: btnClick(4)).grid(row=3, column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="5", bg="palegreen1",command=lambda: btnClick(5)).grid(row=3, column=1)

btn6=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="6", bg="palegreen1",command=lambda: btnClick(6)).grid(row=3, column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="-", bg="palegreen1",command=lambda: btnClick("-")).grid(row=3, column=3)
#============================================================================================
btn1=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="1", bg="palegreen1",command=lambda: btnClick(1)).grid(row=4, column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="2", bg="palegreen1",command=lambda: btnClick(2)).grid(row=4, column=1)

btn3=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="3", bg="palegreen1",command=lambda: btnClick(3)).grid(row=4, column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="*", bg="palegreen1",command=lambda: btnClick("*")).grid(row=4, column=3)
#========================================================================================
btn0=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="0", bg="palegreen1",command=lambda: btnClick(0)).grid(row=5, column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="C", bg="palegreen1", command=btnClearDisplay).grid(row=5, column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="=", bg="palegreen1", command=btnEqualsInput).grid(row=5, column=2)

Division=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('Arial',20,'bold'),
            text="/", bg="palegreen1",command=lambda: btnClick("/")).grid(row=5, column=3)
#===============================Sunshine Hotel Info 1======================================
rand=StringVar()
Chips=StringVar()
Ugali=StringVar()
Chapati=StringVar()
Pilau=StringVar()
Fish=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
VAT=StringVar()
Cost=StringVar()
CostofMeal=StringVar()

lblReceipt_Number = Label(f1, font =('arial',16,'bold'), text="Receipt Number", bd=16, anchor='w')
lblReceipt_Number.grid(row=0,column=2)
txtReceipt_Number=Entry(f1, font =('arial',16,'bold'), textvariable=rand, bd=10, insertwidth=4,
                   bg="#f26060",justify='right')
txtReceipt_Number.grid(row=0,column=3)

lblChips = Label(f1, font =('arial',16,'bold'), text="Chips", bd=16, anchor='w')
lblChips.grid(row=1,column=0)
txtChips=Entry(f1, font =('arial',16,'bold'), textvariable=Chips, bd=10, insertwidth=4,
                   bg="palegreen1",justify='right')
txtChips.grid(row=1,column=1)

lblChapati = Label(f1, font =('arial',16,'bold'), text="Chapati", bd=16, anchor='w')
lblChapati.grid(row=2,column=0)
txtChapati=Entry(f1, font =('arial',16,'bold'), textvariable=Chapati, bd=10, insertwidth=4,
                   bg="palegreen1",justify='right')
txtChapati.grid(row=2,column=1)

lblUgali = Label(f1, font =('arial',16,'bold'), text="Ugali", bd=16, anchor='w')
lblUgali.grid(row=3,column=0)
txtUgali=Entry(f1, font =('arial',16,'bold'), textvariable=Ugali, bd=10, insertwidth=4,
                   bg="palegreen1",justify='right')
txtUgali.grid(row=3,column=1)

lblPilau = Label(f1, font =('arial',16,'bold'), text="Pilau", bd=16, anchor='w')
lblPilau.grid(row=4,column=0)
txtPilau=Entry(f1, font =('arial',16,'bold'), textvariable=Pilau, bd=10, insertwidth=4,
                   bg="palegreen1",justify='right')
txtPilau.grid(row=4,column=1)

lblFish = Label(f1, font =('arial',16,'bold'), text="Fish", bd=16, anchor='w')
lblFish.grid(row=5,column=0)
txtFish=Entry(f1, font =('arial',16,'bold'), textvariable=Fish, bd=10, insertwidth=4,
                   bg="palegreen1",justify='right')
txtFish.grid(row=5,column=1)

#===============================Sunshine Hotel Info 2======================================
lblDrinks = Label(f1, font =('arial',16,'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0,column=0)
txtDrinks=Entry(f1, font =('arial',16,'bold'), textvariable=Drinks, bd=10, insertwidth=4,
                   bg="palegreen1",justify='right')
txtDrinks.grid(row=0,column=1)

#=============Temporary Removal of Cost of Meal========================================
#lblCost = Label(f1, font =('arial',16,'bold'), text="Cost of Meal", bd=16, anchor='w')
#lblCost.grid(row=1,column=2)
#txtCost=Entry(f1, font =('arial',16,'bold'), textvariable=CostofMeal, bd=10, insertwidth=4,
#                   bg="palegreen1",justify='right')
#txtCost.grid(row=1,column=3)

lblService = Label(f1, font =('arial',16,'bold'), text="Service Charge", bd=16, anchor='w')
lblService.grid(row=2,column=2)
txtService=Entry(f1, font =('arial',16,'bold'), textvariable=Service_Charge, bd=10, insertwidth=4,
                   bg="#f26060",justify='right')
txtService.grid(row=2,column=3)


lblVAT = Label(f1, font =('arial',16,'bold'), text="VAT", bd=16, anchor='w')
lblVAT.grid(row=3,column=2)
txtVAT=Entry(f1, font =('arial',16,'bold'), textvariable=VAT, bd=10, insertwidth=4,
                         bg="#f26060",justify='right')
txtVAT.grid(row=3,column=3)

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

btnExit_Receipt=Button(f1,padx=8,pady=6,bd=3, fg="black",font=('arial',18,'bold'), width=9,
                           text="Exit", bg="#bcadad", command= qExit).grid(row=7, column=3)

root.mainloop()


