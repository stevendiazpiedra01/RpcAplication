import sqlite3
import mysql.connector

from mysql.connector import errorcode
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

    """ REGISTRO TELEFONICO """"           
    
        
    __user__ = 'root'
    __password__ = ''
    __host__ = 'localhost'
    __database__ = '127_0_0_1'
    

    #El constructor establece la conexion con la bbdd
    def __init__(self):
        self.cnx = mysql.connector.connect(user= self.__user__, password= self.__password__,
                              host= self.__host__,
                              database=self.__database__)
        self.cursor = self.cnx.cursor()
        print("Conexion establecida.")

    def insertRegistro(self, fecha, hora_inicio, hora_fin, empleadoID, clienteID):
        self.cursor.execute("INSERT INTO registros (fecha, hora_ inicio," and
                            "hora_fin, empleadoID, clienteID) VALUES(%s,%s,%s,%s,%s)",+
                            (fecha, hora_inicio, hora_fin, empleadoID, clienteID))
        self.cnx.commit()
        self.cursor.execute()