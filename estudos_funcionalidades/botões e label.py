from tkinter import *

def bt_click():
    print("bt_click")

    lb["text"] = "funcionou!!"

janela = Tk()

bt = Button(janela, width=20, text="ok", command=bt_click)
bt.place(x=85, y=125)

lb = Label(janela, text="test")
lb.place(x=100, y=150)

janela.geometry("300x300+200+200")
janela.mainloop()
