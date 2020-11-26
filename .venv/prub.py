import mysql.connector
import sqlite3
__user__ = 'root'
__password__ = '2020'
__host__ = 'localhost'
__database__ = 'dbcaso5'
class prub():

    def query(self,query,parametros =()):
            self.cnx = mysql.connector.connect(user=__user__, password=__password__,
                                            host=__host__,
                                            database=__database__)
            self.cursor = self.cnx.cursor()
            print("Conexion establecida.")
    
            self.cursor.execute(query,parametros)

            myresult = self.cursor.fetchall()
            
            for x in myresult:
                print(x) 
            return myresult

    def run_query(self, query, parameters=()):
        db_name = './Sql/dbMadrid.db'
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
s = 'SELECT COUNT(1) FROM empleados WHERE numeroDocumento = %s AND clave = %s'
q = 'select numeroDocumento,clave from empleados where numeroDocumento = %s and clave = %s'
params = ('159874','AC50F25EAB3F4681' )
prub.query(prub.query, q, params)