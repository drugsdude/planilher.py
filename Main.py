import pyautogui as p
import pymsgbox as msg
from tkinter import *
import Access

janela = Tk()
janela.title("Planilher")
janela.geometry("300x150")


def executa():
    info1 = data1.get().split('/')
    info2 = data2.get().split('/')
    dia1 = int(info1[0])
    dia2 = int(info2[0])
    x = dia1
    p.hotkey('alt','tab')
    while (x <= dia2):
        prim_it = ""
        if (x == dia1):
            prim_it = True
        else:
            prim_it = False
        dt = '0'+ str(x) +"/04/2023" if x<10 else str(x) +"/04/2023"
        Access.importa(dt,prim_it)
        Access.finalizar()
        x += 1
        msg.alert('Rotina finalizada!','System','ok')


#Access.abrirNav()

#Access.iniciar()
texto1 = Label(janela,text = "Insira a Data inicial: ")
texto1.grid(column=0,row=1,padx = 10, pady = 10)

data1 = Entry(janela,width=20)
data1.grid(column=1, row=1)

texto2 = Label(janela,text = "Insira a Data Final: ")
texto2.grid(column=0,row = 2,padx=10,pady=10)

data2 = Entry(janela,width=20)
data2.grid(column=1, row=2)

botao = Button(janela,text="Iniciar",command=executa)
botao.grid(column=1,row=3,padx=20,pady=20)

janela.mainloop()

        
