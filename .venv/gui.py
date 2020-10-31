import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow , QApplication, QMessageBox


class guiMetodos(QMainWindow):
    def srup(self):
        uic.loadUi("./app/GUI_REG.ui",self)
        self.registrar.clicked.connect(self.insertar)

    def insertar(self):
        docu = self.documento.text()
        tipoDoc = self.tipoDocu.currentText()
        nom = self.nombre.text()
        ape = self.apellido.text()
        tipoEm = self.tipoEmp.currentText()
        if (tipoDoc == 'C.C.'): tipoDoc = 1
        elif (tipoDoc == 'T.I.'): tipoDoc = 2
        elif (tipoDoc == 'C.E.'): tipoDoc = 3
        elif (tipoDoc == 'P.E.'): tipoDoc = 4

        if (tipoEm == 'Administrador'): tipoEm= 1
        elif (tipoEm == 'Recepcionista'): tipoEm = 2

        s.insertar(docu,tipoDoc,nom,ape,tipoEm)
                
        msg = QMessageBox()
        msg.setWindowTitle("Ingresar Datos")
        msg.setText("Datos Ingresados Correctamente!")
        msg.setIcon(QMessageBox.Information)
        msg.exec()

                

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = guiMetodos()
    GUI.srup()
    GUI.show()
    sys.exit(app.exec_())




