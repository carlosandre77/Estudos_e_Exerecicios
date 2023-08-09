"""from tkinter import *

def button_click1():
    print("button_click1")

def button_click2():
    print("button_click2")

janela = Tk()

bt1 = Button(janela, width=20, text="botão 1", command=button_click1)
bt1.place(x=100, y=100)

bt2 = Button(janela, width=20, text="botão 2", command=button_click2)
bt2.place(x=100, y=130)

janela.geometry("300x300+200+200")
janela.mainloop()"""

from functools import partial
from tkinter import *

def bt_click(botao):
    print(botao["text"])

janela = Tk()

bt1 = Button(janela, width=20, text="botão 1")
bt1["command"] =partial(bt_click, bt1)
bt1.place(x=100, y=100)

bt2 = Button(janela, width=20, text="botão 2")
bt2["command"] =partial(bt_click, bt2)
bt2.place(x=100, y=130)

janela.geometry("300x300+200+200")
janela.mainloop()


