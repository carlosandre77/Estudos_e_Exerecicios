from tkinter import *

def bt_click():
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())

        lb["text"] = (f'A soma de {num1} mais {num2} é {num1+num2}')
    else:
        lb["text"] = "valores informados invalidos"
janela = Tk()

janela.title("soma de dois numeros")

ed1 = Entry(janela)
ed1.place(x=100, y=100)
ed2 = Entry(janela)
ed2.place(x=100, y=130)

bt = Button(janela, text="SOMA", width=20, command=bt_click)
bt.place(x=100, y=150)

lb = Label(janela, text="")
lb.place(x=100, y=200)

janela.geometry("400x300+200+200")
janela.mainloop()

