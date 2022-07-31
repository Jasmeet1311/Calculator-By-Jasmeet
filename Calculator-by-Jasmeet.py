#                            Simple calculator using Tkinter
from tkinter import *

root = Tk()
root.geometry("250x390")
root.maxsize(width=250,height=390)
root.minsize(width=250,height=390)
root.title("Calculator")
# Setting icon
root.wm_iconbitmap("3.cal.ico")
# Entry widget at the top

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value=eval(scvalue.get())
            except Exception as e:
                value = ""

        scvalue.set(value)
        screen.update()

    elif text =="c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
def create_buttons(List):
    frame1 = Frame(root, bg="grey")
    for t in List:
        button1 = Button(frame1, text=t, font="lucida 25 bold")
        button1.bind("<Button-1>", click)
        button1.pack(side=LEFT,padx=7,pady=7)
    frame1.pack(anchor="w",padx=5)

scvalue= StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="lucida 30 bold")
screen.pack(fill=X,pady=5,padx=5)

create_buttons(["1","2","3","+"])
create_buttons(["4","5","6","-"])
create_buttons(["7","8","9","*"])
create_buttons(["0","=","c","/"])
root.mainloop()

