from tkinter import *

janela= Tk()

lb1 = Label(janela, text="horizontal", bg="white")
lb2 = Label(janela, text="", bg="red")
lb3 = Label(janela, text="", bg="blue")

lb1.pack(side=TOP, fill = X)
lb2.pack(side=LEFT, fill= X)
lb3.pack(side=LEFT, fill=X)


janela.geometry("400x300+200+200")
janela.mainloop()