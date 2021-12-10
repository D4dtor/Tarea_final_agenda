class Agenda:
    """Clase Agenda que gestiona listado de Contacto"""
    def __init__(self):
        self.__contactos = []
        self.__abierta = False

    def agregar_contacto(self, contacto):
        """Agrega un Contacto a una lista"""
        self.__contactos.append(contacto)
    
    def listar_contacto(self):
       for c in self.__contactos:
           print(str(c))

    def buscar_contacto(self,consulta):
        n=0
        
        for c in self.__contactos:
            if (consulta in c.get_nombre()):
                print("El nombre ",consulta," está en la agenda")
                n=n+1
            elif (consulta in c.get_telefono()):

                print("El telefono ",consulta," esta en la agenda")
                n=n+1
            elif (consulta in c.get_email()):
                print("El email ",consulta," esta en la agenda")
                n=n+1

        if(n==0):
            print("El termino ",consulta," no está en la agenda")
    def editar_contacto(self,consulta):
        n=0
        
        for c in self.__contactos:
            if (consulta == c.get_nombre()):
                nuevo=str(input("Escriba el nuevo nombre: "))
                c.set_nombre(nuevo)
                n=n+1
            elif (consulta==c.get_telefono()):
                nuevo=str(input("Escriba el nuevo telefono: "))
                c.set_telefono(nuevo) 
                n=n+1
            elif (consulta==c.get_email()):
                nuevo=str(input("Escriba el nuevo email: "))
                c.set_email(nuevo)
                n=n+1
        if(n==0):
            print("El termino ",consulta," no está en la agenda")
        else: 
            self.listar_contacto()


    
    """def eliminar_contacto(self):
       n=0
        borrado= " "
        
        for c in self.__contactos:
            print(str(c))
        x=str(input("Cual contacto desea borrar? "))
           
        for c in self.__contactos:
            if (x in c.get_nombre()):
                c = borrado
                n=n+1

        if(n==0):
            print("El nombre ",x," no está en la agenda")
        pass"""
        
        


    def cerrar_agenda(self):
       self.__abierta = False

    def abrir_agenda(self):
        self.__abierta = True
        while( self.__abierta):
            self.__muestra_menu()
            self.__leer_opcion()
            
    
    def __muestra_menu(self):
        
        """Muestra las opciones disponibles"""
        print("------ SELECCIONA OPCIÓN ------")
        print("| 1.- Listar Contacto: ")
        print("| 2.- Buscar Contacto: ")
        print("| 3.- Editar Contacto: ")
        print("| 4.- Eliminar Contacto: ")
        print("| 5.- Cerrar Agenda: ")
        print("-----------------------")
    
    def __leer_opcion(self):
        """ Función auxiliar para leer datos del Usuario"""
        try:
            opcion = -1
            while((opcion > 4) or (opcion < 1)):
                opcion = int(input(">"))
        except:
            print("Error")     
        
        if(opcion == 1):
            self.listar_contacto()
        elif(opcion == 2 ):
            n=0
            while(n<1):
                consulta=str(input("Escribe el termino que quiera buscar: "))
                n=2
            self.buscar_contacto(consulta)
        elif (opcion==3):
            self.listar_contacto()
            consulta=str(input("Escribe el termino que quiera editar: "))
            self.editar_contacto(consulta)
        elif (opcion==4):
            """consulta=str(input("Escribe el termino que quieras borrar: "))
            self.eliminar_contacto(consulta)"""
            pass
        elif(opcion==5):
            self.cerrar_agenda()

        "Eliminar Contacto"
        
     