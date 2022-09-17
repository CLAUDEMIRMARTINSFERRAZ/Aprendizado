#Calculadora Simples

from tkinter import *
from tkinter import ttk

#Cores
cor1 = '#b0aeb5' #cinza
cor2 ='#f4f2f7' #Branca
cor3 = '#0c1bed' #Azul 
cor4 = '#e0f52a' #amarelo
cor5 = '#f77605' #Laranja


janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.config(bg=cor1)

#Craindo Frames
frame_tela = Frame (janela, width= 235, height = 50, bg=cor3)
frame_tela.grid(row=0, column= 0)

frame_corpo = Frame (janela, width= 235, height =268)
frame_corpo.grid(row=1, column= 0)

#Criando os botões

b_1 = Button (frame_corpo, text='C', width=11, height=2, bg= cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0,y=0)
b_2 = Button (frame_corpo, text='%', width=11, height=2, bg=cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118,y=0)
b_3 = Button (frame_corpo, text='/', width=11, height=2, bg= cor5, fg= cor2, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177,y=0)


janela.mainloop()