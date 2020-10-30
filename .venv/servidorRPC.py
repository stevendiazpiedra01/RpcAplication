from xmlrpc.server import SimpleXMLRPCServer

class metodosRPC:

    _metodos_rpc = ['suma']

    def __init__(self, direccion):
        self._datos = {}
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)

        for metodo in self._metodos_rpc:
            self._servidor.register_function(getattr(self, metodo))  
            
    def suma(self,num1 , num2):
       return (num1+num2)
    
    
    def iniciar_servidor(self):
        self._servidor.serve_forever()



            