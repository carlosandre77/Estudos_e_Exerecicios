from tkinter import *

janela= Tk()

lb1 = Label(janela, text="label 1 ", bg="white")
lb1.grid(row=4, column=3)
lb2 = Label(janela, text="label 2 ", bg="white")
lb2.grid(row=3, column=2)


janela.geometry("500x200+600+200")
janela.mainloop()