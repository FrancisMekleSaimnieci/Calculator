from ast import operator
from tkinter import*
from math import*
mansLogs=Tk()
mansLogs.title("Kalkulātors")
mansLogs.geometry("300x300")

def btnClick(number):
    current=e.get()#nolasa esoso skaitli
    e.delete(0,END)#nodzes
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)
    return 0

def btnCommand(command):
    global num1 #jaiegaume skaitlis un darbiba
    global mathOp 
    mathOp=command#+,-,*,/
    num1=int(e.get())
    e.delete(0,END)
    return 0

def vienads():
    global num2
    num2=(int(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0, END)
    e.insert(0, str(result))
    return 0

def notirit():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

def sq_rt():
    global operator
    global num1
    global mathOp
    num1=(float(e.get()))
    num1=sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)
    return 0

e=Entry(mansLogs, width=15, font=("Ariel Black",20))
e.grid(row=0, column=0, columnspan=4)

btn0=Button(mansLogs, text="0",padx="40", pady="20", command=lambda:btnClick(0))
btn1=Button(mansLogs, text="1",padx="40", pady="20", command=lambda:btnClick(1))
btn2=Button(mansLogs, text="2",padx="40", pady="20", command=lambda:btnClick(2))
btn3=Button(mansLogs, text="3",padx="40", pady="20", command=lambda:btnClick(3))
btn4=Button(mansLogs, text="4",padx="40", pady="20", command=lambda:btnClick(4))
btn5=Button(mansLogs, text="5",padx="40", pady="20", command=lambda:btnClick(5))
btn6=Button(mansLogs, text="6",padx="40", pady="20", command=lambda:btnClick(6))
btn7=Button(mansLogs, text="7",padx="40", pady="20", command=lambda:btnClick(7))
btn8=Button(mansLogs, text="8",padx="40", pady="20", command=lambda:btnClick(8))
btn9=Button(mansLogs, text="9",padx="40", pady="20", command=lambda:btnClick(9))

btnsum=Button(mansLogs, text="+",padx="40", pady="20", command=lambda:btnClick("+"))
btnmin=Button(mansLogs, text="-",padx="40", pady="20", command=lambda:btnClick("-"))
btndal=Button(mansLogs, text="/",padx="40", pady="20", command=lambda:btnClick("/"))
btnreiz=Button(mansLogs, text="*",padx="40", pady="20", command=lambda:btnClick("*"))
btnvien=Button(mansLogs, text="=",padx="40", pady="20", command=vienads)
btnpun=Button(mansLogs, text=".",padx="40", pady="20", command=lambda:btnClick("."))
btnClean=Button(mansLogs, text="C",padx="40", pady="20", command=notirit)

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btnsum.grid(row=1,column=3)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btnmin.grid(row=2,column=3)
 
btn7.grid(row=3,column=0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)
btndal.grid(row=3,column=3)

btn0.grid(row=4,column=0)
btnClean.grid(row=4,column=1)
btnreiz.grid(row=4,column=2)
btnvien.grid(row=4,column=3)

mansLogs.mainloop()