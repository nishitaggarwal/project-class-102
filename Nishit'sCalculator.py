#%%
import tkinter as tk
from tkinter import *

window=tk.Tk()
window.title("Nishit's Calculator")
window.geometry("400x400")

var = StringVar()


def fun_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)



def fun_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 

 
def fun_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
 
expression = ""
 
input_text = StringVar()


input_field = Entry(window,textvariable=input_text)
input_field.grid(columnspan=4, ipadx=100, ipady=5)

_1 = Button(window, text='1', fg='white', bg='red', bd=0, height=2, width=7,cursor  = "hand2",command = lambda: fun_click("1"))
_1.grid(row=2, column=0)

_2 = Button(window, text='2', fg='white', bg='red', bd=0,  height=2, width=7,cursor  = "hand2",command = lambda: fun_click("2"))
_2.grid(row=2, column=1)

_3 = Button(window, text='3', fg='white', bg='red', bd=0, height=2, width=7,cursor  = "hand2",command = lambda: fun_click("3"))
_3.grid(row=2, column=2)

_4 = Button(window, text='4', fg='white', bg='red', bd=0,  height=2, width=7,cursor  = "hand2",command = lambda: fun_click("4"))
_4.grid(row=3, column=0)

_5 = Button(window, text='5', fg='white', bg='red', bd=0, height=2, width=7,cursor  = "hand2",command = lambda: fun_click("5"))
_5.grid(row=3, column=1)

_6 = Button(window, text='6', fg='white', bg='red', bd=0,  height=2, width=7,cursor  = "hand2",command = lambda: fun_click("6"))
_6.grid(row=3, column=2)

_7 = Button(window, text='7', fg='white', bg='red', bd=0, height=2, width=7,cursor  = "hand2",command = lambda: fun_click("7"))
_7.grid(row=4, column=0)

_8 = Button(window, text='8', fg='white', bg='red', bd=0,  height=2, width=7,cursor  = "hand2",command = lambda: fun_click("8"))
_8.grid(row=4, column=1)

_9 = Button(window, text='9', fg='white', bg='red', bd=0, height=2, width=7,cursor  = "hand2",command = lambda: fun_click("9"))
_9.grid(row=4, column=2)

_0 = Button(window, text='0', fg='white', bg='red', bd=0,  height=2, width=7,cursor  = "hand2",command = lambda: fun_click("0"))
_0.grid(row=5, column=0)

plus = Button(window, text=' + ', fg='black', bg='red', height=2, width=7,cursor  = "hand2",command = lambda: fun_click("+")) 
plus.grid(row=2, column=3) 
  
minus = Button(window, text=' - ', fg='black', bg='red', height=2, width=7,cursor  = "hand2",command = lambda: fun_click("-")) 
minus.grid(row=3, column=3) 
  
multiply = Button(window, text=' X  ', fg='black', bg='red',height=2, width=7,cursor  = "hand2",command = lambda: fun_click("*")) 
multiply.grid(row=4, column=3) 
  
divide = Button(window, text=' / ', fg='black', bg='red', height=2, width=7,cursor  = "hand2",command = lambda: fun_click("/")) 
divide.grid(row=5, column=3) 
  
equal = Button(window, text=' = ', fg='black', bg='red',  height=2, width=7,cursor  = "hand2",command = lambda: fun_equal()) 
equal.grid(row=5, column=2) 
  
clear = Button(window, text='Clear', fg='black', bg='red',height=2, width=7,cursor  = "hand2",command = lambda: fun_clear()) 
clear.grid(row=5, column='1') 
  
Decimal= Button(window, text='.', fg='black', bg='red',height=2, width=7,cursor  = "hand2",command = lambda: fun_click(".")) 
Decimal.grid(row=6, column=0) 

window.mainloop()


# %%
