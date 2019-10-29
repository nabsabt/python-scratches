import tkinter as tk
import time

Height= 600
Width = 400

minHeight = 600
minWidth = 400

entryWidth = 15

parentWindow = tk.Tk()

canvas = tk.Canvas(parentWindow, height=Height, width=Width)
canvas.place()


frame = tk.Frame(parentWindow, bg='#80c1ff')
frame.place(relwidth=1, relheight=1)

titleLabel = tk.Label(frame, text='BASIC CALCULATOR', bg='#80c1ff', font=("Impact", 22))
titleLabel.place(relx=0.5, rely=0.03, anchor='center')

############################################################input fields

#########ADDITION  ---->
addResult = 0
additionLabel = tk.Label(frame, text='ADDITION', bg='#80c1ff', fg='#808080', font=("Impact", 12))
additionLabel.place(relx=0.5, rely=0.1, anchor='center')

add1Text = tk.Entry(frame, text='', width=entryWidth)
add1Text.place(relx=0.05, rely=0.15)

plusLabel = tk.Label(frame, text='+', bg='#80c1ff')
plusLabel.place(relx=0.3, rely=0.15)

add2Text = tk.Entry(frame, text='', width=entryWidth)
add2Text.place(relx=0.35, rely=0.15)

addEqualsLabel = tk.Label(frame, text='=', bg='#80c1ff')
addEqualsLabel.place(relx=0.6, rely=0.15)

addresultLabel = tk.Label(frame, text=addResult, bg='#80c1ff')
addresultLabel.place(relx=0.65, rely=0.15)

def addFunction():
    a = float(add1Text.get())
    b = float(add2Text.get())
    addResult = a + b
    addresultLabel.configure(text = addResult)

calcAdd = tk.Button(frame, text='Calc', fg='white', bg='#00c100', command=addFunction)
calcAdd.place(relx=0.85, rely=0.15)

#########ADDITION  <----

#########SUBSTRACTION ---->
subResult = 0

subLabel = tk.Label(frame, text='SUBSTRACTION', bg='#80c1ff', fg='#808080', font=("Impact", 12))
subLabel.place(relx=0.5, rely=0.25, anchor='center')

sub1Text = tk.Entry(frame, text='', width=entryWidth)
sub1Text.place(relx=0.05, rely=0.3)

minusLabel = tk.Label(frame, text='-', bg='#80c1ff')
minusLabel.place(relx=0.3, rely=0.3)

sub2Text = tk.Entry(frame, text='', width=entryWidth)
sub2Text.place(relx=0.35, rely=0.3)

subEqualsLabel = tk.Label(frame, text='=', bg='#80c1ff')
subEqualsLabel.place(relx=0.6, rely=0.3)

subresultLabel = tk.Label(frame, text=subResult, bg='#80c1ff')
subresultLabel.place(relx=0.65, rely=0.3)

def subFunction():
    a = float(sub1Text.get())
    b = float(sub2Text.get())
    subResult = a - b
    subresultLabel.configure(text = subResult)

calcSub = tk.Button(frame, text = 'Calc',fg='white', bg='#00c100', command=subFunction)
calcSub.place(relx=0.85, rely=0.3)

#########SUBSTRACTION <----

#########MULTIPLICATION ---->
multiResult = 0

multiLabel = tk.Label(frame, text='MULTIPLICATION', bg='#80c1ff', fg='#808080', font=("Impact", 12))
multiLabel.place(relx=0.5, rely=0.4, anchor='center')

multi1Text = tk.Entry(frame, text='', width=entryWidth)
multi1Text.place(relx=0.05, rely=0.45)

multiLabel = tk.Label(frame, text='*', bg='#80c1ff')
multiLabel.place(relx=0.3, rely=0.45)

multi2Text = tk.Entry(frame, text='', width=entryWidth)
multi2Text.place(relx=0.35, rely=0.45)

multiEqualsLabel = tk.Label(frame, text='=', bg='#80c1ff')
multiEqualsLabel.place(relx=0.6, rely=0.45)

multiResultLabel = tk.Label(frame, text=multiResult, bg='#80c1ff')
multiResultLabel.place(relx=0.65, rely=0.45)

def multiplyFunction():
    a = float(multi1Text.get())
    b = float(multi2Text.get())
    multiResult = a * b
    multiResultLabel.configure(text = multiResult)

calcMultiply = tk.Button(frame, text = 'Calc',fg='white', bg='#00c100', command=multiplyFunction)
calcMultiply.place(relx=0.85, rely=0.45)

#########MULTIPLICATION <----

#########DIVISION ---->
divResult = 0

divLabel = tk.Label(frame, text='DIVISION', bg='#80c1ff', fg='#808080', font=("Impact", 12))
divLabel.place(relx=0.5, rely=0.55, anchor='center')

div1Text = tk.Entry(frame, text='', width=entryWidth)
div1Text.place(relx=0.05, rely=0.6)

divLabel = tk.Label(frame, text='/', bg='#80c1ff')
divLabel.place(relx=0.3, rely=0.6)

div2Text = tk.Entry(frame, text='', width=entryWidth)
div2Text.place(relx=0.35, rely=0.6)

errorLabel = tk.Label(frame, text='', width=20, bg='#80c1ff', fg='red')
errorLabel.place(relx=0.35, rely=0.63 )

divEqualsLabel = tk.Label(frame, text='=', bg='#80c1ff')
divEqualsLabel.place(relx=0.6, rely=0.6)

divResultLabel = tk.Label(frame, text=multiResult, bg='#80c1ff')
divResultLabel.place(relx=0.65, rely=0.6)

def divFunction():
    a = float(div1Text.get())
    b = float(div2Text.get())

    try:
        divResult = a / b
        divResultLabel.configure(text=divResult)
    except ZeroDivisionError:
        errorLabel.configure(text='You cannot devide with 0!')
        #time.sleep(1)
        div2Text.delete(0, 'end')


divMultiply = tk.Button(frame, text = 'Calc',fg='white', bg='#00c100', command=divFunction)
divMultiply.place(relx=0.85, rely=0.6)

#########DIVISION <----

#########RESET ALL VALUES

def clearAll():
    add1Text.delete(0, 'end')
    add2Text.delete(0, 'end')
    sub1Text.delete(0, 'end')
    sub2Text.delete(0, 'end')
    multi1Text.delete(0, 'end')
    multi2Text.delete(0, 'end')
    div1Text.delete(0, 'end')
    div2Text.delete(0, 'end')

CAButton = tk.Button(frame, text='Clear All', fg='white', bg='#760000', command=clearAll)
CAButton.place(relx=0.5, rely=0.7, anchor='center', width ='60')

#############################################################end of input fields

def closeWin():
    parentWindow.destroy()

Closebutton = tk.Button(frame, text='Close App', fg='white', bg='#00c100', command=closeWin)
Closebutton.place(relx=0.5,rely=0.95, anchor='center', width = '80')




#entry = tk.Entry(frame)
#entry.pack()


parentWindow.minsize(minWidth, minHeight)
parentWindow.maxsize(minWidth, minHeight)
parentWindow.mainloop()