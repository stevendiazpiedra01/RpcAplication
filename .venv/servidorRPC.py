from metodosRPC import metodosRPC
from xmlrpc.server import SimpleXMLRPCServer
class servidor(metodosRPC):
    # metodo para agregar registro -> insertRegistro
    _metodos_rpc = ['run_query','reg_usuario','del_Emp','metodoEncriptacion','metodoDesencriptacion', 'insertRegistro']
    db_name = '../Sql/dbMadrid.db' 
    def __init__(self, direccion):
        self._datos = {}
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)

        for metodo in self._metodos_rpc:
            self._servidor.register_function(getattr(self, metodo))  
    
    


if __name__ == '__main__':
    rpc = servidor(('',20064))
    print ('Se ha iniciado el servidor RPC.')
    rpc.iniciar_servidor()
