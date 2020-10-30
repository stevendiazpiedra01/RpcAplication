from metodosRPC import metodosRPC

if __name__ == '__main__':
    rpc = metodosRPC(('',23000))
    print ('Se ha iniciado el servidor RPC.')
    rpc.iniciar_servidor()
                