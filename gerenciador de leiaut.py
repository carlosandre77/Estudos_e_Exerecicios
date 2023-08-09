from tkinter import *

janela = Tk()
#W x H + L + T
lb= Label(janela, text="1 2 3 testando!!")
lb.place(x=100, y=100)

janela.geometry("300x300+200+200")
janela.mainloop()