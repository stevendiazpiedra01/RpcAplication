from xmlrpc.client import ServerProxy

s= ServerProxy('http://localhost:20064', allow_none=True)
suma = s.suma(6,6)

print ('Hola care monsa %s' %suma)