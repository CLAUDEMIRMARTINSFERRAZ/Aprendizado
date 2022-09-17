
from tkinter import *
from tkinter import ttk


janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg='white')


#____Divisão de Pagina__

Frame_cima = Frame(janela, width= 295, height=50, bg='white', pady=0, padx=0, relief='flat')
Frame_cima.grid (row=0, column=0, sticky=NSEW)

janela.mainloop()
