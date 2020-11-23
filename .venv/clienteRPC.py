from metodosRPC import metodosRPC
from xmlrpc.client import ServerProxy
from tkinter import ttk
from tkinter import *
from datetime import date

import random
import sqlite3

metodos = metodosRPC()
s= ServerProxy('http://localhost:20064', allow_none=True)


class clienteRpc:
    db_name = '../Sql/dbMadrid.db'
    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Registro de Clientes')
        

        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = 'Registrar Nuevo Empleado')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Documento Input
        Label(frame, text = 'Documento: ').grid(row = 1, column = 0)
        self.docu = Entry(frame)
        self.docu.focus()
        self.docu.grid(row = 1, column = 1)

        Label(frame, text = 'Tipo de Documento: ').grid(row = 2, column = 0)
        self.tipDocu = ttk.Combobox(frame, values=['C.C.', 'T.I.', 'C.E.','P.E.'],width=17,height=1)
        self.tipDocu.grid(row = 2, column = 1)

        # Nombre Input
        Label(frame, text = 'Nombre: ').grid(row = 3, column = 0)
        self.nom = Entry(frame)
        self.nom.grid(row = 3, column = 1)

        # Apellido Input
        Label(frame, text = 'Apellido: ').grid(row = 4, column = 0)
        self.ape = Entry(frame)
        self.ape.grid(row = 4, column = 1)

        Label(frame, text = 'Tipo de Empleado: ').grid(row = 5, column = 0)
        self.tipEmp = ttk.Combobox(frame, values=['Administración', 'Recepción'],width=17,height=1)
        self.tipEmp.grid(row = 5, column = 1)
        
        # Contraseña 
        Label(frame, text = 'Contraseña: ').grid(row = 6, column = 0)
        self.con = Entry(frame,show="*")
        self.con.grid(row = 6, column = 1)
        
        # Confirmación Contraseña
        Label(frame, text = 'Confirmación: ').grid(row = 7, column = 0)
        self.conAux = Entry(frame, show="*")
        self.conAux.grid(row = 7, column = 1)
   
        # Button Add Product 
        ttk.Button(frame, text = 'Registrar', command = self.reg_emp).grid(row = 8, columnspan = 2, sticky = W + E)

        # Output Messages 
        self.message = Label(self.wind,text = '', fg = 'red')
        self.message.grid(row =9 , column = 0, columnspan = 2, sticky = W + E)


        # Table
        self.tree = ttk.Treeview(self.wind,height = 10, columns = ('#0','#1','#2','#3','#4'))
        self.tree.grid(row = 4, column = 0, columnspan = 2)
    
        self.tree.heading('#0', text = 'Nombres', anchor = CENTER)
        self.tree.heading('#1', text = 'Documento', anchor = CENTER)
        self.tree.heading('#2', text = 'Tipo De Documento', anchor = CENTER)
        self.tree.heading('#3', text = 'Apellidos', anchor = CENTER)
        self.tree.heading('#4', text = 'Tipo Empleado', anchor = CENTER)
        self.tree.heading('#5', text = 'Fecha de Ingreso', anchor = CENTER)

        # Buttons
        ttk.Button(self.wind,text = 'ACTUALIZAR REGISTRO', command = self.consultarReg).grid(row = 10, columnspan = 10, sticky = W + E)
        ttk.Button(self.wind,text = 'DELETE', command = self.borrar_Emp).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(self.wind,text = 'EDIT', command = self.edit_Emp).grid(row = 5, column = 1, sticky = W + E)
        ttk.Button(self.wind,text = 'CERRAR', command = self.quit).grid(row = 11, columnspan = 2, sticky = W + E)

        # Filling the Rows
        self.consultar_Usuarios()
    
    # User Input Validation
    def quit(self):
        self.wind.destroy()

    def validation(self):
        return len(self.docu.get()) != 0 and len(self.tipDocu.get()) != 0 and len(self.nom.get()) != 0 and len(self.ape.get()) != 0 and len(self.tipEmp.get()) != 0
    
    def run_query(self, query, parameters = ()):
        db_name = './Sql/dbMadrid.db' 
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def consultarReg(self):
        self.consultar_Usuarios()
        self.message['text'] = 'Registro Actualizado'

    def consultar_Usuarios(self):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM empleados'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('', 3, text = row[2], values = (row[0],self.tipDocview(row[1]),row[3],self.tipEmpView(row[4]),row[6]))
            

    def tipEmpSave(self,tip):
        if (tip == 'Administración'):
            tip = 1
        elif(tip == 'Recepción'):
            tip = 2
        return tip

    def tipEmpView(self,tip):
        if (tip == 1):
            tip = 'Administración'
        elif(tip == 2):
            tip = 'Recepción'
        return tip

    def tipDocSave(self,tip):
        if (tip == 'C.C.'):
            tip = 1
        elif(tip == 'T.I.'):
            tip = 2
        elif(tip == 'C.E.'):
            tip = 3
        elif(tip == 'P.E.'):
            tip = 4
        
        return tip
    
    def tipDocview(self,tipo):
        if (tipo == 1):
            tipo = 'C.C.'
        elif(tipo == 2):
            tipo = 'T.I.'
        elif(tipo == 3):
            tipo = 'C.E.'
        elif(tipo == 4):
            tipo= 'P.E.'
        return tipo

    def reg_emp(self): 
        

        if (self.validation() & (self.con.get() == self.conAux.get() ) ):
            tipEmpAux = self.tipEmpSave(self.tipEmp.get())
            tipDocAux = self.tipDocSave(self.tipDocu.get())
            conAux = self.con.get()
            s.reg_usuario(self.docu.get(), tipDocAux, self.nom.get(), self.ape.get(), tipEmpAux,conAux)
            self.message['text'] = 'Empleado {} Agregado Satisfactoriamente'.format(self.nom.get())
            self.docu.delete(0, END)
            self.tipDocu.delete(0, END)
            self.nom.delete(0, END)
            self.ape.delete(0, END)
            self.tipEmp.delete(0, END)
            self.con.delete(0, END)
            self.conAux.delete(0, END)
        else:
            self.message['text'] = 'OJO, Datos Requeridos o La contraseña No Coincide con la Confirmación'
        self.consultar_Usuarios()

   
    def borrar_Emp(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Por Favor Seleccione Registro'
            return
        self.message['text'] = ''
        nomb = self.tree.item(self.tree.selection())['text']
        s.del_Emp(nomb)
        self.message['text'] = 'Record {} deleted Successfully'.format(nomb)
        self.consultar_Usuarios()
 

    def edit_Emp(self):
        return 0
    
    """ REGISTRO TELEFONICO""""

    def randomDate(self):
        start_dt = date.today().replace(day=1, month=1).toordinal()
        end_dt = date.today().toordinal()
        random_day = date.fromordinal(random.randint(start_dt, end_dt))
        return random_day

    def randomHour(self):
        hour = str(random.randint(0, 24)), ':', str(random.randint(0, 59))
        return ''.join(hour)

    # metodo que debe ejecutar el cliente ->
    # proxy.test(randomDate(), randomHour(), randomHour(), random.randint(1, 3), random.randint(1, 3))
        

if __name__ == '__main__':
    window = Tk()
    application = clienteRpc(window)
    window.mainloop()
