from tkinter import *

janela= Tk()

lb1 = Label(janela, text="label 1", bg="green")
lb2 = Label(janela, text="label 2", bg="red")
lb3 = Label(janela, text="label 3", bg="yellow")
lb4 = Label(janela, text="label 4", bg="blue")

lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack(side=BOTTOM)


janela.geometry("400x300+200+200")
janela.mainloop()