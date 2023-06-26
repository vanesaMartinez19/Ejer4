from tkinter import *
from tkinter import ttk
from functools import partial
from ClaseImaginario import fraccion

class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperando=None
    __segundoOperando=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        self.__ventana.geometry('600x250')
        mainframe = ttk.Frame(self.__ventana, padding="10 20 10 20")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        operatorEntry=ttk.Entry(mainframe, width=20, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))

        panelEntry = ttk.Entry(mainframe, width=40, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))

        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)

        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=3, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=4, row=7, sticky=W)

        ttk.Button(mainframe, text='[i]', command=partial(self.ponerNUMERO, 'i')).grid(column= 5, row=2, sticky=W)
        ttk.Button(mainframe, text='[+]', command=partial(self.ponerNUMERO, '+')).grid(column= 4, row=2, sticky=W)
        ttk.Button(mainframe, text='[-]', command=partial(self.ponerNUMERO, '-')).grid(column= 4, row=3, sticky=W)
        ttk.Button(mainframe, text='C', command=self.__ventana.destroy).grid(column= 5, row=3, sticky=W)

        self.__panel.set('')
        panelEntry.focus()
        self.__ventana.mainloop()

    def ponerNUMERO(self, numero):
        if self.__operadorAux==None:
            valor = self.__panel.get()
            self.__panel.set(valor+numero)
        
        else:
            if '+' in self.__panel.get():
                self.__operadorAux=None
                valor=self.__panel.get().split('+' or '-')
                va = valor[1].split('i')
                self.__primerOperando=fraccion(int(valor[0]),int(va[0]), '+')
                self.__panel.set(numero)
            elif '-' in self.__panel.get():
                self.__operadorAux=None
                valor=self.__panel.get().split('-')
                va = valor[1].split('i')
                self.__primerOperando=fraccion(int(valor[0]),int(va[0]), '-')
                self.__panel.set(numero)
            else:
                self.__operadorAux=None
                valor=self.__panel.get()
                self.__primerOperando=int(valor)
                self.__panel.set(numero)


    def borrarPanel(self):
        self.__panel.set('')

    def resolverOperacion(self, operando1, operacion, operando2):
        resultado=0
        if operacion=='+':
            resultado=operando1+operando2
        else:
            if operacion=='-':
                resultado=operando1-operando2
            else:
                if operacion=='*':
                    resultado=operando1*operando2
                else:
                    if operacion=='%':
                        resultado=operando1/operando2
        self.__panel.set((resultado))

    def ponerOPERADOR(self, op):

        if op=='=':
            operacion=self.__operador.get()
            if '+' in self.__panel.get():
                valor=self.__panel.get().split('+')
                va = valor[1].split('i')
                self.__segundoOperando=fraccion(int(valor[0]),int(va[0]), '+')
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            elif '-' in self.__panel.get():
                valor=self.__panel.get().split('-')
                va = valor[1].split('i')
                self.__segundoOperando=fraccion(int(valor[0]),int(va[0]), '-')
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            else:
                self.__segundoOperando=(self.__panel.get())
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set('')
                self.__operadorAux=None
        else:
            if self.__operador.get()=='':
                self.__operador.set(op)
                self.__operadorAux=op

            else:
                operacion=self.__operador.get()
                self.__segundoOperando=str(self.__panel.get())
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux=op
                
if __name__=='__main__':
    calculadora=Calculadora()