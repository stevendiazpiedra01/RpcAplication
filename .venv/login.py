from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3

from menu import Menu
from metodosRPC import metodosRPC
from clienteRPC import clienteRpc

metodos = metodosRPC()
class LoginInicial:
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
        self.message['text'] = 'OJO, Datos Requeridos o La contraseña No Coincide con la Confirmación'
        
    def abrirMenu(self):
        win = Tk()
        app = Menu(win)
        win.mainloop()

    def mees(self):
        self.message['text'] = 'No ha ingresado'
    def quit(self):
        self.wind.destroy()

    def run_query(self, query, parameters=()):
        db_name = './Sql/dbMadrid.db'
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    

    def veriEmp(self):
        # filling data
        sqlq = "SELECT COUNT(1) FROM empleados WHERE numeroDocumento = ? AND clave = ? "
        desCon = metodos.metodoEncriptacion(self.con.get())
        query = self.run_query(sqlq,(int(self.doc.get()),desCon, ))
        if (query.fetchone()[0]):
            self.abrirMenu()
        else:
            messagebox.showinfo(title='Error De Autenticación', message='Usuario o Contraseña erroneos.')
        query.close()

class LoginRegistro:
    
    

    
    def abrirCliente(self):
        win = Tk()
        app = clienteRpc(win)
        win.mainloop()

    def quit(self):
        self.winds.destroy()

    def run_query(self, query, parameters=()):
        db_name = './Sql/dbMadrid.db'
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result  
    
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
                command= self.veriEmpReg).grid(row=3, columnspan=2, sticky=W + E)

        Button(frame,
                text="CERRAR",
                command=self.quit).grid(row=4, columnspan=2, sticky=W + E)

            # Output Messages
        message = Label(self.winds, text='', fg='red')
        message.grid(row=5, column=0, columnspan=2, sticky=W + E)
        message['text'] = 'OJO, Datos Requeridos o La contraseña No Coincide con la Confirmación'    

        
    def veriEmpReg(self):
            # filling data
        sqlq = "SELECT COUNT(1) FROM empleados WHERE numeroDocumento = ? AND clave = ? AND idTipoEmpleado_FK = 1"
        desCon = metodos.metodoEncriptacion(self.con.get())
        query = self.run_query(sqlq,(int(self.doc.get()),desCon, ))
        if (query.fetchone()[0]):
            self.quit()
            self.abrirCliente()
                
        else:
            messagebox.showinfo(title='Error De Autenticación', message='Usuario o Contraseña erroneos.')
        query.close()
    

    
   
        
if __name__ == '__main__':
    window = Tk()
    application = LoginInicial(window)
    window.mainloop()
