from tkinter import ttk
from tkinter import *
from tkinter.ttk import Combobox
from login import LoginRegistro

log = LoginRegistro()
class Menu:
    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Menu')
        

        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = 'Menu')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

         # Documento Input
        Button(frame,  
                text ="Registro de Empleados",  
                command = self.openNewWindow).grid(row = 1, columnspan = 2, sticky = W + E)
            
        Button(frame,  
                text ="Realizar Llamada a Sucursal Madrid",  
                command = self.openNewWindow).grid(row = 2, columnspan = 2, sticky = W + E)
        
        Button(frame,  
                text ="CERRAR",  
                command = self.quit).grid(row = 3, columnspan = 2, sticky = W + E)

 
    def quit(self):
        self.wind.destroy()

    # sets the geometry of main  
    # root window 

    def openNewWindow(self): 
        log.login()      
   
    
    
    
    
    # a button widget which will open a  
    # new window on button click 
if __name__ == '__main__':
    window = Tk()
    application = Menu(window)
    window.mainloop()
