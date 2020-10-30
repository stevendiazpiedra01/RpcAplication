from xmlrpc.client import ServerProxy

s= ServerProxy('http://localhost:20064', allow_none=True)
insertar = s.insertar()

print ('Hola care monda %s' %insertar)