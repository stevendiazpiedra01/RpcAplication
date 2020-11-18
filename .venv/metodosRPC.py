import sqlite3
from tkinter import messagebox
class metodosRPC:
    def run_query(self, query, parameters = ()):
        db_name = './Sql/dbMadrid.db' 
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    
    
    # Function to Execute Database Querys
    def reg_usuario(self, docu, tipDocu, nom, ape, tipEmp):
        query = 'INSERT INTO empleados VALUES(?, ?, ?, ?, ?)'
        parameters =  ( docu, tipDocu, nom, ape, tipEmp)
        self.run_query(query, parameters)
            
    def tipEmp(self,tip):
        if (tip == 'Administración'):
            tip = 1
        elif(tip == 'Recepción'):
            tip = 2
        return tip

    def tipDoc(self,tip):
        if (tip == 'C.C.'):
            tip = 1
        elif(tip == 'T.I.'):
            tip = 2
        elif(tip == 'C.E.'):
            tip = 3
        elif(tip == 'P.E.'):
            tip = 4
        return tip
    
    def iniciar_servidor(self):
        self._servidor.serve_forever()



            