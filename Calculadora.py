#Calculadora Simples

from tkinter import *
from tkinter import ttk

#Cores
cor1 = '#b0aeb5' #


janela = Tk()
janela.title('Calculadora')
janela.geometry('335x418')
janela.config(bg=cor1)

frame_tela = Frame (janela, width= 335, height = 50)
frame_tela.grid(row=0, column= 0)

janela.mainloop()