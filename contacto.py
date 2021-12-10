class Contacto:
    """ Clase contacto donde se guardan los contactos"""
    def __init__(self, nombre, telefono, email):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
    
    def __str__(self):
        return "Nombre:  {0} Telefono: {1} Email : {2}".format(self.__nombre, self.__telefono, self.__email)
        
    def ver_nombres(self,nombre):
        lista=[]
        lista.append(nombre)

        return lista


    def get_telefono(self):
        """Get Telefono"""
        return self.__telefono
    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
        
'''
c1 = Contacto("manuel", "666.666.666", "c1@email.test")
c1.nombre = "Lucia"
c1.set_telefono("777")
print(str(c1))
'''