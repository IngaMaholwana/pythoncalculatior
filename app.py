import tkinter as tk
from functools import partial

operation = 0

def display_btn(clicked_button):
    current_text = lbl.cget("text")
    if current_text == "Error":
        current_text = ""
    new_text = f"{current_text}{clicked_button}"
    lbl.config(text=new_text)

    if "=" in clicked_button:
        try:
            operation = eval(new_text[:-1])
            lbl.config(text=f"{operation}")
        except:
            lbl.config(text="Error")

def clear_display():
    lbl.config(text="")

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)


lbl = tk.Label(root, text="", height=2, width=12, anchor='e', relief="sunken", font=("Arial", 14))
lbl.grid(row=0, column=0, columnspan=4, padx=5, pady=(5, 10))


buttons = {}
for i in range(1, 10):
    buttons[i] = tk.Button(root, text=f"{i}", height=2, width=4, command=lambda num=i: display_btn(str(num)))
    buttons[i].grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3, padx=1, pady=1)


operators = ["+", "-", "*", "/"]
for i, op in enumerate(operators):
    cmd = partial(display_btn, op)
    btn_op = tk.Button(root, text=op, height=2, width=4, command=cmd)
    btn_op.grid(row=i, column=3, padx=1, pady=1)


btn0 = tk.Button(root, text="0", height=2, width=4, command=lambda: display_btn("0"))
btn0.grid(row=4, column=1, padx=1, pady=(1, 5))

btnDot = tk.Button(root, text=".", height=2, width=4, command=lambda: display_btn("."))
btnDot.grid(row=4, column=0, padx=1, pady=(1, 5))

btnAC = tk.Button(root, text="AC", height=2, width=4, command=clear_display)
btnAC.grid(row=4, column=2, padx=1, pady=(1, 5))

btnEqu = tk.Button(root, text="=", height=2, width=4, command=lambda: display_btn("="))
btnEqu.grid(row=4, column=3, padx=1, pady=(1, 5))

root.mainloop()
