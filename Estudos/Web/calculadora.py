from tkinter import *
from tkinter.ttk import Combobox

janela = Tk()
btnAC = Button(janela, text='AC', bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btnAC.place(x=50, y=100)
btnMaisMenos = Button(janela, text='+/-', bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btnMaisMenos.place(x=114, y=100)
btnPct = Button(janela, text='%', bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btnPct.place(x=178, y=100)
btnDiv = Button(janela, text='/', bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btnDiv.place(x=242, y=100)
btn07 = Button(janela, text=7, bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btn07.place(x=50, y=161)
btn08 = Button(janela, text=8, bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btn08.place(x=114, y=161)
btn09 = Button(janela, text=9, bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btn09.place(x=178, y=161)
btnmult = Button(janela, text='X', bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btnmult.place(x=242, y=161)
btn04 = Button(janela, text=4, bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btn04.place(x=50, y=222)
btn05 = Button(janela, text=5, bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btn05.place(x=114, y=222)
btn06 = Button(janela, text=6, bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btn06.place(x=178, y=222)
btnminus = Button(janela, text='-', bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btnminus.place(x=242, y=222)
btn01 = Button(janela, text=1, bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btn01.place(x=50, y=283)
btn02 = Button(janela, text=2, bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btn02.place(x=114, y=283)
btn03 = Button(janela, text=3, bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btn03.place(x=178, y=283)
btnAdd = Button(janela, text='+', bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btnAdd.place(x=242, y=283)
btn00 = Button(janela, text=0, bg='white',
               fg='black', font='Arial, 14',
               height=2, width=11)
btn00.place(x=50, y=344)
btnComma = Button(janela, text=',', bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btnComma.place(x=178, y=344)
btnEqual = Button(janela, text='=', bg='white',
               fg='black', font='Arial, 14',
               height=2, width=5)
btnEqual.place(x=242, y=344)

janela.title('Calculadora')
janela.geometry('400x500')
janela.mainloop()

