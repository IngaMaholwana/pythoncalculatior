import tkinter as tk 
from functools import partial #the functool helpd work with high order functions. kind of exact like lambda 

def display_btn():
    pass


root = tk.Tk()
root.resizable(False,False) #window cant be resised
root.mainloop()

lbl = tk.Label(root, text="")
lbl.grid(row=0,column=0, columnspan=4,padx=1,pady=(5,1))

buttons = {}
for i in range(1,10):
    buttons[i] = tk.Button(root, text=f"{i}", height=2, width=4, command=lambda num=i : display_btn(num))
    buttons[i].grid(row=(i -1) // 3 + 1, columns=(i - 1) % 3, padx=1, pady=1) 

operators = ["+","-","*","/"]
for i, op in enumerate(operators):  
    cmd = partial(display_btn(), op)
    btn_op = tk.Button(root, takefocus=op, text=op, height=2, width=2, command=cmd)
    btn_op.grid(row=i + 1, column=3, padx=1, pady=1)
    
      