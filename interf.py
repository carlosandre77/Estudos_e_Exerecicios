from tkinter import *
import random
import time;
import datetime

root=Tk()
root.geometry("1350x750+0+0")
root.title("programa TESTE")
root.configure(background='blue')

Tops= Frame (root,width=1350,height=100,bd=9,relief="raise")
Tops.pack(side=TOP)

fleftl= Frame (root,width=900,height=650,bd=8,relief="raise")
fleftl.pack(side=LEFT)

frigthl= Frame (root,width=440,height=650,bd=8,relief="raise")
frigthl.pack(side=RIGHT)

root.mainloop()