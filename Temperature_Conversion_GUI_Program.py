from tkinter import *

window=Tk()
window.title('Temperature Conversion')

# https://www.google.com/search?ei=3RvcXZLANe27tgWLl4A4&q=temperature+conversion&oq=temperature+conversion&gs_l=psy-ab.3..0l10.4940.8300..8590...0.2..0.60.971.22......0....1..gws-wiz.......0i71j0i273j0i131j0i67.ERWy2LjuNNE&ved=0ahUKEwjSotnB_YXmAhXtna0KHYsLAAcQ4dUDCAo&uact=5

# Define Fahrenheit to Celsius ->

def F_to_C():
    celsius=(float(F_to_C_value.get())-32)*(5/9)
    t1.delete("1.0",END)
    t1.insert(END,celsius)

# Define Celsius to Fahrenheit ->

def C_to_F():
    fahrenheit=(float(C_to_F_value.get())*(9/5))+32
    t2.delete("1.0",END)
    t2.insert(END,fahrenheit)

# Build GUI for F-to-C ->

b1 = Button(window,text="Execute F-to-C", command=F_to_C)
b1.grid(row=0,column=0)

F_to_C_value=StringVar()
e1=Entry(window,textvariable=F_to_C_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

# Build GUI for C-to-F ->

b2 = Button(window,text="Execute C-to-F", command=C_to_F)
b2.grid(row=1,column=0)

C_to_F_value=StringVar()
e2=Entry(window,textvariable=C_to_F_value)
e2.grid(row=1,column=1)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=2)


window.mainloop()
