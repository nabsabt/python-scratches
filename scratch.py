import tkinter as tk

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
num1 = 0
num2 = 0
result =0

#########ADDITION
additionLabel = tk.Label(frame, text='ADDITION', bg='#80c1ff', fg='#808080', font=("Impact", 12))
additionLabel.place(relx=0.5, rely=0.1, anchor='center')

add1Text = tk.Entry(frame, text='number 1', width=entryWidth)
add1Text.place(relx=0.05, rely=0.15)

plusLabel = tk.Label(frame, text='+', bg='#80c1ff')
plusLabel.place(relx=0.3, rely=0.15)

add2Text = tk.Entry(frame, text='number 2', width=entryWidth)
add2Text.place(relx=0.35, rely=0.15)

equalsLabel = tk.Label(frame, text='=', bg='#80c1ff')
equalsLabel.place(relx=0.6, rely=0.15)

addresultLabel = tk.Label(frame, text=result, bg='#80c1ff')
addresultLabel.place(relx=0.65, rely=0.15)

def addFunction():
    result = add1Text.get() + add1Text.get()
    addresultLabel.configure(text = result)

calcAdd = tk.Button(frame, text='Calc', fg='white', bg='#00c100', command=addFunction)
calcAdd.place(relx=0.85, rely=0.15)

#########ADDITION
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