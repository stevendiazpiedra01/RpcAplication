from xmlrpc.server import SimpleXMLRPCServer
import sqlite3

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
        
        
    
    
    def iniciar_servidor(self):
        self._servidor.serve_forever()



            