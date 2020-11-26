from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3
import mysql.connector
from menu import Menu
from metodosRPC import metodosRPC
from clienteRPC import clienteRpc

metodos = metodosRPC()


class LoginInicial:
    __user__ = 'root'
    __password__ = '2020'
    __host__ = 'localhost'
    __database__ = 'dbcaso5'

    cnx = mysql.connector.connect(user=__user__, password=__password__,
                                       host=__host__,
                                       database=__database__)
    cursor = cnx.cursor()
    print("...")

    def __init__(self, window):

        # Initializations
        self.wind = window
        self.wind.title('Identificación De Acceso')

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text='Login')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Documento
        Label(frame, text='Documento: ').grid(row=1, column=0)
        self.doc = Entry(frame)
        self.doc.grid(row=1, column=1)

        # Confirmación Contraseña
        Label(frame, text='Contraseña: ').grid(row=2, column=0)
        self.con = Entry(frame, show="*")
        self.con.grid(row=2, column=1)

        # Documento Input
        Button(frame,
               text="Ingresar",
               command=self.veriEmp).grid(row=3, columnspan=2, sticky=W + E)

        Button(frame,
               text="CERRAR",
               command=self.quit).grid(row=4, columnspan=2, sticky=W + E)

        # Output Messages
        self.message = Label(self.wind, text='', fg='red')
        self.message.grid(row=5, column=0, columnspan=2, sticky=W + E)

    def abrirMenu(self):
        win = Tk()
        app = Menu(win)
        win.mainloop()

    def quit(self):
        self.wind.destroy()

    def run_query(self, query, parametros=()):

        self.cursor.execute(query, parametros)

        myresult = self.cursor.fetchall()
        self.cnx.commit()
        return myresult

    def veriEmp(self):
        # filling data
        sqlQuery = 'SELECT numeroDocumento,clave FROM empleados WHERE numeroDocumento = %s AND clave = %s'
        desCon = metodos.metodoEncriptacion(self.con.get())
        docuInt = int(self.doc.get())
        params = (docuInt, desCon, )
        query = self.run_query(sqlQuery,params)
        paramse = [params]
        if (query == paramse):
            self.abrirMenu()
        else:
            messagebox.showinfo(title='Error De Autenticación',
                                message='Usuario o Contraseña erroneos.')
        
                
         


class LoginRegistro:

    __user__ = 'root'
    __password__ = '2020'
    __host__ = 'localhost'
    __database__ = 'dbcaso5'

    cnx = mysql.connector.connect(user=__user__, password=__password__,
                                       host=__host__,
                                       database=__database__)
    cursor = cnx.cursor()
    print("...")
    def abrirCliente(self):
        win = Tk()
        app = clienteRpc(win)
        win.mainloop()

    def quit(self):
        self.winds.destroy()

    def run_query(self, query, parametros=()):
    
        self.cursor.execute(query, parametros)

        myresult = self.cursor.fetchall()
        self.cnx.commit()
        return myresult

    def login(self):

        self.winds = Toplevel()
        self.winds.title('Identificación De Acceso')

        # Creating a Frame Container
        frame = LabelFrame(self.winds, text='Login')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Documento
        Label(frame, text='Documento: ').grid(row=1, column=0)
        self.doc = Entry(frame)
        self.doc.grid(row=1, column=1)

        # Confirmación Contraseña
        Label(frame, text='Contraseña: ').grid(row=2, column=0)
        self.con = Entry(frame, show="*")
        self.con.grid(row=2, column=1)

        # Documento Input
        Button(frame,
               text="Ingresar",
               command=self.veriEmpReg).grid(row=3, columnspan=2, sticky=W + E)

        Button(frame,
               text="CERRAR",
               command=self.quit).grid(row=4, columnspan=2, sticky=W + E)

        # Output Messages
        message = Label(self.winds, text='', fg='red')
        message.grid(row=5, column=0, columnspan=2, sticky=W + E)
        message['text'] = 'OJO, Datos Requeridos o La contraseña No Coincide con la Confirmación'

    def veriEmpReg(self):
        # filling data
        sqlQuery = 'SELECT numeroDocumento,clave FROM empleados WHERE numeroDocumento = %s AND clave = %s AND idTipoEmpleado_FK = 1'
        desCon = metodos.metodoEncriptacion(self.con.get())
        docuInt = int(self.doc.get())
        params = (docuInt, desCon, )
        query = self.run_query(sqlQuery,params)
        paramse = [params]
        if (query == paramse):
            self.quit()
            self.abrirCliente()
        else:
            messagebox.showinfo(title='Error De Autenticación',
                            message='Eror de identificacion. \nRAZONES POSIBLES: \n1. No tienes permiso para esta Seccion \n2. Usuario o Contraseña erroneos.')
        


if __name__ == '__main__':
    window = Tk()
    application = LoginInicial(window)
    window.mainloop()
