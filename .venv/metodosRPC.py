from xmlrpc.server import SimpleXMLRPCServer
import sqlite3

class metodosRPC:

    
    _metodos_rpc = ['insertar']

    def __init__(self, direccion):
        self._datos = {}
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)

        for metodo in self._metodos_rpc:
            self._servidor.register_function(getattr(self, metodo))  
            
    def insertar(self):
        nombre = 'brayan'
        conn = sqlite3.connect('./Sql/dbMadrid.db')

        conn.execute("INSERT INTO empleados (numeroDocumento,idTipoDocumento_FK,nombres,apellidos,idTipoEmpleado_FK) "
             "VALUES (1032500168, '1', 'Dayann', 'Useche', '2')")
        conn.commit()
        conn.close()
        return nombre
    
    
    def iniciar_servidor(self):
        self._servidor.serve_forever()



            