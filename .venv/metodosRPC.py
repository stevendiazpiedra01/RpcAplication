import sqlite3
import mysql.connector

from mysql.connector import errorcode
from encriptarCon import *

from datetime import datetime

class metodosRPC:
    __user__ = 'root'
    __password__ = '2020'
    __host__ = 'localhost'
    __database__ = 'dbcaso5'
    conx = mysql.connector.connect(user= __user__, password= __password__,
                              host= __host__,
                              database=__database__)
    cursor = conx.cursor()
    print("Conexion establecida.")


            
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
        sqlQuery = 'INSERT INTO empleados (name, address) VALUES (%s, %s)'
        query = 'INSERT INTO empleados (numeroDocumento, idTipoDocumento_FK , nombres , apellidos,idTipoEmpleado_FK,clave,fecIngreso) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        parameters =  ( docu, tipDocu, nom, ape, tipEmp, conAux, hoy)
        self.cursor.execute(query, parameters)
        self.conx.commit()
  



    
    
    def del_Emp(self,nomb):
        querySql ='DELETE FROM empleados WHERE nombres = %s'
        nombAux = (nomb, )
        self.cursor.execute(querySql,nombAux)
        self.conx.commit()
  
      

   
    
    def iniciar_servidor(self):
        self._servidor.serve_forever()

     

    #El constructor establece la conexion con la bbdd
    

    def insertRegistro(self, fecha, hora_inicio, hora_fin, empleadoID, clienteID):
        self.cursor.execute("INSERT INTO registros (fecha, hora_ inicio," and
                            "hora_fin, empleadoID, clienteID) VALUES(%s,%s,%s,%s,%s)",+
                            (fecha, hora_inicio, hora_fin, empleadoID, clienteID))
                         
        self.conx.commit()
        self.cursor.execute()