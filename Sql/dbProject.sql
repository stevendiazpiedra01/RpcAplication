
CREATE TABLE IF NOT EXISTS tipoEmpleado (
	idTipoEmpleado	INTEGER NOT NULL,
	tipoEmpleado	TEXT,
	PRIMARY KEY(idTipoEmpleado)
);
CREATE TABLE IF NOT EXISTS tipoDocumento (
	idTipoDocumeto	INTEGER NOT NULL,
	tipoDocumento	TEXT NOT NULL,
	PRIMARY KEY(idTipoDocumeto)
);
CREATE TABLE IF NOT EXISTS empleados (
	numeroDocumento	INTEGER(10) NOT NULL,
	idTipoDocumento_FK	INTEGER(1) NOT NULL,
	nombres	TEXT(50) NOT NULL,
	apellidos	TEXT(50) NOT NULL,
	idTipoEmpleado_FK	INTEGER NOT NULL,
	clave	TEXT NOT NULL,
	fecIngreso	TEXT,
	PRIMARY KEY(numeroDocumento),
	FOREIGN KEY(idTipoDocumento_FK) REFERENCES tipoDocumento(idTipoDocumeto),
	FOREIGN KEY(idTipoEmpleado_FK) REFERENCES tipoEmpleado(idTipoEmpleado)
);
INSERT INTO tipoEmpleado VALUES (1,'administracion');
INSERT INTO tipoEmpleado VALUES (2,'recepcion');
INSERT INTO tipoDocumento VALUES (1,'C.C.');
INSERT INTO tipoDocumento VALUES (2,'T.I.');
INSERT INTO tipoDocumento VALUES (3,'C.E.');
INSERT INTO tipoDocumento VALUES (4,'P.E.');
INSERT INTO empleados VALUES (123465,1,'ÑLKJHGASDFG','ASDFGHKJGHF',1,'5D35F90EF65610CE','2020-11-20');
INSERT INTO empleados VALUES (159,1,'dis','que',1,'7647A0AF802B1BC8','2020-11-20');
INSERT INTO empleados VALUES (156789,1,'asdf','gfdsa',2,'12F9BD8AB249F72F','2020-11-20');
INSERT INTO empleados VALUES (6986,1,'cont','carro',2,'5C19A7A9771B62DF','2020-11-20 02:00:34.485124');
INSERT INTO empleados VALUES (1022416695,1,'brayan','diaz',1,'EF3C9BFCC8CE4C77ADC22F083BC79A78','2020-11-20 02:04:48.219959');
INSERT INTO empleados VALUES (159874,1,'cayan','merez',1,'AC50F25EAB3F4681','2020-11-20 02:13:25.519312');
INSERT INTO empleados VALUES (2615,1,'cris','camil',2,'DF65A65023BF230E','2020-11-20 02:18:16.699840');
COMMIT;
