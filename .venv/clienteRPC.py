

from xmlrpc.client import ServerProxy
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Combobox

import sqlite3

s= ServerProxy('http://localhost:20064', allow_none=True)
class guiMetodos:
    db_name = './Sql/dbMadrid.db'
    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Products Application')

        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = 'Registrar Nuevo Empleado')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Documento Input
        Label(frame, text = 'Documento: ').grid(row = 1, column = 0)
        self.docu = Entry(frame)
        self.docu.focus()
        self.docu.grid(row = 1, column = 1)

        Label(frame, text = 'Tipo de Documento: ').grid(row = 2, column = 0)
        self.tipDocu = ttk.Combobox(frame, values=['AB', 'BC', 'MB', 'NB', 'NL', 'NS'],width=17,height=1)
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
        self.tipEmp = ttk.Combobox(frame, values=['AB', 'BC', 'MB', 'NB', 'NL', 'NS'],width=17,height=1)
        self.tipEmp.grid(row = 5, column = 1)
        
   
        # Button Add Product 
        ttk.Button(frame, text = 'Registrar', command = self.reg_usuario).grid(row = 6, columnspan = 2, sticky = W + E)

        # Output Messages 
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 7, column = 0, columnspan = 2, sticky = W + E)


        # Table
        self.tree = ttk.Treeview(height = 10, columns = ('#0','#1','#2','#3'))
        self.tree.grid(row = 4, column = 0, columnspan = 2)
    
        self.tree.heading('#0', text = 'Documento', anchor = CENTER)
        self.tree.heading('#1', text = 'Tipo Documento', anchor = CENTER)
        self.tree.heading('#2', text = 'Nombres', anchor = CENTER)
        self.tree.heading('#3', text = 'Apellidos', anchor = CENTER)
        self.tree.heading('#4', text = 'Tipo Empleado', anchor = CENTER)

        # Buttons
        ttk.Button(text = 'DELETE', command = self.delete_product).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'EDIT', command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)

        # Filling the Rows
        self.consultar_Usuarios()

    # Function to Execute Database Querys
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Get Products from Database
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
            self.tree.insert('', 3, text = row[0], values = (row[1],row[2],row[3],row[4]))


    # User Input Validation
    def validation(self):
        return len(self.docu.get()) != 0 and len(self.tipDocu.get()) != 0 and len(self.nom.get()) != 0 and len(self.ape.get()) != 0 and len(self.tipDocu.get()) != 0

    def reg_usuario(self):
        if self.validation():
            query = 'INSERT INTO empleados VALUES(?, ?, ?, ?, ?)'
            parameters =  (self.docu.get(), self.tipDocu.get(), self.nom.get(), self.ape.get(), self.tipEmp.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Empleado {} Agregado Satisfactoriamente'.format(self.nom.get())
            self.docu.delete(0, END)
            self.tipDocu.delete(0, END)
            self.nom.delete(0, END)
            self.ape.delete(0, END)
            self.tipEmp.delete(0, END)
        else:
            self.message['text'] = 'OJO, Datos Requeridos'
        self.consultar_Usuarios()
    
    def delete_product(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        nomb = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM empleados WHERE documento = ?'
        self.run_query(query, (nomb, ))
        self.message['text'] = 'Record {} deleted Successfully'.format(nomb)
        self.consultar_Usuarios()

     
        
    def edit_product(self):
        return 0


if __name__ == '__main__':
    window = Tk()
    application = guiMetodos(window)
    window.mainloop()
