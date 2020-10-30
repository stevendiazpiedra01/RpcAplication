from servidorRPC import metodosRPC

if __name__ == '__main__':
    rpc = metodosRPC(('',20064))
    print ('Se ha iniciado el servidor RPC.')
    rpc.iniciar_servidor()
                