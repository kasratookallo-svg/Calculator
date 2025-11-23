from tkinter import *
import tkinter.messagebox as msg
from tkinter import messagebox


# tkinter event list

def mouse_enter(event):
    widget = event.widget
    widget.config(background="blue")
    widget.config(foreground="white")

def mouse_exit(event):
    widget = event.widget
    widget.config(background="lightblue")
    widget.config(foreground="black")


def mouse_click(event):
    try:
        widget = event.widget
        char = widget["text"]

        if len(result.get()) < 10 :

            if char == "=":
                result.set(round(eval(result.get()), 4))
            elif char == ".":
                if "." not in result.get():
                    result.set(result.get() + ".")
            elif len(result.get()) > 1 and result.get()[-1] not in ["*", " /", "-", "+"]:
                result.set(result.get() + char)
            else:
                result.set(result.get() + char)
    except Exception as e:
        msg.showerror("Error", str(e))

Win = Tk()
Win.geometry("190x220")
Win.title("Calculator")

btn_labels = [
    ["7","8","9","*"],
    ["4","5","6","/"],
    ["1","2","3","-"],
    ["0","+","=","."]

]

result = StringVar()
Entry(Win, textvariable=result , font=("Arial", 14 ), width=13 ).place(x = 10 , y= 10)
for row in range(4):
    for col in range(4):
        btn = Button(Win , text=btn_labels[row][col],width=3, bg = "lightblue")
        btn.place(x = 10 + col*40 , y = 60 + row*40)
        btn.bind("<Button-1>", mouse_click)
        btn.bind("<Enter>", mouse_enter)
        btn.bind("<Leave>", mouse_exit)

Win.mainloop()

