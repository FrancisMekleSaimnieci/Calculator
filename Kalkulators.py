from tkinter import*
mLogs=Tk()
mLogs.title("Kalkulātors")
mLogs.goemetry("300x300")

def btnClick(number):
    current=e.get()#nolasa esoso skaitli
    e.delete(0,END)#nodzes
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)
    return 0
def btnCommand(command):
    global num1 #jaiegaume skaitlis un darbiba
    global mathOp 
    mathOp=comand#+,-,*,/
    num1=int(e.get())
    e.delete(0,END)
    return 0

e=Entry(mansLogs, wdth=15, font=("Ariel Black",20))
e.grind(row=0, column=0, coulmspan=4)

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

btnsum=Button(mansLogs, text="+",padx="40", pady="20", cpmmand=lambda:btnClick("+"))
btnmin=Button(mansLogs, text="-",padx="40", pady="20", cpmmand=lambda:btnClick("-"))
btndal=Button(mansLogs, text="/",padx="40", pady="20", cpmmand=lambda:btnClick("/"))
btnreiz=Button(mansLogs, text="*",padx="40", pady="20", cpmmand=lambda:btnClick("*"))
btnvien=Button(mansLogs, text="=",padx="40", pady="20", cpmmand=lambda:btnClick("="))
btnpun=Button(mansLogs, text=".",padx="40", pady="20", cpmmand=lambda:btnClick("."))



