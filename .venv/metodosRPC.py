import sqlite3
from encriptarCon import *

from datetime import datetime

class metodosRPC:
    def run_query(self, query, parameters = ()):
        db_name = './Sql/dbMadrid.db' 
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

            
    def metodoEncriptacion (self,password):
        self.encStr = crypt.EncryptStringENC(password)
        return self.encStr

    def metodoDesencriptacion (self,password):
        self.decStr = crypt.DecryptStringENC(password)
        return self.decStr


    
    
    # Function to Execute Database Querys
    def reg_usuario(self, docu, tipDocu, nom, ape, tipEmp, clave):
        hoy = datetime.today()
        conAux = (self.metodoEncriptacion(clave))
        query = 'INSERT INTO empleados VALUES(?, ?, ?, ?, ?, ?, ?)'
        parameters =  ( docu, tipDocu, nom, ape, tipEmp, conAux, hoy)
        self.run_query(query, parameters)


    
    
    def del_Emp(self,nomb):
        query = 'DELETE FROM empleados WHERE nombres = ?'
        self.run_query(query, ((str(nomb)), ))
    
    def iniciar_servidor(self):
        self._servidor.serve_forever()



            