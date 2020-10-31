from xmlrpc.server import SimpleXMLRPCServer
import sqlite3
from xmlrpc.client import ServerProxy
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Combobox

class metodosRPC:

    
    _metodos_rpc = ['insertar','mostrar']

    def __init__(self, direccion):
        self._datos = {}
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)

        for metodo in self._metodos_rpc:
            self._servidor.register_function(getattr(self, metodo))  
            
    def insertar(self, numDoc, tipoDoc, nom, ape, tipoEmp):
        conn = sqlite3.connect('./Sql/dbMadrid.db')

        dbQuery = ( 'INSERT INTO empleados (numeroDocumento,idTipoDocumento_FK,nombres,apellidos,idTipoEmpleado_FK)' 
                    'VALUES (:numeroDocumento,:idTipoDocumento_FK,:nombres,:apellidos,:idTipoEmpleado_FK);')
        guardarDatos = {
            'numeroDocumento':numDoc,
            'idTipoDocumento_FK':tipoDoc,
            'nombres':nom,
            'apellidos':ape,
            'idTipoEmpleado_FK':tipoEmp
        }
        
        conn.execute(dbQuery, guardarDatos)
        conn.commit()
        print("Record inserted successfully into Laptop table")
        conn.close()
    
    def mostrar(self):
        conn = sqlite3.connect('./Sql/dbMadrid.db')
        cursor = conn.execute("SELECT * from empleados")
        aux = cursor
        return aux.fetchall() 
    
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

        
    
    
    def iniciar_servidor(self):
        self._servidor.serve_forever()



            