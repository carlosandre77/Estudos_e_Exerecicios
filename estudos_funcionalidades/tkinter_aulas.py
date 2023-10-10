from tkinter import *

janela = Tk()

janela.title("titulo")
janela["bg"] = "red"
janela["background"] = "blue"
Label(janela, text="fala galera").pack()

#LxA+esquerda+ topo
#300x300+100+100
janela.geometry("1366x786+0+0")

janela.mainloop()